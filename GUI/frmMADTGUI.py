# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmMADTGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmMADT(object):
    def setupUi(self, frmMADT):
        frmMADT.setObjectName("frmMADT")
        frmMADT.resize(782, 764)
        self.btnInFile = QtWidgets.QPushButton(frmMADT)
        self.btnInFile.setGeometry(QtCore.QRect(710, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.label_33 = QtWidgets.QLabel(frmMADT)
        self.label_33.setGeometry(QtCore.QRect(30, 20, 161, 16))
        self.label_33.setObjectName("label_33")
        self.btnOutFile = QtWidgets.QPushButton(frmMADT)
        self.btnOutFile.setGeometry(QtCore.QRect(710, 60, 51, 32))
        self.btnOutFile.setObjectName("btnOutFile")
        self.txtInFile = QtWidgets.QLineEdit(frmMADT)
        self.txtInFile.setGeometry(QtCore.QRect(200, 20, 501, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.btnConvert = QtWidgets.QPushButton(frmMADT)
        self.btnConvert.setGeometry(QtCore.QRect(620, 715, 141, 32))
        self.btnConvert.setObjectName("btnConvert")
        self.label_35 = QtWidgets.QLabel(frmMADT)
        self.label_35.setGeometry(QtCore.QRect(30, 60, 161, 16))
        self.label_35.setObjectName("label_35")
        self.txtOutFile = QtWidgets.QLineEdit(frmMADT)
        self.txtOutFile.setGeometry(QtCore.QRect(200, 60, 501, 21))
        self.txtOutFile.setText("")
        self.txtOutFile.setObjectName("txtOutFile")
        self.btnClose = QtWidgets.QPushButton(frmMADT)
        self.btnClose.setGeometry(QtCore.QRect(30, 715, 141, 32))
        self.btnClose.setObjectName("btnClose")
        self.tabWidget = QtWidgets.QTabWidget(frmMADT)
        self.tabWidget.setGeometry(QtCore.QRect(30, 150, 731, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 60, 16))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(360, 10, 61, 16))
        self.label.setObjectName("label")
        self.txtITrLabel = QtWidgets.QComboBox(self.tab)
        self.txtITrLabel.setGeometry(QtCore.QRect(240, 110, 121, 26))
        self.txtITrLabel.setEditable(True)
        self.txtITrLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtITrLabel.setObjectName("txtITrLabel")
        self.txtITrData = QtWidgets.QComboBox(self.tab)
        self.txtITrData.setGeometry(QtCore.QRect(240, 70, 121, 26))
        self.txtITrData.setEditable(True)
        self.txtITrData.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtITrData.setObjectName("txtITrData")
        self.txtITeLabel = QtWidgets.QComboBox(self.tab)
        self.txtITeLabel.setGeometry(QtCore.QRect(390, 110, 121, 26))
        self.txtITeLabel.setEditable(True)
        self.txtITeLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtITeLabel.setObjectName("txtITeLabel")
        self.txtITeData = QtWidgets.QComboBox(self.tab)
        self.txtITeData.setGeometry(QtCore.QRect(390, 70, 121, 26))
        self.txtITeData.setEditable(True)
        self.txtITeData.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtITeData.setObjectName("txtITeData")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(285, 40, 81, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(430, 40, 81, 16))
        self.label_8.setObjectName("label_8")
        self.txtFoldID = QtWidgets.QComboBox(self.tab)
        self.txtFoldID.setGeometry(QtCore.QRect(240, 150, 121, 26))
        self.txtFoldID.setEditable(True)
        self.txtFoldID.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtFoldID.setObjectName("txtFoldID")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(20, 150, 121, 16))
        self.label_9.setObjectName("label_9")
        self.lbFoldID = QtWidgets.QLabel(self.tab)
        self.lbFoldID.setGeometry(QtCore.QRect(390, 150, 251, 16))
        self.lbFoldID.setObjectName("lbFoldID")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 671, 80))
        self.groupBox.setObjectName("groupBox")
        self.cbScale = QtWidgets.QCheckBox(self.groupBox)
        self.cbScale.setGeometry(QtCore.QRect(20, 40, 641, 21))
        self.cbScale.setChecked(True)
        self.cbScale.setObjectName("cbScale")
        self.txtMinSamplesSplit = QtWidgets.QLineEdit(self.tab_2)
        self.txtMinSamplesSplit.setGeometry(QtCore.QRect(260, 240, 160, 21))
        self.txtMinSamplesSplit.setObjectName("txtMinSamplesSplit")
        self.txtMaxLeafNodes = QtWidgets.QLineEdit(self.tab_2)
        self.txtMaxLeafNodes.setGeometry(QtCore.QRect(260, 400, 160, 21))
        self.txtMaxLeafNodes.setObjectName("txtMaxLeafNodes")
        self.txtMaxFeatures = QtWidgets.QLineEdit(self.tab_2)
        self.txtMaxFeatures.setGeometry(QtCore.QRect(550, 360, 160, 21))
        self.txtMaxFeatures.setText("")
        self.txtMaxFeatures.setObjectName("txtMaxFeatures")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(30, 360, 221, 16))
        self.label_14.setObjectName("label_14")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(30, 320, 231, 16))
        self.label_18.setObjectName("label_18")
        self.cbSplitter = QtWidgets.QComboBox(self.tab_2)
        self.cbSplitter.setGeometry(QtCore.QRect(260, 160, 161, 26))
        self.cbSplitter.setObjectName("cbSplitter")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(30, 240, 221, 16))
        self.label_11.setObjectName("label_11")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(30, 280, 231, 16))
        self.label_15.setObjectName("label_15")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(30, 160, 231, 16))
        self.label_13.setObjectName("label_13")
        self.txtMinWeightFractionLeaf = QtWidgets.QLineEdit(self.tab_2)
        self.txtMinWeightFractionLeaf.setGeometry(QtCore.QRect(260, 320, 160, 21))
        self.txtMinWeightFractionLeaf.setObjectName("txtMinWeightFractionLeaf")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(30, 400, 251, 16))
        self.label_16.setObjectName("label_16")
        self.txtMinSamplesLeaf = QtWidgets.QLineEdit(self.tab_2)
        self.txtMinSamplesLeaf.setGeometry(QtCore.QRect(260, 280, 160, 21))
        self.txtMinSamplesLeaf.setObjectName("txtMinSamplesLeaf")
        self.cbCriterion = QtWidgets.QComboBox(self.tab_2)
        self.cbCriterion.setGeometry(QtCore.QRect(260, 120, 161, 26))
        self.cbCriterion.setObjectName("cbCriterion")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(30, 120, 231, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(30, 200, 221, 16))
        self.label_20.setObjectName("label_20")
        self.txtMaxDepth = QtWidgets.QLineEdit(self.tab_2)
        self.txtMaxDepth.setGeometry(QtCore.QRect(260, 200, 160, 21))
        self.txtMaxDepth.setObjectName("txtMaxDepth")
        self.cbPresort = QtWidgets.QCheckBox(self.tab_2)
        self.cbPresort.setGeometry(QtCore.QRect(500, 120, 201, 20))
        self.cbPresort.setChecked(False)
        self.cbPresort.setObjectName("cbPresort")
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setGeometry(QtCore.QRect(30, 440, 251, 16))
        self.label_21.setObjectName("label_21")
        self.txtMinImpurityDecrease = QtWidgets.QLineEdit(self.tab_2)
        self.txtMinImpurityDecrease.setGeometry(QtCore.QRect(260, 440, 160, 21))
        self.txtMinImpurityDecrease.setObjectName("txtMinImpurityDecrease")
        self.txtMinImpuritySplit = QtWidgets.QLineEdit(self.tab_2)
        self.txtMinImpuritySplit.setGeometry(QtCore.QRect(260, 480, 160, 21))
        self.txtMinImpuritySplit.setObjectName("txtMinImpuritySplit")
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setGeometry(QtCore.QRect(30, 480, 251, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setGeometry(QtCore.QRect(450, 360, 221, 16))
        self.label_23.setObjectName("label_23")
        self.cbMaxFeatures = QtWidgets.QComboBox(self.tab_2)
        self.cbMaxFeatures.setGeometry(QtCore.QRect(260, 360, 161, 26))
        self.cbMaxFeatures.setObjectName("cbMaxFeatures")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.txtFoldFrom = QtWidgets.QSpinBox(self.tab_3)
        self.txtFoldFrom.setGeometry(QtCore.QRect(100, 30, 80, 24))
        self.txtFoldFrom.setMaximum(100000)
        self.txtFoldFrom.setProperty("value", 1)
        self.txtFoldFrom.setObjectName("txtFoldFrom")
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(40, 30, 60, 16))
        self.label_17.setObjectName("label_17")
        self.txtFoldTo = QtWidgets.QSpinBox(self.tab_3)
        self.txtFoldTo.setGeometry(QtCore.QRect(270, 30, 80, 24))
        self.txtFoldTo.setMaximum(100000)
        self.txtFoldTo.setProperty("value", 1)
        self.txtFoldTo.setObjectName("txtFoldTo")
        self.label_44 = QtWidgets.QLabel(self.tab_3)
        self.label_44.setGeometry(QtCore.QRect(210, 30, 60, 16))
        self.label_44.setObjectName("label_44")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 201, 16))
        self.label_4.setObjectName("label_4")
        self.txtFilter = QtWidgets.QLineEdit(self.tab_4)
        self.txtFilter.setGeometry(QtCore.QRect(190, 30, 291, 21))
        self.txtFilter.setObjectName("txtFilter")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(490, 30, 211, 16))
        self.label_5.setObjectName("label_5")
        self.txtClass = QtWidgets.QTextEdit(self.tab_4)
        self.txtClass.setGeometry(QtCore.QRect(190, 70, 91, 431))
        self.txtClass.setReadOnly(True)
        self.txtClass.setObjectName("txtClass")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(20, 70, 201, 16))
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.cbAverage = QtWidgets.QCheckBox(self.tab_5)
        self.cbAverage.setGeometry(QtCore.QRect(20, 30, 181, 20))
        self.cbAverage.setChecked(True)
        self.cbAverage.setObjectName("cbAverage")
        self.cbPrecision = QtWidgets.QCheckBox(self.tab_5)
        self.cbPrecision.setGeometry(QtCore.QRect(20, 70, 181, 20))
        self.cbPrecision.setChecked(True)
        self.cbPrecision.setObjectName("cbPrecision")
        self.cbPrecisionAvg = QtWidgets.QComboBox(self.tab_5)
        self.cbPrecisionAvg.setGeometry(QtCore.QRect(240, 70, 321, 26))
        self.cbPrecisionAvg.setObjectName("cbPrecisionAvg")
        self.cbAPrecisionAvg = QtWidgets.QComboBox(self.tab_5)
        self.cbAPrecisionAvg.setGeometry(QtCore.QRect(240, 110, 321, 26))
        self.cbAPrecisionAvg.setObjectName("cbAPrecisionAvg")
        self.cbAPrecision = QtWidgets.QCheckBox(self.tab_5)
        self.cbAPrecision.setGeometry(QtCore.QRect(20, 110, 231, 20))
        self.cbAPrecision.setChecked(False)
        self.cbAPrecision.setObjectName("cbAPrecision")
        self.cbRecallAvg = QtWidgets.QComboBox(self.tab_5)
        self.cbRecallAvg.setGeometry(QtCore.QRect(240, 150, 321, 26))
        self.cbRecallAvg.setObjectName("cbRecallAvg")
        self.cbRecall = QtWidgets.QCheckBox(self.tab_5)
        self.cbRecall.setGeometry(QtCore.QRect(20, 150, 181, 20))
        self.cbRecall.setChecked(True)
        self.cbRecall.setObjectName("cbRecall")
        self.cbF1 = QtWidgets.QCheckBox(self.tab_5)
        self.cbF1.setGeometry(QtCore.QRect(20, 190, 181, 20))
        self.cbF1.setChecked(True)
        self.cbF1.setObjectName("cbF1")
        self.cbF1Avg = QtWidgets.QComboBox(self.tab_5)
        self.cbF1Avg.setGeometry(QtCore.QRect(240, 190, 321, 26))
        self.cbF1Avg.setObjectName("cbF1Avg")
        self.tabWidget.addTab(self.tab_5, "")
        self.label_12 = QtWidgets.QLabel(frmMADT)
        self.label_12.setGeometry(QtCore.QRect(185, 720, 421, 20))
        self.label_12.setObjectName("label_12")
        self.btnOutModel = QtWidgets.QPushButton(frmMADT)
        self.btnOutModel.setGeometry(QtCore.QRect(710, 100, 51, 32))
        self.btnOutModel.setObjectName("btnOutModel")
        self.label_36 = QtWidgets.QLabel(frmMADT)
        self.label_36.setGeometry(QtCore.QRect(30, 100, 171, 16))
        self.label_36.setObjectName("label_36")
        self.txtOutModel = QtWidgets.QLineEdit(frmMADT)
        self.txtOutModel.setGeometry(QtCore.QRect(200, 100, 501, 21))
        self.txtOutModel.setText("")
        self.txtOutModel.setObjectName("txtOutModel")

        self.retranslateUi(frmMADT)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmMADT)
        frmMADT.setTabOrder(self.txtInFile, self.btnInFile)
        frmMADT.setTabOrder(self.btnInFile, self.txtOutFile)
        frmMADT.setTabOrder(self.txtOutFile, self.btnOutFile)
        frmMADT.setTabOrder(self.btnOutFile, self.tabWidget)
        frmMADT.setTabOrder(self.tabWidget, self.txtITrData)
        frmMADT.setTabOrder(self.txtITrData, self.txtITrLabel)
        frmMADT.setTabOrder(self.txtITrLabel, self.btnConvert)
        frmMADT.setTabOrder(self.btnConvert, self.btnClose)

    def retranslateUi(self, frmMADT):
        _translate = QtCore.QCoreApplication.translate
        frmMADT.setWindowTitle(_translate("frmMADT", "Decision Tree Classifier"))
        self.btnInFile.setText(_translate("frmMADT", "..."))
        self.label_33.setText(_translate("frmMADT", "Input Data (per fold)"))
        self.btnOutFile.setText(_translate("frmMADT", "..."))
        self.btnConvert.setText(_translate("frmMADT", "Analyze"))
        self.label_35.setText(_translate("frmMADT", "Analysis"))
        self.btnClose.setText(_translate("frmMADT", "Close"))
        self.label_2.setText(_translate("frmMADT", "Data"))
        self.label_3.setText(_translate("frmMADT", "Label"))
        self.label.setText(_translate("frmMADT", "Input"))
        self.label_7.setText(_translate("frmMADT", "Train"))
        self.label_8.setText(_translate("frmMADT", "Test"))
        self.label_9.setText(_translate("frmMADT", "FoldID"))
        self.lbFoldID.setText(_translate("frmMADT", "ID=None"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmMADT", "Data"))
        self.groupBox.setTitle(_translate("frmMADT", "<Input Data Normalization>"))
        self.cbScale.setText(_translate("frmMADT", "Scale Data Train~N(0,1) and Test~N(0,1)"))
        self.txtMinSamplesSplit.setText(_translate("frmMADT", "2"))
        self.txtMaxLeafNodes.setText(_translate("frmMADT", "0"))
        self.label_14.setText(_translate("frmMADT", "Max Features"))
        self.label_18.setText(_translate("frmMADT", "Min Weight Fraction Leaf "))
        self.label_11.setText(_translate("frmMADT", "Min Samples Split "))
        self.label_15.setText(_translate("frmMADT", "Min Samples Leaf"))
        self.label_13.setText(_translate("frmMADT", "Splitter"))
        self.txtMinWeightFractionLeaf.setText(_translate("frmMADT", "0"))
        self.label_16.setText(_translate("frmMADT", "Max Leaf Nodes (None=0)"))
        self.txtMinSamplesLeaf.setText(_translate("frmMADT", "1"))
        self.label_19.setText(_translate("frmMADT", "Criterion"))
        self.label_20.setText(_translate("frmMADT", "Max Depth (None=0)"))
        self.txtMaxDepth.setText(_translate("frmMADT", "0"))
        self.cbPresort.setText(_translate("frmMADT", "Presort"))
        self.label_21.setText(_translate("frmMADT", "Min Impurity Decrease"))
        self.txtMinImpurityDecrease.setText(_translate("frmMADT", "0"))
        self.txtMinImpuritySplit.setText(_translate("frmMADT", "0"))
        self.label_22.setText(_translate("frmMADT", "Min Impurity Split (None=0)"))
        self.label_23.setText(_translate("frmMADT", "Value"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmMADT", "Parameters"))
        self.label_17.setText(_translate("frmMADT", "From:"))
        self.label_44.setText(_translate("frmMADT", "To:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("frmMADT", "Fold"))
        self.label_4.setText(_translate("frmMADT", "Remove Class IDs"))
        self.txtFilter.setText(_translate("frmMADT", "0"))
        self.label_5.setText(_translate("frmMADT", "e.g. 0 or [1,2]"))
        self.label_10.setText(_translate("frmMADT", "Existed Classes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("frmMADT", "Filter Class ID"))
        self.cbAverage.setText(_translate("frmMADT", "Average"))
        self.cbPrecision.setText(_translate("frmMADT", "Precision"))
        self.cbAPrecision.setText(_translate("frmMADT", "Average of Precision"))
        self.cbRecall.setText(_translate("frmMADT", "Recall"))
        self.cbF1.setText(_translate("frmMADT", "f1 score"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("frmMADT", "Metrics"))
        self.label_12.setText(_translate("frmMADT", "$FOLD$ will be replaced by fold number."))
        self.btnOutModel.setText(_translate("frmMADT", "..."))
        self.label_36.setText(_translate("frmMADT", "Models (per fold)"))

