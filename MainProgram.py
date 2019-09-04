# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 22:31:11 2019

@author: xuanm
"""

from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QGraphicsRectItem, QGraphicsScene, QMessageBox, QMainWindow
import cv2
import sys
import MainWindow
import time
import datetime
import serial
import numpy as np

def get_file_name(path, base_name, no_camera):
    day = list(time.localtime()[0:3])
    day_str = [str(i) for i in day]
    for i in range(len(day_str)):
        if day[i] < 10:
            day_str[i] = ''.join(('0', day_str[i]))
    day_str = ''.join(day_str)
    
    t=list(time.localtime()[3:6])
    t_str = [str(i) for i in t]
    for i in range(len(t)):
        if t[i] < 10:
           t_str[i] = ''.join(('0', t_str[i]))	
    t_str = ''.join(t_str)
    file_name = ''.join((path, base_name, '_', day_str, '_', t_str, '_', str(no_camera+1), '.avi'))
    file_name_txt = ''.join((path, base_name, '_', day_str, '_', t_str, '_', str(no_camera+1), '.txt'))
    return file_name, file_name_txt
    
def add_timestr(img):
    t_str = datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3]
    color=(0,0,255)
    cv2.putText(img, t_str, (20, 20) ,cv2.FONT_HERSHEY_SIMPLEX ,0.8, color,2)
    return img    

class MainProgram(QWidget):
    def __init__(self): 
        app = 0
        app = QtWidgets.QApplication(sys.argv)
        super().__init__()
        MainProgram = QMainWindow()
        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(MainProgram)
        
        self.flag_preview = 1
        
        self.timer_camera = QtCore.QTimer()
        self.timer_serial = QtCore.QTimer()
        self.timer_camera.timeout.connect(self.show_camera)
        self.timer_serial.timeout.connect(self.serial_timer_trigger)
        self.cap = []
        self.N = 4
        
        self.base_file_name = 'Video'
        self.path = './'
        
        self.video_out = []
        self.txt_out = []
        self.flag_recording = 0
        self.start_time = 0
        
        self.action_connect()
        MainProgram.show()
        self.ui.release_cameras.setEnabled(False)
        self.ui.Button_endrecording.setEnabled(False)
        sys.exit(app.exec_())
    
    def action_connect(self):
        self.ui.open_cameras.clicked.connect(self.open_cameras_clicked)
        self.ui.close_preview.clicked.connect(self.close_preview_clicked)
        self.ui.release_cameras.clicked.connect(self.release_cameras_clicked)
        self.ui.open_preview.clicked.connect(self.open_preview_clicked)
        self.ui.Button_filename.clicked.connect(self.Button_filename_clicked)
        self.ui.Button_savepath.clicked.connect(self.Button_savepath_clicked)
        self.ui.Button_recording.clicked.connect(self.Button_recording_clicked)
        self.ui.Button_endrecording.clicked.connect(self.Button_endrecording_clicked)
        self.ui.Button_trigger.clicked.connect(self.Button_trigger_clicked)
        self.ui.Button_canceltrigger.clicked.connect(self.Button_canceltrigger_clicked)

    def open_cameras_clicked(self):
        for i in range(self.N):
            temp = cv2.VideoCapture(i)
            if temp.isOpened() == True:
                self.cap.append(temp)
                print(i)
            else:
                temp.release()
        
        self.timer_camera.start(30)
        self.ui.open_cameras.setEnabled(False)
        self.ui.release_cameras.setEnabled(True)
        
    def release_cameras_clicked(self):
        self.timer_camera.stop()
        len_cap = len(self.cap)
        if self.flag_preview == 1:
            cv2.destroyAllWindows()
        if len_cap != 0:
            for i in range(len_cap):
                self.cap[i].release()
        self.cap = []
        self.ui.open_cameras.setEnabled(True)
        self.ui.release_cameras.setEnabled(False)
        

    def close_preview_clicked(self):
        self.flag_preview = 0
        cv2.destroyAllWindows()
        
    def open_preview_clicked(self):
        self.flag_preview = 1
        
    def Button_filename_clicked(self):
        self.base_file_name = self.ui.Edit_filename.text()
        if self.base_file_name == "":
           self.base_file_name = "Video"
        print(self.base_file_name)
    
    def Button_savepath_clicked(self):
        self.path = QFileDialog.getExistingDirectory(self, "Choose the path", './')
        self.path = ''.join((self.path, "/"))
        self.ui.Label_savepath.setText(self.path)
        print(self.path)
        
    def Button_recording_clicked(self):
        self.video_out = []
        self.txt_out = []
        len_cap = len(self.cap)
        if len_cap != 0:
            for i in range(len_cap):
                save_name, save_name_txt = get_file_name(self.path, self.base_file_name, i)
                print(save_name)
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                self.video_out.append(cv2.VideoWriter(save_name,fourcc, 30.0, (640,480)))
                self.txt_out.append(open(save_name_txt, 'w'))
                self.start_time = int(round(time.time() * 1000))
            self.flag_recording = 1
            self.ui.Button_endrecording.setEnabled(True)
            self.ui.Button_recording.setEnabled(False)
            if self.flag_preview == 1:
                self.ui.Label_mrecordingtime.setText("Recording")
            else:
                self.ui.Label_mrecordingtime.setText("Recording without preview")
        else:
            QMessageBox.information(self, "Info", "Please open cameras first", QMessageBox.Yes | QMessageBox.No)
        
    def Button_endrecording_clicked(self):
        self.ui.Label_mrecordingtime.setText("")
        len_out = len(self.video_out)
        self.flag_recording = 0
        self.ui.Button_endrecording.setEnabled(False)
        self.ui.Button_recording.setEnabled(True)
        if len_out != 0:
            for i in range(len_out):
                self.video_out[i].release()
                self.txt_out[i].close()
            self.video_out = []
            self.txt_out = []
    
    def Button_trigger_clicked(self):
        len_cap = len(self.cap)
        self.video_out = []
        self.txt_out = []
        if len_cap != 0:
            try:
               self.my_serial = serial.Serial('COM4', 115200, timeout=0.5)
            except:
               print('error with the serial port')
            else:
               print("Waiting for triggering signal")
               self.timer_serial.start(5)
               self.ui.Button_trigger.setEnabled(False)
        else:
            QMessageBox.information(self, "Info", "Please open cameras first", QMessageBox.Yes | QMessageBox.No)
    
    def serial_timer_trigger(self):
        len_cap = len(self.cap)
        data = self.my_serial.read_all()
        if data != b'' :
           if data == b"STR":
              if self.flag_recording == 0:
                  if len_cap != 0:
                    for i in range(len_cap):
                        save_name, save_name_txt = get_file_name(self.path, self.base_file_name, i)
                        print(save_name)
                        fourcc = cv2.VideoWriter_fourcc(*'XVID')
                        self.video_out.append(cv2.VideoWriter(save_name,fourcc, 30.0, (640,480)))
                        self.txt_out.append(open(save_name_txt, 'w'))
                        self.start_time = int(round(time.time() * 1000))
                    self.flag_recording = 1
                    if self.flag_preview == 1:
                        self.ui.Label_trecordingtime.setText("Recording")
                    else:
                        self.ui.Label_trecordingtime.setText("Recording without preview")
              print("receive : ",data)

           if data == b"END":
              self.ui.Label_trecordingtime.setText("")
              len_out = len(self.video_out)
              self.flag_recording = 0
              if len_out != 0:
                 for i in range(len_out):
                     self.video_out[i].release()
                     self.txt_out[i].close()
                 self.video_out = []
                 self.txt_out = []
              print("receive : ",data)  
       
    def Button_canceltrigger_clicked(self):   
        if hasattr(self, 'my_serial'):
           if self.my_serial.isOpen():
              self.timer_serial.stop()
              self.my_serial.close()
              self.ui.Button_trigger.setEnabled(True)
              print("***********The serial port is closed*****************")

        
    def show_camera(self): 
        len_cap = len(self.cap)
        if len_cap != 0:
            for i in range(len_cap):    
                ret, frame = self.cap[i].read()
                if not ret:
                    print("Failed to read Camera No. %d" % (i))
                else:
                    show = cv2.resize(frame, (640, 480))
                    #show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
                    show = add_timestr(show)
                    window_name = ''.join(['Video', str(i+1)])
                    if self.flag_preview == 1:
                        cv2.imshow(window_name, show)
                    if self.flag_recording == 1:
                        self.video_out[i].write(show)
                        current_time = int(round(time.time() * 1000))
                        dt = (current_time - self.start_time)/1000
                        self.txt_out[i].write(str(dt))
                        self.txt_out[i].write('\t')
                        self.txt_out[i].write(datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3])
                        self.txt_out[i].write('\n')
    
        
if __name__ == "__main__":
    MainProgram()

    
    
    
    
    
    
    
