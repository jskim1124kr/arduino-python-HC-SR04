from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time
import serial

ser = serial.Serial('COM3')


class DistanceThread(QObject):

    sig_numbers = pyqtSignal(int)
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.startTime = 0
        self.checkTime = 0
        self.count = 0
    @pyqtSlot()
    def run(self):
        self.startTime = QDateTime.currentDateTime().toString("hh:mm:ss").split(":")
        startHour = int(self.startTime[0])
        if startHour > 12:
            startHour = startHour - 12
        startMin = int(self.startTime[1])
        startSec = int(self.startTime[2])
        self.startTime = "[ " + str(startHour) + " ] 시" + \
                       "[ " + str(startMin) + " ] 분" + \
                       "[ " + str(startSec) + " ] 초"
        ser.flush()
        while True:
            ser.write([0])
            distance = ser.readline().decode()
            distance = distance.strip().strip()
            distance = int(distance)
            self.sig_numbers.emit(distance)
            if distance < 10:
                self.count +=1
                if self.count == 3: ser.write([1])
                elif self.count == 5: ser.write([2])
                elif self.count == 7: ser.write([3])
            time.sleep(1)







