# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmRenameFileGUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmRenameFile(object):
    def setupUi(self, frmRenameFile):
        frmRenameFile.setObjectName("frmRenameFile")
        frmRenameFile.resize(663, 623)
        self.groupBox_3 = QtWidgets.QGroupBox(frmRenameFile)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 98, 621, 80))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(300, 35, 60, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(480, 35, 60, 16))
        self.label_10.setObjectName("label_10")
        self.txtRunPer = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtRunPer.setGeometry(QtCore.QRect(530, 35, 80, 21))
        self.txtRunPer.setObjectName("txtRunPer")
        self.txtRunLen = QtWidgets.QSpinBox(self.groupBox_3)
        self.txtRunLen.setGeometry(QtCore.QRect(370, 35, 80, 24))
        self.txtRunLen.setMaximum(100000)
        self.txtRunLen.setProperty("value", 2)
        self.txtRunLen.setObjectName("txtRunLen")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(15, 35, 71, 16))
        self.label_8.setObjectName("label_8")
        self.txtRunRange = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtRunRange.setGeometry(QtCore.QRect(80, 35, 201, 21))
        self.txtRunRange.setObjectName("txtRunRange")
        self.groupBox = QtWidgets.QGroupBox(frmRenameFile)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 621, 80))
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(300, 35, 60, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(480, 35, 60, 16))
        self.label_4.setObjectName("label_4")
        self.txtSubPer = QtWidgets.QLineEdit(self.groupBox)
        self.txtSubPer.setGeometry(QtCore.QRect(530, 35, 80, 21))
        self.txtSubPer.setObjectName("txtSubPer")
        self.txtSubLen = QtWidgets.QSpinBox(self.groupBox)
        self.txtSubLen.setGeometry(QtCore.QRect(370, 35, 80, 24))
        self.txtSubLen.setMaximum(100000)
        self.txtSubLen.setSingleStep(1)
        self.txtSubLen.setProperty("value", 2)
        self.txtSubLen.setObjectName("txtSubLen")
        self.txtSubRange = QtWidgets.QLineEdit(self.groupBox)
        self.txtSubRange.setGeometry(QtCore.QRect(74, 35, 211, 21))
        self.txtSubRange.setObjectName("txtSubRange")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(14, 35, 71, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox_4 = QtWidgets.QGroupBox(frmRenameFile)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 273, 621, 111))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(11, 69, 81, 16))
        self.label_5.setObjectName("label_5")
        self.txtTask = QtWidgets.QLineEdit(self.groupBox_4)
        self.txtTask.setGeometry(QtCore.QRect(100, 70, 501, 21))
        self.txtTask.setText("")
        self.txtTask.setObjectName("txtTask")
        self.btnDIR = QtWidgets.QPushButton(self.groupBox_4)
        self.btnDIR.setGeometry(QtCore.QRect(559, 26, 51, 32))
        self.btnDIR.setObjectName("btnDIR")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(10, 31, 111, 16))
        self.label.setToolTip("")
        self.label.setToolTipDuration(-1)
        self.label.setStatusTip("")
        self.label.setObjectName("label")
        self.txtDIR = QtWidgets.QLineEdit(self.groupBox_4)
        self.txtDIR.setGeometry(QtCore.QRect(118, 31, 431, 21))
        self.txtDIR.setToolTip("")
        self.txtDIR.setToolTipDuration(-1)
        self.txtDIR.setStatusTip("")
        self.txtDIR.setText("")
        self.txtDIR.setObjectName("txtDIR")
        self.groupBox_2 = QtWidgets.QGroupBox(frmRenameFile)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 185, 621, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.txtConPer = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtConPer.setGeometry(QtCore.QRect(530, 35, 80, 21))
        self.txtConPer.setObjectName("txtConPer")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(480, 35, 60, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(300, 35, 60, 21))
        self.label_12.setObjectName("label_12")
        self.txtConLen = QtWidgets.QSpinBox(self.groupBox_2)
        self.txtConLen.setGeometry(QtCore.QRect(370, 35, 80, 24))
        self.txtConLen.setMaximum(100000)
        self.txtConLen.setSingleStep(1)
        self.txtConLen.setProperty("value", 2)
        self.txtConLen.setObjectName("txtConLen")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(20, 35, 61, 16))
        self.label_7.setObjectName("label_7")
        self.txtConRange = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtConRange.setGeometry(QtCore.QRect(80, 35, 201, 21))
        self.txtConRange.setObjectName("txtConRange")
        self.groupBox_5 = QtWidgets.QGroupBox(frmRenameFile)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 390, 621, 111))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_16 = QtWidgets.QLabel(self.groupBox_5)
        self.label_16.setGeometry(QtCore.QRect(11, 69, 81, 16))
        self.label_16.setObjectName("label_16")
        self.txtOutput = QtWidgets.QLineEdit(self.groupBox_5)
        self.txtOutput.setGeometry(QtCore.QRect(100, 70, 500, 21))
        self.txtOutput.setText("")
        self.txtOutput.setObjectName("txtOutput")
        self.label_17 = QtWidgets.QLabel(self.groupBox_5)
        self.label_17.setGeometry(QtCore.QRect(10, 31, 111, 16))
        self.label_17.setToolTip("")
        self.label_17.setToolTipDuration(-1)
        self.label_17.setStatusTip("")
        self.label_17.setObjectName("label_17")
        self.txtInput = QtWidgets.QLineEdit(self.groupBox_5)
        self.txtInput.setGeometry(QtCore.QRect(100, 31, 500, 21))
        self.txtInput.setToolTip("")
        self.txtInput.setToolTipDuration(-1)
        self.txtInput.setStatusTip("")
        self.txtInput.setText("")
        self.txtInput.setObjectName("txtInput")
        self.btnExit = QtWidgets.QPushButton(frmRenameFile)
        self.btnExit.setGeometry(QtCore.QRect(530, 520, 113, 32))
        self.btnExit.setObjectName("btnExit")
        self.btnRun = QtWidgets.QPushButton(frmRenameFile)
        self.btnRun.setGeometry(QtCore.QRect(20, 520, 113, 32))
        self.btnRun.setObjectName("btnRun")
        self.label_23 = QtWidgets.QLabel(frmRenameFile)
        self.label_23.setGeometry(QtCore.QRect(20, 560, 631, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_23.setObjectName("label_23")

        self.retranslateUi(frmRenameFile)
        QtCore.QMetaObject.connectSlotsByName(frmRenameFile)
        frmRenameFile.setTabOrder(self.txtSubLen, self.txtSubPer)
        frmRenameFile.setTabOrder(self.txtSubPer, self.txtRunLen)
        frmRenameFile.setTabOrder(self.txtRunLen, self.txtRunPer)
        frmRenameFile.setTabOrder(self.txtRunPer, self.txtConLen)
        frmRenameFile.setTabOrder(self.txtConLen, self.txtConPer)
        frmRenameFile.setTabOrder(self.txtConPer, self.txtDIR)
        frmRenameFile.setTabOrder(self.txtDIR, self.btnDIR)
        frmRenameFile.setTabOrder(self.btnDIR, self.txtTask)
        frmRenameFile.setTabOrder(self.txtTask, self.txtInput)
        frmRenameFile.setTabOrder(self.txtInput, self.txtOutput)
        frmRenameFile.setTabOrder(self.txtOutput, self.btnExit)
        frmRenameFile.setTabOrder(self.btnExit, self.btnRun)

    def retranslateUi(self, frmRenameFile):
        _translate = QtCore.QCoreApplication.translate
        frmRenameFile.setWindowTitle(_translate("frmRenameFile", "Group Rename Files"))
        self.groupBox_3.setTitle(_translate("frmRenameFile", "<Runs>"))
        self.label_9.setText(_translate("frmRenameFile", "Length:"))
        self.label_10.setText(_translate("frmRenameFile", "Perfix:"))
        self.txtRunPer.setText(_translate("frmRenameFile", "0"))
        self.label_8.setText(_translate("frmRenameFile", "Ranges:"))
        self.txtRunRange.setToolTip(_translate("frmRenameFile", "<html><head/><body><p><span style=\" font-size:18pt; color:#0000ff;\">RunRange: sequence of ranges, i.e. If all 12 subjects have runs from 2 to 5 then Range=[12*2-5]; If 3 subjects have runs from 1 to 4 and 2 subjects have runs from 5 to 7 then Range=[3*1-4, 2*5-7]</span></p></body></html>"))
        self.txtRunRange.setText(_translate("frmRenameFile", "[1*1-1]"))
        self.groupBox.setTitle(_translate("frmRenameFile", "<Subjects>"))
        self.label_3.setText(_translate("frmRenameFile", "Length:"))
        self.label_4.setText(_translate("frmRenameFile", "Perfix:"))
        self.txtSubPer.setText(_translate("frmRenameFile", "0"))
        self.txtSubRange.setToolTip(_translate("frmRenameFile", "<html><head/><body><p><span style=\" font-size:18pt; color:#0000ff;\">SubRange: a unique range of integers, i.e. Range=[1, 4-8, 10, 12-14]</span></p></body></html>"))
        self.txtSubRange.setText(_translate("frmRenameFile", "[1-1]"))
        self.label_2.setText(_translate("frmRenameFile", "Range:"))
        self.groupBox_4.setTitle(_translate("frmRenameFile", "<General>"))
        self.label_5.setText(_translate("frmRenameFile", "Task Name:"))
        self.btnDIR.setText(_translate("frmRenameFile", "..."))
        self.label.setText(_translate("frmRenameFile", "Main Directory:"))
        self.label.setProperty("setToolTip", _translate("frmRenameFile", "Please enter the main directory of the fMRI dataset. Format of directory must be based on BIDS structure."))
        self.groupBox_2.setTitle(_translate("frmRenameFile", "<Counter>"))
        self.txtConPer.setText(_translate("frmRenameFile", "0"))
        self.label_11.setText(_translate("frmRenameFile", "Perfix:"))
        self.label_12.setText(_translate("frmRenameFile", "Length:"))
        self.label_7.setText(_translate("frmRenameFile", "Ranges:"))
        self.txtConRange.setToolTip(_translate("frmRenameFile", "<html><head/><body><p><span style=\" font-size:18pt; color:#0000ff;\">CounterRange: sequence of ranges, i.e. If all 12 subjects have runs from 2 to 5 then Range=[12*2-5]; If 3 subjects have runs from 1 to 4 and 2 subjects have runs from 5 to 7 then Range=[3*1-4, 2*5-7]</span></p></body></html>"))
        self.txtConRange.setText(_translate("frmRenameFile", "[1*1-1]"))
        self.groupBox_5.setTitle(_translate("frmRenameFile", "<File Structures>"))
        self.label_16.setText(_translate("frmRenameFile", "Output Files:"))
        self.label_17.setText(_translate("frmRenameFile", "Input Files:"))
        self.label_17.setProperty("setToolTip", _translate("frmRenameFile", "Please enter the main directory of the fMRI dataset. Format of directory must be based on BIDS structure."))
        self.btnExit.setText(_translate("frmRenameFile", "Exit"))
        self.btnRun.setText(_translate("frmRenameFile", "Run"))
        self.label_23.setText(_translate("frmRenameFile", "$MAINDIR$, $SUB$, $TASK$, $RUN$, $COUNT$ will be replaced by\n"
"the preprocessing parameters. It\'s case sensitive."))

