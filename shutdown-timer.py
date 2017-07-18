from PyQt5.QtWidgets import (QApplication, QDialog, QLabel,
                             QLineEdit, QPushButton, QTextEdit)
from PyQt5.QtCore import (QTimer, QRect, Qt)

class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Timer")
        self.setFixedSize(262, 40)
        
        self.timer = QTimer(self)
        
        self.hour_value = 0
        self.minute_value = 0
        self.second_value = 0
        
        self.hour = QLineEdit(self)
        self.hour.setGeometry(QRect(10, 10, 21, 21))
        
        self.label = QLabel(":", self)
        self.label.setGeometry(QRect(30, 10, 12, 21))
        self.label.setAlignment(Qt.AlignCenter)
        
        self.minute = QLineEdit(self)
        self.minute.setGeometry(QRect(40, 10, 21, 21))

        self.label_2 = QLabel(":", self)
        self.label_2.setGeometry(QRect(60, 10, 12, 21))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.second = QLineEdit(self)
        self.second.setGeometry(QRect(70, 10, 21, 21))
        
        self.start_btn = QPushButton("Start", self)
        self.start_btn.setGeometry(QRect(100, 10, 51, 21))

        self.pause_btn = QPushButton("Pause", self)
        self.pause_btn.setGeometry(QRect(150, 10, 51, 21))

        self.stop_btn = QPushButton("Stop", self)
        self.stop_btn.setGeometry(QRect(200, 10, 51, 21))

        #####
        
        self.start_btn.clicked.connect(self.res)
        self.pause_btn.clicked.connect(self.pause)
        self.stop_btn.clicked.connect(self.stop)
        self.timer.timeout.connect(self.update)

    def res(self):
        self.timer.stop()
        self.hour_value = int(self.hour.text())
        self.minute_value = int(self.minute.text())
        self.second_value = int(self.second.text())

        self.hour.setText(str(self.hour_value))
        self.minute.setText(str(self.minute.text()))
        self.second.setText(str(self.second.text()))
        self.timer.start(1000)

    def update(self):
        if self.hour_value == 0 and self.minute_value == 0 and self.second_value == 0:
            self.timer.stop()
            self.execOperation()
        elif self.second_value == 0:
            if self.minute_value > 0:
                self.second_value = 59
                self.minute_value -= 1
            else:
                self.second_value = 59
                if self.hour_value > 0:
                    self.minute_value = 59
                    self.hour_value -= 1     
        else:
            self.second_value -= 1
        
        self.hour.setText(str(self.hour_value).zfill(2))
        self.second.setText(str(self.second_value).zfill(2))
        self.minute.setText(str(self.minute_value).zfill(2))
        
    def pause(self):
        if self.pause_btn.text() == "Pause":
            self.timer.stop()
            self.pause_btn.setText("Resume")
        else:
            self.timer.start(1000)
            self.pause_btn.setText("Pause")
        
    def stop(self):
        self.timer.stop()
        self.hour.setText(str(0).zfill(2))
        self.second.setText(str(0).zfill(2))
        self.minute.setText(str(0).zfill(2))
        
    def execOperation(self):
        os.system(r"timeout -t 0 -nobreak && shutdown -s -t 0")
        
        
if __name__ == "__main__":
    import sys
    import os
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    
    sys.exit(dialog.exec_())
        
        
