# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sb_server.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(775, 416)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 84, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(76, 70, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 28, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 37, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 27, 34))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 43, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 97, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 28, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 84, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(76, 70, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 28, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 37, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 27, 34))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 43, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 97, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 28, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 28, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 84, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(76, 70, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 28, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 37, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 28, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 28, 35))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 43, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 43, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 56, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 60, 171, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.Label_Score1 = QtWidgets.QLabel(self.frame)
        self.Label_Score1.setGeometry(QtCore.QRect(0, 0, 171, 171))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.Label_Score1.setFont(font)
        self.Label_Score1.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Score1.setObjectName("Label_Score1")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(210, 60, 171, 171))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.Label_Score2 = QtWidgets.QLabel(self.frame_2)
        self.Label_Score2.setGeometry(QtCore.QRect(0, 0, 171, 171))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.Label_Score2.setFont(font)
        self.Label_Score2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Label_Score2.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Score2.setObjectName("Label_Score2")
        self.TextBox_Team1 = QtWidgets.QTextEdit(self.centralwidget)
        self.TextBox_Team1.setGeometry(QtCore.QRect(20, 20, 131, 31))
        self.TextBox_Team1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TextBox_Team1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.TextBox_Team1.setLineWidth(1)
        self.TextBox_Team1.setObjectName("TextBox_Team1")
        self.TextBox_Team2 = QtWidgets.QTextEdit(self.centralwidget)
        self.TextBox_Team2.setGeometry(QtCore.QRect(210, 20, 131, 31))
        self.TextBox_Team2.setObjectName("TextBox_Team2")
        self.Frame_Team1 = QtWidgets.QFrame(self.centralwidget)
        self.Frame_Team1.setGeometry(QtCore.QRect(20, 240, 171, 151))
        self.Frame_Team1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_Team1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_Team1.setObjectName("Frame_Team1")
        self.SpinBox_Score1 = QtWidgets.QSpinBox(self.Frame_Team1)
        self.SpinBox_Score1.setGeometry(QtCore.QRect(110, 100, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SpinBox_Score1.setFont(font)
        self.SpinBox_Score1.setObjectName("SpinBox_Score1")
        self.Button_Goal1 = QtWidgets.QPushButton(self.Frame_Team1)
        self.Button_Goal1.setGeometry(QtCore.QRect(10, 50, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Button_Goal1.setFont(font)
        self.Button_Goal1.setObjectName("Button_Goal1")
        self.Button_SetScore1 = QtWidgets.QPushButton(self.Frame_Team1)
        self.Button_SetScore1.setGeometry(QtCore.QRect(10, 100, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Button_SetScore1.setFont(font)
        self.Button_SetScore1.setObjectName("Button_SetScore1")
        self.TextBox_WhoGoaled1 = QtWidgets.QTextEdit(self.Frame_Team1)
        self.TextBox_WhoGoaled1.setGeometry(QtCore.QRect(10, 10, 151, 31))
        self.TextBox_WhoGoaled1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TextBox_WhoGoaled1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.TextBox_WhoGoaled1.setLineWidth(1)
        self.TextBox_WhoGoaled1.setObjectName("TextBox_WhoGoaled1")
        self.Frame_Team2 = QtWidgets.QFrame(self.centralwidget)
        self.Frame_Team2.setGeometry(QtCore.QRect(210, 240, 171, 151))
        self.Frame_Team2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_Team2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_Team2.setObjectName("Frame_Team2")
        self.SpinBox_Score2 = QtWidgets.QSpinBox(self.Frame_Team2)
        self.SpinBox_Score2.setGeometry(QtCore.QRect(110, 100, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SpinBox_Score2.setFont(font)
        self.SpinBox_Score2.setObjectName("SpinBox_Score2")
        self.Button_Goal2 = QtWidgets.QPushButton(self.Frame_Team2)
        self.Button_Goal2.setGeometry(QtCore.QRect(10, 50, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Button_Goal2.setFont(font)
        self.Button_Goal2.setObjectName("Button_Goal2")
        self.Button_SetScore2 = QtWidgets.QPushButton(self.Frame_Team2)
        self.Button_SetScore2.setGeometry(QtCore.QRect(10, 100, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Button_SetScore2.setFont(font)
        self.Button_SetScore2.setObjectName("Button_SetScore2")
        self.TextBox_WhoGoaled2 = QtWidgets.QTextEdit(self.Frame_Team2)
        self.TextBox_WhoGoaled2.setGeometry(QtCore.QRect(10, 10, 151, 31))
        self.TextBox_WhoGoaled2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TextBox_WhoGoaled2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.TextBox_WhoGoaled2.setLineWidth(1)
        self.TextBox_WhoGoaled2.setObjectName("TextBox_WhoGoaled2")
        self.Button_SetTeam1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_SetTeam1.setGeometry(QtCore.QRect(160, 20, 31, 31))
        self.Button_SetTeam1.setObjectName("Button_SetTeam1")
        self.Button_SetTeam2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_SetTeam2.setGeometry(QtCore.QRect(350, 20, 31, 31))
        self.Button_SetTeam2.setObjectName("Button_SetTeam2")
        self.Frame_MatchManage = QtWidgets.QFrame(self.centralwidget)
        self.Frame_MatchManage.setGeometry(QtCore.QRect(400, 60, 361, 171))
        self.Frame_MatchManage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_MatchManage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_MatchManage.setObjectName("Frame_MatchManage")
        self.TimeEdit = QtWidgets.QTimeEdit(self.Frame_MatchManage)
        self.TimeEdit.setGeometry(QtCore.QRect(110, 120, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TimeEdit.setFont(font)
        self.TimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.TimeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.MinuteSection)
        self.TimeEdit.setObjectName("TimeEdit")
        self.Button_SetTime = QtWidgets.QPushButton(self.Frame_MatchManage)
        self.Button_SetTime.setGeometry(QtCore.QRect(10, 120, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Button_SetTime.setFont(font)
        self.Button_SetTime.setObjectName("Button_SetTime")
        self.label = QtWidgets.QLabel(self.Frame_MatchManage)
        self.label.setGeometry(QtCore.QRect(190, 120, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Label_Viewers = QtWidgets.QLabel(self.Frame_MatchManage)
        self.Label_Viewers.setGeometry(QtCore.QRect(260, 120, 101, 41))
        self.Label_Viewers.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Label_Viewers.setObjectName("Label_Viewers")
        self.Button_Pause = QtWidgets.QPushButton(self.Frame_MatchManage)
        self.Button_Pause.setGeometry(QtCore.QRect(190, 70, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Button_Pause.setFont(font)
        self.Button_Pause.setObjectName("Button_Pause")
        self.Button_Start = QtWidgets.QPushButton(self.Frame_MatchManage)
        self.Button_Start.setGeometry(QtCore.QRect(10, 70, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Button_Start.setFont(font)
        self.Button_Start.setObjectName("Button_Start")
        self.Label_Time = QtWidgets.QLabel(self.Frame_MatchManage)
        self.Label_Time.setGeometry(QtCore.QRect(90, 0, 181, 71))
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Label_Time.setFont(font)
        self.Label_Time.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Time.setObjectName("Label_Time")
        self.List_Log = QtWidgets.QListWidget(self.centralwidget)
        self.List_Log.setGeometry(QtCore.QRect(400, 240, 361, 151))
        self.List_Log.setObjectName("List_Log")
        self.Frame_MatchManage.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.TextBox_Team1.raise_()
        self.TextBox_Team2.raise_()
        self.Frame_Team1.raise_()
        self.Frame_Team2.raise_()
        self.Button_SetTeam1.raise_()
        self.Button_SetTeam2.raise_()
        self.List_Log.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Server-Scoreboard"))
        self.Label_Score1.setText(_translate("MainWindow", "0"))
        self.Label_Score2.setText(_translate("MainWindow", "0"))
        self.Button_Goal1.setText(_translate("MainWindow", "Goal!"))
        self.Button_SetScore1.setText(_translate("MainWindow", "Set score"))
        self.Button_Goal2.setText(_translate("MainWindow", "Goal!"))
        self.Button_SetScore2.setText(_translate("MainWindow", "Set score"))
        self.Button_SetTeam1.setText(_translate("MainWindow", "✅"))
        self.Button_SetTeam2.setText(_translate("MainWindow", "✅"))
        self.TimeEdit.setDisplayFormat(_translate("MainWindow", "mm:ss"))
        self.Button_SetTime.setText(_translate("MainWindow", "Set time"))
        self.label.setText(_translate("MainWindow", "Viewers: "))
        self.Label_Viewers.setText(_translate("MainWindow", "0"))
        self.Button_Pause.setText(_translate("MainWindow", "Pause"))
        self.Button_Start.setText(_translate("MainWindow", "Start"))
        self.Label_Time.setText(_translate("MainWindow", "00:00"))
