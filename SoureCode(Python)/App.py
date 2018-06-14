from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import*
import re
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm



import os



from worker import *


class Ui_MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.name = ""
        self.age = ""
        self.gender = ""
        self.jumin = ""
        self.date = ""
        self.job = ""
        self.level = ""
        self.total_count = 0
        self.count = 0
        self.totalTime = ""
        self.saveMin = 0
        self.loadCnt = []
        self.loadTime = []

        self.check_tab = QWidget()
        self.checkStartBtn = QPushButton(self.check_tab)

        self.runningTime = ""
        self.endTime = 0

        self.startHour = 0
        self.startMin = 0
        self.startSec  = 0

        self.endHour = 0
        self.endMin = 0
        self.endSec = 0


        self.timer = QTimer()

        self.timer.timeout.connect(self.displayTime)
        self.timer.start(1000)

        self.worker1 = DistanceThread()
        self.worker_thread1 = QThread()
        self.worker1.moveToThread(self.worker_thread1)
        self.worker_thread1.start()

        self.updateSec = 0
        self.updateMin = 0
        self.updateHour = 0



        self.three_sec = 0
        self.five_sec = 0
        self.seven_sec = 0



        self._DistanceSignals()



    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QRect(20, 10, 751, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QWidget()
        self.tab1.setObjectName("tab1")


        self.label = QLabel(self.tab1)
        self.label.setGeometry(QRect(10, 10, 500, 100))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label = QLabel(self.tab1)
        self.label.setGeometry(QRect(10, 10, 600, 100))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(30)
        self.label.setText("Slim Life - 건강한 배변활동 도우미 ")
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.logoImage = QLabel(self.tab1)
        self.logoImage.setGeometry(QRect(570, 10, 600, 100))
        self.logoImage.setPixmap(QPixmap("logo.png"))
        self.logoImage.setObjectName("logoImage")

        self.tab_line1 = QFrame(self.tab1)
        self.tab_line1.setGeometry(QRect(10, 80, 700, 100))
        self.tab_line1.setFrameShape(QFrame.HLine)
        self.tab_line1.setFrameShadow(QFrame.Sunken)
        self.tab_line1.setObjectName("tab_line1")




        self.mainLabel = QLabel(self.tab1)
        self.mainLabel.setGeometry(QRect(10, 120, 800, 100))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(25)
        self.mainLabel.setText("건강한 배변습관을 위한 첫 걸음, Slim Life 입니다. ")
        self.mainLabel.setFont(font)
        self.mainLabel.setObjectName("mainLabel")

        self.number1 = QLabel(self.tab1)
        self.number1.setGeometry(QRect(10, 220, 600, 100))
        self.number1.setPixmap(QPixmap("one.png"))
        self.number1.setObjectName("number1")

        self.number1Label = QLabel(self.tab1)
        self.number1Label.setGeometry(QRect(100, 217, 800, 100))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(20)
        self.number1Label.setText("변비 및 치질등의 증상으로 고생하고 계시는 분들 !!")
        self.number1Label.setFont(font)
        self.number1Label.setObjectName("number1Label")


        self.number2 = QLabel(self.tab1)
        self.number2.setGeometry(QRect(10, 330, 600, 100))
        self.number2.setPixmap(QPixmap("two.png"))
        self.number2.setObjectName("number2")

        self.number2Label = QLabel(self.tab1)
        self.number2Label.setGeometry(QRect(100, 327, 800, 100))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(20)
        self.number2Label.setText("스마트폰 사용으로 지나치게 변기에 오래 앉아계시는 분들 !!")
        self.number2Label.setFont(font)
        self.number2Label.setObjectName("number2Label")


        self.number3 = QLabel(self.tab1)
        self.number3.setGeometry(QRect(10, 440, 600, 100))
        self.number3.setPixmap(QPixmap("three.png"))
        self.number3.setObjectName("number3")

        self.number3Label = QLabel(self.tab1)
        self.number3Label.setGeometry(QRect(100, 437, 800, 100))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(20)
        self.number3Label.setText("배변 활동 개선을 원하시는 모든 분들 !!")
        self.number3Label.setFont(font)
        self.number3Label.setObjectName("number3Label")



        self.tabWidget.addTab(self.tab1, "")


        self.info_tab = QWidget()
        self.info_tab.setObjectName("info_tab")
        self.label_2 = QLabel(self.info_tab)
        self.label_2.setGeometry(QRect(10, 10, 161, 41))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.namelabel = QLabel(self.info_tab)
        self.namelabel.setGeometry(QRect(10, 60, 51, 21))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(16)
        self.namelabel.setFont(font)
        self.namelabel.setObjectName("namelabel")
        self.nameEdit = QTextEdit(self.info_tab)
        self.nameEdit.setGeometry(QRect(60, 60, 131, 21))
        self.nameEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.nameEdit.setObjectName("nameEdit")
        self.genderLabel = QLabel(self.info_tab)
        self.genderLabel.setGeometry(QRect(10, 90, 41, 21))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(16)
        self.genderLabel.setFont(font)
        self.genderLabel.setObjectName("genderLabel")
        self.maleCheck = QCheckBox(self.info_tab)
        self.maleCheck.setGeometry(QRect(60, 90, 51, 16))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(11)
        font.setUnderline(True)
        self.maleCheck.setFont(font)
        self.maleCheck.setObjectName("maleCheck")
        self.femaleCheck = QCheckBox(self.info_tab)
        self.femaleCheck.setGeometry(QRect(130, 90, 51, 16))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(11)
        font.setUnderline(True)
        self.femaleCheck.setFont(font)
        self.femaleCheck.setObjectName("femaleCheck")
        self.ageLabel = QLabel(self.info_tab)
        self.ageLabel.setGeometry(QRect(10, 120, 51, 21))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(16)
        self.ageLabel.setFont(font)
        self.ageLabel.setObjectName("ageLabel")
        self.ageEdit = QTextEdit(self.info_tab)
        self.ageEdit.setGeometry(QRect(60, 120, 71, 21))
        self.ageEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ageEdit.setObjectName("ageEdit")
        self.jobLabel = QLabel(self.info_tab)
        self.jobLabel.setGeometry(QRect(10, 150, 51, 21))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(16)
        self.jobLabel.setFont(font)
        self.jobLabel.setObjectName("jobLabel")
        self.jobEdit = QTextEdit(self.info_tab)
        self.jobEdit.setGeometry(QRect(60, 150, 71, 21))
        self.jobEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.jobEdit.setObjectName("jobEdit")
        self.numLabel = QLabel(self.info_tab)
        self.numLabel.setGeometry(QRect(10, 190, 91, 21))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(16)
        self.numLabel.setFont(font)
        self.numLabel.setObjectName("numLabel")
        self.num1Edit = QTextEdit(self.info_tab)
        self.num1Edit.setGeometry(QRect(100, 190, 91, 21))
        self.num1Edit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.num1Edit.setObjectName("num1Edit")
        self.num2Edit = QTextEdit(self.info_tab)
        self.num2Edit.setGeometry(QRect(210, 190, 91, 21))
        self.num2Edit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.num2Edit.setObjectName("num2Edit")
        self.dateLabel = QLabel(self.info_tab)
        self.dateLabel.setGeometry(QRect(10, 240, 91, 21))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(16)
        self.dateLabel.setFont(font)
        self.dateLabel.setObjectName("dateLabel")
        self.dateCalender = QCalendarWidget(self.info_tab)
        self.dateCalender.setGeometry(QRect(100, 240, 301, 211))
        self.dateCalender.setObjectName("dateCalender")

        self.temp = QLabel(self.info_tab)
        self.temp.setGeometry(QRect(20, 490, 110, 21))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(16)
        self.temp.setFont(font)
        self.temp.setText("성명 : ")
        self.temp.setObjectName("temp")

        self.loadName = QTextEdit(self.info_tab)
        self.loadName.setGeometry(QRect(70, 490, 110, 21))
        self.loadName.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.loadName.setObjectName("loadName")

        self.loadBtn = QPushButton(self.info_tab)
        self.loadBtn.setGeometry(QRect(200, 480, 130, 41))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(14)
        self.loadBtn.setFont(font)
        self.loadBtn.setText("불러오기")
        self.loadBtn.setObjectName("loadBtn")

        self.saveButton = QPushButton(self.info_tab)
        self.saveButton.setGeometry(QRect(590, 480, 141, 41))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(14)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")





        self.line = QFrame(self.info_tab)
        self.line.setGeometry(QRect(410, 0, 20, 521))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QFrame(self.info_tab)
        self.line_2.setGeometry(QRect(0, 40, 421, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QFrame(self.info_tab)
        self.line_3.setGeometry(QRect(0, 220, 421, 16))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QFrame(self.info_tab)
        self.line_4.setGeometry(QRect(0, 460, 421, 16))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_3 = QLabel(self.info_tab)
        self.label_3.setGeometry(QRect(440, 10, 91, 31))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line_5 = QFrame(self.info_tab)
        self.line_5.setGeometry(QRect(420, 40, 321, 16))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.namelabel_2 = QLabel(self.info_tab)
        self.namelabel_2.setGeometry(QRect(430, 60, 51, 21))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(16)
        self.namelabel_2.setFont(font)
        self.namelabel_2.setObjectName("namelabel_2")
        self.genderLabel_2 = QLabel(self.info_tab)
        self.genderLabel_2.setGeometry(QRect(430, 100, 41, 21))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(16)
        self.genderLabel_2.setFont(font)
        self.genderLabel_2.setObjectName("genderLabel_2")
        self.ageLabel_2 = QLabel(self.info_tab)
        self.ageLabel_2.setGeometry(QRect(430, 140, 51, 21))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(16)
        self.ageLabel_2.setFont(font)
        self.ageLabel_2.setObjectName("ageLabel_2")
        self.jobLabel_2 = QLabel(self.info_tab)
        self.jobLabel_2.setGeometry(QRect(430, 180, 51, 21))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(16)
        self.jobLabel_2.setFont(font)
        self.jobLabel_2.setObjectName("jobLabel_2")
        self.numLabel_2 = QLabel(self.info_tab)
        self.numLabel_2.setGeometry(QRect(430, 220, 91, 21))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(16)
        self.numLabel_2.setFont(font)
        self.numLabel_2.setObjectName("numLabel_2")
        self.dateLabel_2 = QLabel(self.info_tab)
        self.dateLabel_2.setGeometry(QRect(430, 260, 91, 21))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(16)
        self.dateLabel_2.setFont(font)
        self.dateLabel_2.setObjectName("dateLabel_2")


        self.nameResult = QLabel(self.info_tab)
        self.nameResult.setGeometry(QRect(480, 60, 56, 21))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(16)
        self.nameResult.setFont(font)
        self.nameResult.setObjectName("nameResult")



        self.genderResult = QLabel(self.info_tab)
        self.genderResult.setGeometry(QRect(480, 100, 56, 21))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(16)
        self.genderResult.setFont(font)
        self.genderResult.setObjectName("genderResult")


        self.ageResult = QLabel(self.info_tab)
        self.ageResult.setGeometry(QRect(480, 140, 56, 21))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(16)
        self.ageResult.setFont(font)
        self.ageResult.setObjectName("ageResult")



        self.jobResult = QLabel(self.info_tab)
        self.jobResult.setGeometry(QRect(480, 181, 56, 21))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(16)
        self.jobResult.setFont(font)
        self.jobResult.setObjectName("jobResult")


        self.numResult = QLabel(self.info_tab)
        self.numResult.setGeometry(QRect(520, 220, 300, 21))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(16)
        self.numResult.setFont(font)
        self.numResult.setObjectName("numResult")


        self.dateResult = QLabel(self.info_tab)
        self.dateResult.setGeometry(QRect(520, 260, 300, 21))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(16)
        self.dateResult.setFont(font)
        self.dateResult.setObjectName("dateResult")

        self.plotHelp = QLabel(self.info_tab)
        self.plotHelp.setGeometry(QRect(440, 300, 500, 150))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(13)
        self.plotHelp.setFont(font)
        self.plotHelp.setText("배변활동 주기를 보기 원하시는 분들은" +"\n" +
                              "불러오기 후 활동 주기 버튼을 클릭해주세요!" +"\n" +"\n" +
                              "! 사전에 검사하신 분은.. " + "\n" +
                              "성명 입력, 불러오기 후 검사해주세요.")
        self.plotHelp.setObjectName("plotHelp")
        self.plotHelp.setStyleSheet("QLabel#plotHelp {color:blue}")

        self.plotting = QPushButton(self.info_tab)
        self.plotting.setGeometry(QRect(430, 480, 150, 41))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(15)
        self.plotting.setFont(font)
        self.plotting.setText("활동 주기")
        self.plotting.setObjectName("plotting")

        self.tabWidget.addTab(self.info_tab, "")



        self.check_tab.setObjectName("check_tab")

        self.timeLabel = QLabel(self.check_tab)
        self.timeLabel.setGeometry(QRect(10, 0, 171, 71))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(28)
        self.timeLabel.setFont(font)
        self.timeLabel.setObjectName("timeLabel")

        self.time = QLabel(self.check_tab)
        self.time.setGeometry(QRect(180, -3, 171, 71))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(28)
        self.time.setFont(font)
        self.time.setObjectName("time")



        self.distanceLabel = QLabel(self.check_tab)
        self.distanceLabel.setGeometry(QRect(15, 70, 400, 110))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(30)
        self.distanceLabel.setFont(font)
        self.distanceLabel.setText("사용중이지 않습니다.")
        self.distanceLabel.setObjectName("distanceLabel")


        self.usingImage = QLabel(self.check_tab)
        self.usingImage.setGeometry(QRect(330, 70, 400, 100))
        self.usingImage.setPixmap(QPixmap("미사용.png"))





        self.check = QLabel(self.check_tab)
        self.check.setGeometry(QRect(15, 150, 450, 100))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(25)
        self.check.setFont(font)
        self.check.setObjectName("check")

        self.alramLabel = QLabel(self.check_tab)
        self.alramLabel.setGeometry(QRect(15, 230, 450, 100))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(25)
        self.alramLabel.setFont(font)
        self.alramLabel.setText("사용 수준 : ")
        self.alramLabel.setObjectName("alramLabel")

        self.alram = QLabel(self.check_tab)
        self.alram.setGeometry(QRect(160, 220, 450, 100))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(25)
        self.alram.setFont(font)
        self.alram.setPixmap(QPixmap("양호1.png"))
        self.alram.setObjectName("alram")






        self.runningTimeLabel = QLabel(self.check_tab)
        self.runningTimeLabel.setGeometry(QRect(15, 310, 400, 100))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(20)
        self.runningTimeLabel.setFont(font)
        self.runningTimeLabel.setText("총 사용 시간")
        self.runningTimeLabel.setObjectName("runningTimeLabel")

        self.runningTimeLabel2 = QLabel(self.check_tab)
        self.runningTimeLabel2.setGeometry(QRect(15, 360, 600, 100))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(15)
        self.runningTimeLabel2.setFont(font)
        self.runningTimeLabel2.setObjectName("runningTimeLabel2")





        self.checkStartBtn.setGeometry(QRect(10, 460, 171, 51))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(26)
        self.checkStartBtn.setFont(font)
        self.checkStartBtn.setObjectName("checkStartBtn")


        self.line_11 = QFrame(self.check_tab)
        self.line_11.setGeometry(QRect(0, 60, 731, 16))
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QFrame(self.check_tab)
        self.line_12.setGeometry(QRect(0, 215, 731, 16))
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QFrame(self.check_tab)
        self.line_13.setGeometry(QRect(0, 170, 731, 16))
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QFrame(self.check_tab)
        self.line_14.setGeometry(QRect(0, 320, 731, 16))
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)
        self.line_14.setObjectName("line_14")




        self.line_17 = QFrame(self.check_tab)
        self.line_17.setGeometry(QRect(0, 440, 731, 16))
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)
        self.line_17.setObjectName("line_17")


        self.tabWidget.addTab(self.check_tab, "")
        self.result_tab = QWidget()
        self.result_tab.setObjectName("result_tab")
        self.resultName = QLabel(self.result_tab)
        self.resultName.setGeometry(QRect(20, 20, 191, 51))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(40)
        self.resultName.setFont(font)
        self.resultName.setText("")
        self.resultName.setObjectName("resultName")
        self.label_8 = QLabel(self.result_tab)
        self.label_8.setGeometry(QRect(240, 30, 61, 31))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(26)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")


        self.resutlLabel = QLabel(self.result_tab)
        self.resutlLabel.setGeometry(QRect(330, 20, 191, 51))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(36)
        self.resutlLabel.setFont(font)
        self.resutlLabel.setObjectName("resutlLabel")



        self.label_12 = QLabel(self.result_tab)
        self.label_12.setGeometry(QRect(30, 110, 400, 31))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(25)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        self.result4 = QLabel(self.result_tab)
        self.result4.setGeometry(QRect(200, 110, 91, 31))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(25)
        self.result4.setFont(font)
        self.result4.setObjectName("result4")

        self.label_13 = QLabel(self.result_tab)
        self.label_13.setGeometry(QRect(30, 180, 400, 31))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(25)
        self.label_13.setFont(font)
        self.label_13.setText("총 사용 시간 : ")
        self.label_13.setObjectName("label_13")




        self.result5 = QLabel(self.result_tab)
        self.result5.setGeometry(QRect(220, 145, 600, 100))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(25)
        self.result5.setFont(font)
        self.result5.setObjectName("result5")

        self.label_14 = QLabel(self.result_tab)
        self.label_14.setGeometry(QRect(30, 250, 400, 31))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(25)
        self.label_14.setFont(font)
        self.label_14.setText("진단 결과")
        self.label_14.setObjectName("label_14")

        self.result6 = QLabel(self.result_tab)
        self.result6.setGeometry(QRect(30, 290, 800, 100))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(17)
        self.result6.setFont(font)
        self.result6.setObjectName("result6")

        self.result7 = QLabel(self.result_tab)
        self.result7.setGeometry(QRect(30, 390, 800, 100))
        self.result7.setObjectName("result6")





        self.line_16 = QFrame(self.result_tab)
        self.line_16.setGeometry(QRect(10, 80, 731, 16))
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_17 = QFrame(self.result_tab)
        self.line_17.setGeometry(QRect(10, 150, 731, 16))
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.line_18 = QFrame(self.result_tab)
        self.line_18.setGeometry(QRect(10, 220, 731, 16))
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.line_19 = QFrame(self.result_tab)



        self.tabWidget.addTab(self.result_tab, "")



        self.food_tab = QWidget()

        self.foodName = QLabel(self.food_tab)
        self.foodName.setGeometry(QRect(30, 5, 200, 100))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(30)
        self.foodName.setFont(font)
        self.foodName.setObjectName("foodName")


        self.foodTemp1 = QLabel(self.food_tab)
        self.foodTemp1.setGeometry(QRect(200, 5, 200, 100))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(26)
        self.foodTemp1.setFont(font)
        self.foodTemp1.setText("님께 ")
        self.foodTemp1.setObjectName("foodTemp1")

        self.foodTemp2 = QLabel(self.food_tab)
        self.foodTemp2.setGeometry(QRect(270, 30, 400, 51))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(36)
        self.foodTemp2.setFont(font)
        self.foodTemp2.setText(" 맞는 추천 식이요법 !")

        self.foodTemp2.setObjectName("foodTemp2")

        self.foodLine1 = QFrame(self.food_tab)
        self.foodLine1.setGeometry(QRect(10, 80, 731, 16))
        self.foodLine1.setFrameShape(QFrame.HLine)
        self.foodLine1.setFrameShadow(QFrame.Sunken)
        self.foodLine1.setObjectName("foodLine1")

        self.foodLine2 = QFrame(self.food_tab)
        self.foodLine2.setGeometry(QRect(10, 280, 731, 16))
        self.foodLine2.setFrameShape(QFrame.HLine)
        self.foodLine2.setFrameShadow(QFrame.Sunken)
        self.foodLine2.setObjectName("foodLine2")


        self.food1 = QLabel(self.food_tab)
        self.food1.setGeometry(QRect(10, 280, 200, 100))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(25)
        self.food1.setFont(font)
        self.food1.setText("추천 식단")
        self.food1.setObjectName("food1")
        self.food1.setStyleSheet("QLabel#food1 {color:blue}")

        self.food2 = QLabel(self.food_tab)
        self.food2.setGeometry(QRect(10, 5, 700, 370))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(17)
        self.food2.setFont(font)
        self.food2.setText("공통 실천 사항" + "\n" + "\n"+
                           "1. 매일 일정시간에 규칙적으로 식사한다."+ "\n" +
                           "2. 흰쌀 보다는 현미, 보리, 콩, 수수, 귀리 등 잡곡을 이용한다."+ "\n" +
                           "3. 적어도 하루에 1.5L ~ 2L의 수분을 섭취한다." + "\n" +
                           "4. 마음을 편안하게 가지고 스트레스를 해소한다. "+ "\n" +
                           "5. 과일과 채소는 껍질째 섭취하고, 두류를 자주 이용한다.")
        self.food2.setObjectName("food2")

        self.breakFast = QLabel(self.food_tab)
        self.breakFast.setGeometry(QRect(10, 320, 200, 100))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(20)
        self.breakFast.setFont(font)
        self.breakFast.setText("아침")
        self.breakFast.setObjectName("breakFast")

        self.lunch = QLabel(self.food_tab)
        self.lunch.setGeometry(QRect(290, 320, 200, 100))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(20)
        self.lunch.setFont(font)
        self.lunch.setText("점심")
        self.lunch.setObjectName("lunch")

        self.dinner = QLabel(self.food_tab)
        self.dinner.setGeometry(QRect(540, 320, 200, 100))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(20)
        self.dinner.setFont(font)
        self.dinner.setText("저녁")
        self.dinner.setObjectName("dinner")

        self.breakFast2 = QLabel(self.food_tab)
        self.breakFast2.setGeometry(QRect(10, 340, 500, 200))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(15)
        self.breakFast2.setFont(font)

        self.breakFast2.setObjectName("breakFast2")

        self.lunch2 = QLabel(self.food_tab)
        self.lunch2.setGeometry(QRect(290, 340, 270, 200))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(15)
        self.lunch2.setFont(font)
        self.lunch2.setObjectName("lunch2")

        self.dinner2 = QLabel(self.food_tab)
        self.dinner2.setGeometry(QRect(540, 340, 270, 200))
        font = QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(15)
        self.dinner2.setFont(font)
        self.dinner2.setObjectName("dinner2")


        self.tabWidget.addTab(self.food_tab, "")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)


        self.function()

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Slim Life ver 1.0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Slim Life 는?"))
        self.label_2.setText(_translate("MainWindow", "인적사항 작성"))
        self.namelabel.setText(_translate("MainWindow", "성명 : "))
        self.genderLabel.setText(_translate("MainWindow", "성별"))
        self.maleCheck.setText(_translate("MainWindow", "남성"))
        self.femaleCheck.setText(_translate("MainWindow", "여성"))
        self.ageLabel.setText(_translate("MainWindow", "나이 : "))
        self.jobLabel.setText(_translate("MainWindow", "직업 : "))
        self.numLabel.setText(_translate("MainWindow", "주민번호 :"))
        self.dateLabel.setText(_translate("MainWindow", "검사 일자"))
        self.saveButton.setText(_translate("MainWindow", "저장하기"))
        self.label_3.setText(_translate("MainWindow", "인적사항"))
        self.namelabel_2.setText(_translate("MainWindow", "성명 : "))
        self.genderLabel_2.setText(_translate("MainWindow", "성별"))
        self.ageLabel_2.setText(_translate("MainWindow", "나이 : "))
        self.jobLabel_2.setText(_translate("MainWindow", "직업 : "))
        self.numLabel_2.setText(_translate("MainWindow", "주민번호 :"))
        self.dateLabel_2.setText(_translate("MainWindow", "검사 일자"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.info_tab), _translate("MainWindow", "인적사항 작성"))
        self.timeLabel.setText(_translate("MainWindow", "현재시간 : "))
        self.checkStartBtn.setText(_translate("MainWindow", "검사시작"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.check_tab), _translate("MainWindow", "검사하기"))
        self.label_8.setText(_translate("MainWindow", "님의 "))
        self.resutlLabel.setText(_translate("MainWindow", "검사 결과"))
        self.label_12.setText(_translate("MainWindow", "측정 수준 :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.result_tab), _translate("MainWindow", "결과보기"))




        self.tabWidget.setTabText(self.tabWidget.indexOf(self.food_tab), _translate("MainWindow", "식이요법"))


    def function(self):
        self.saveButton.clicked.connect(self.saveBtn_clicked)
        self.loadBtn.clicked.connect(self.loadBtn_clicekd)
        self.plotting.clicked.connect(self.plotting_clicked)

    @pyqtSlot(int)
    def Distanceupdates(self, dis):

        if dis < 10:


            self.distanceLabel.setText("화장실 사용중 입니다.")
            self.usingImage.setPixmap(QPixmap("사용.png"))
            self.updateSec += 1
            self.count += 1

            if self.updateSec >= 3:
                self.updateSec = 0
                self.updateMin += 1
                self.saveMin += 1

            self.check.setText("경과 시간 : " +
                               str(self.updateMin) + " 분" +
                               str(self.updateSec) + " 초")

            self.totalTime = (str(self.updateMin) + " 분" +
                              str(self.updateSec) + " 초")

            if self.count >= 3:
                self.level = "경고"
                self.alram.setPixmap(QPixmap("경고1.png"))
                if self.count >= 5:
                    self.level = "위험"
                    self.alram.setPixmap(QPixmap("위험1.png"))
                    if self.count >= 7:
                        self.level = "고위험"
                        self.alram.setPixmap(QPixmap("고위험1.png"))
                    if self.count < 3:
                        self.level = "양호"

        if dis >= 10:
            self.distanceLabel.setText("사용중이지 않습니다.")
            self.usingImage.setPixmap(QPixmap("미사용.png"))
            self.alram.setPixmap(QPixmap("양호1.png"))
            self.updateSec = 0
            self.updateMin = 0
            self.check.setText("경과 시간 : " +
                               str(self.updateMin) + " 분" +
                               str(self.updateSec) + " 초")
            self._DistanceThreadReset()

    def _DistanceSignals(self):
        self.checkStartBtn.clicked.connect(self.worker1.run)
        self.worker1.sig_numbers.connect(self.Distanceupdates)

    def saveBtn_clicked(self):

        answer = QMessageBox.question(self, "작성완료", "작성하신 내용이 맞습니까?", QMessageBox.Yes, QMessageBox.No)
        if answer == QMessageBox.Yes:
            self.name = self.nameEdit.toPlainText()
            self.age = self.ageEdit.toPlainText()
            self.job = self.jobEdit.toPlainText()

            gender_choice = self.maleCheck.checkState()
            if int(gender_choice) is 2:
                self.gender = "남성"
            else:
                self.gender = "여성"

            num1 = self.num1Edit.toPlainText()
            num2 = self.num2Edit.toPlainText()
            self.jumin = str(num1) + "-" + str(num2)
            date = self.dateCalender.selectedDate()
            date = (str(date)[18:])
            date = re.sub('[()]', '', date)
            date = date.split(",")
            self.date = (str(date[0]) + "년" + str(date[1]) + "월" + str(date[2]) + "일")

            self.nameResult.setText(self.name)
            self.ageResult.setText(self.age)
            self.jobResult.setText(self.job)
            self.numResult.setText(self.jumin)
            self.genderResult.setText(self.gender)
            self.dateResult.setText(self.date)
        if answer == QMessageBox.No:
            QMessageBox.about(self,"작성 취소","다시 작성해주세요.")

    def loadBtn_clicekd(self):
        if os.path.exists(self.loadName.toPlainText()):
            with open(self.loadName.toPlainText(),'r',encoding='utf-8') as txt:
                for i in txt:
                    i = i.strip().split(",")
                    self.loadCnt.append(i[0])
                    self.loadTime.append(i[1])
                print(self.loadCnt)
                print(self.loadTime)
            QMessageBox.about(self, "검사 정보", self.loadName.toPlainText() + "님의 검사 정보를 불러왔습니다.")
        else:
            QMessageBox.about(self, "검사 정보", "검사 정보가 존재하지 않습니다.")

    def _DistanceThreadReset(self):

        if self.worker_thread1.isRunning():
            self.worker1.count = 0
            self.worker_thread1.terminate()
            self.worker_thread1.wait()
            self.worker_thread1.start()

            self.endTime = QDateTime.currentDateTime().toString("hh:mm:ss").split(":")
            self.endHour = int(self.endTime[0])
            if self.endHour > 12:
                self.endHour = self.endHour-12
            self.endMin = int(self.endTime[1])
            self.endSec = int(self.endTime[2])
            self.endTime = "[ " + str(self.endHour) + " ] 시간" + \
                           "[ " + str(self.endMin) + " ] 분" + \
                           "[ " + str(self.endSec) + " ] 초"

            self.runningTime = "[ 검사 시작 시간 ] : " + str(self.worker1.startTime) + "\n" + \
                               "[ 검사 종료 시간 ] : " + str(self.endTime)


            self.runningTimeLabel2.setText(self.runningTime)

            self.resultName.setText(str(self.name))

            self.count = 0
            self.updateSec = 0
            self.updateMin = 0
            self.distanceLabel.setText("사용중이지 않습니다.")
            self.check.setText("사용중이지 않습니다.")
            self.alram.setPixmap(QPixmap("양호1.png"))
            self.usingImage.setPixmap(QPixmap("미사용.png"))
            self.result5.setText(self.totalTime)
            self.foodName.setText(self.name)
            if self.level != "위험" and self.level != "경고" and self.level != "고위험":
                self.result4.setText("양호")
            else:
                self.result4.setText(self.level)

            if self.level == "경고":
                self.result6.setText("5분 이상 변기에 앉아 있으면 항문 주위의 혈류량이 증가해" + "\n" +
                                     "치질이 발생할 수 있습니다. 긴 시간은 아니지만, 조심해주세요 !")
                self.result7.setPixmap(QPixmap("경고평가.png"))
                self.breakFast2.setText(
                    "현미밥 (1공기)" + "\n" +
                    "시금치된장국 (1그릇)" + "\n" +
                    "고등어무조림 (1토막)" + "\n" +
                    "고사리나물 (1접시)" + "\n" +
                    "건포도채소샐러드 (1접시)")
                self.lunch2.setText(
                    "잡곡밥 (1공기)" + "\n" +
                    "비지찌개 (1그릇)" + "\n" +
                    "연근곤약조림 (1토막)" + "\n" +
                    "미나리나물 (1접시)" + "\n" +
                    "총각김치 (1접시)")
                self.dinner2.setText(
                    "팥밥 (1공기)" + "\n" +
                    "미역국 (1그릇)" + "\n" +
                    "쇠고기버섯볶음 (1토막)" + "\n" +
                    "부추해물전 (1접시)" + "\n" +
                    "도라지생채 (1접시)")
            elif self.level == "위험":
                self.result6.setText("10~15분 가량 변기에 앉아있으면 항문 조임근이나 배변근들의 문제로" + "\n" +
                                     "배출장애형 변비가 발생할 수 있어요. 배변활동 관리가 필요해요.")
                self.result7.setPixmap(QPixmap("위험평가.png"))
                self.breakFast2.setText(
                    "잡곡밥 (1공기)" + "\n" +
                    "청국장 (1그릇)" + "\n" +
                    "고구마조림(1토막)" + "\n" +
                    "브로콜리 (1접시)" + "\n" +
                    "바나나(1토막)")
                self.lunch2.setText(
                    "보리밥 (1공기)" + "\n" +
                    "표고버섯 소고기국 (1그릇)" + "\n" +
                    "미나리나물 (1접시)" + "\n" +
                    "요구르트 (1개)")
                self.dinner2.setText(
                    "현미밥 (1공기)" + "\n" +
                    "콩나물국 (1그릇)" + "\n" +
                    "양배추소고기 볶음 (1그릇)" + "\n" +
                    "둥글레차 (1잔)")

            elif self.level == "고위험":
                self.result6.setText("15분 이상 변기에 앉아 있으면 골반과 괄약근에 많은 힘이 가해지는데" + "\n" +
                                     "이러한 힘들이 항문과 직장에 굉장한 압박을 가해 탈장을 유발할수 있어요!" + "\n" +
                                     "배변활동 치료가 필요해요 !")
                self.result7.setPixmap(QPixmap("고위험평가.png"))
                self.breakFast2.setText("병원치료가 시급합니다 ! 식단 보다는 병원에 방문하세요 !!")
                self.dinner2.setText("")
                self.lunch2.setText("")

            else:
                self.result6.setText("배변활동이 양호하십니다. 앞으로도 이렇게 쭉 관리해주세요!")
                self.result7.setPixmap(QPixmap("양호평가.png"))
                self.breakFast2.setText("배변 활동이 양호하시네요 !! 지금처럼 맛있게 먹고 관리해주세요 !")
                self.dinner2.setText("")
                self.lunch2.setText("")

            if os.path.exists(self.loadName.toPlainText()):

                with open(self.loadName.toPlainText(), 'a', encoding='utf-8') as txt:
                    lastCnt = int(self.loadCnt.pop())
                    txt.write(str(lastCnt+1) + "," + str(self.saveMin) +"\n")

            else:
                with open(self.name, 'w', encoding='utf-8') as txt:

                    txt.write(str(1) + "," + str(self.saveMin) + "\n")

            QMessageBox.about(self, "검사 종료", "검사를 종료합니다.")

    def displayTime(self):
        temp = QDateTime.currentDateTime().toString("hh:mm:ss")
        self.time.setText(temp)

    def plotting_clicked(self):

        x_axis = []
        y_axis = []
        for i in range(1, int(self.loadCnt.pop())+1,  1):
            x_axis.append(i)

        for i in self.loadTime:
            y_axis.append(int(i))

        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.plot(x_axis,y_axis,color="g",marker="o",linestyle="--",label ="배변활동주기")
        ax.set_title(self.loadName.toPlainText()+ "님의 배변활동 주기")
        ax.set_xlabel("배변 횟수")
        ax.set_ylabel("이용 시간")
        ax.legend(loc="best")
        plt.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
