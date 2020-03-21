# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1054, 862)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(220, 30, 681, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 30, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 810, 111, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.line_code = QtWidgets.QLineEdit(Form)
        self.line_code.setGeometry(QtCore.QRect(110, 650, 91, 31))
        self.line_code.setObjectName("line_code")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(20, 650, 81, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(210, 650, 81, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.line_name = QtWidgets.QLineEdit(Form)
        self.line_name.setGeometry(QtCore.QRect(300, 650, 161, 31))
        self.line_name.setObjectName("line_name")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(930, 30, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox_type = QtWidgets.QComboBox(Form)
        self.comboBox_type.setGeometry(QtCore.QRect(110, 730, 91, 31))
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_3.setGeometry(QtCore.QRect(20, 730, 81, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_4.setGeometry(QtCore.QRect(20, 690, 181, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.line_date = QtWidgets.QLineEdit(Form)
        self.line_date.setGeometry(QtCore.QRect(210, 690, 251, 31))
        self.line_date.setObjectName("line_date")
        self.textBrowser_5 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_5.setGeometry(QtCore.QRect(210, 730, 81, 31))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.comboBox_op_type = QtWidgets.QComboBox(Form)
        self.comboBox_op_type.setGeometry(QtCore.QRect(300, 730, 161, 31))
        self.comboBox_op_type.setObjectName("comboBox_op_type")
        self.comboBox_op_type.addItem("")
        self.comboBox_op_type.addItem("")
        self.textBrowser_6 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_6.setGeometry(QtCore.QRect(210, 770, 131, 31))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.line_vol = QtWidgets.QLineEdit(Form)
        self.line_vol.setGeometry(QtCore.QRect(350, 770, 111, 31))
        self.line_vol.setObjectName("line_vol")
        self.textBrowser_7 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_7.setGeometry(QtCore.QRect(20, 770, 81, 31))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.line_price = QtWidgets.QLineEdit(Form)
        self.line_price.setGeometry(QtCore.QRect(110, 770, 91, 31))
        self.line_price.setObjectName("line_price")
        self.pushButton_createTable = QtWidgets.QPushButton(Form)
        self.pushButton_createTable.setGeometry(QtCore.QRect(120, 80, 93, 28))
        self.pushButton_createTable.setObjectName("pushButton_createTable")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 120, 831, 221))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.pushButton_display = QtWidgets.QPushButton(Form)
        self.pushButton_display.setGeometry(QtCore.QRect(20, 80, 93, 28))
        self.pushButton_display.setObjectName("pushButton_display")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(600, 660, 401, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_10.setGeometry(QtCore.QRect(0, 0, 401, 31))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 40, 111, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_2.setGeometry(QtCore.QRect(120, 40, 281, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_backup = QtWidgets.QPushButton(self.frame)
        self.pushButton_backup.setGeometry(QtCore.QRect(250, 140, 71, 31))
        self.pushButton_backup.setObjectName("pushButton_backup")
        self.pushButton_update = QtWidgets.QPushButton(self.frame)
        self.pushButton_update.setGeometry(QtCore.QRect(0, 140, 161, 31))
        self.pushButton_update.setObjectName("pushButton_update")
        self.pushButton_curPrice = QtWidgets.QPushButton(self.frame)
        self.pushButton_curPrice.setGeometry(QtCore.QRect(170, 140, 71, 31))
        self.pushButton_curPrice.setObjectName("pushButton_curPrice")
        self.line_curPrice = QtWidgets.QLineEdit(self.frame)
        self.line_curPrice.setGeometry(QtCore.QRect(290, 100, 111, 31))
        self.line_curPrice.setObjectName("line_curPrice")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_8.setGeometry(QtCore.QRect(0, 100, 81, 31))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_9.setGeometry(QtCore.QRect(200, 100, 81, 31))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.line_code_price = QtWidgets.QLineEdit(self.frame)
        self.line_code_price.setGeometry(QtCore.QRect(90, 100, 101, 31))
        self.line_code_price.setObjectName("line_code_price")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(220, 350, 61, 31))
        self.toolButton.setObjectName("toolButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 350, 191, 31))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(20, 390, 221, 21))
        self.comboBox.setObjectName("comboBox")
        self.tableWidget_insert = QtWidgets.QTableWidget(Form)
        self.tableWidget_insert.setGeometry(QtCore.QRect(20, 420, 831, 192))
        self.tableWidget_insert.setObjectName("tableWidget_insert")
        self.tableWidget_insert.setColumnCount(7)
        self.tableWidget_insert.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_insert.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_insert.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_insert.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_insert.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_insert.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_insert.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_insert.setHorizontalHeaderItem(6, item)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form._test)
        self.pushButton_2.clicked.connect(self.textEdit.clear)
        self.pushButton_3.clicked.connect(Form.entry)
        self.pushButton_4.clicked.connect(Form.close)
        self.pushButton_createTable.clicked.connect(Form._init_db)
        self.pushButton_display.clicked.connect(Form.show_hold)
        self.pushButton_curPrice.clicked.connect(Form.update_price)
        self.pushButton_update.clicked.connect(Form.update_hold)
        self.pushButton_5.clicked.connect(Form.update_ready)
        self.pushButton_backup.clicked.connect(Form.backup_price)
        self.toolButton.clicked.connect(Form.get_files)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "响应测试"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">我的交易系统</p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "清空"))
        self.pushButton_3.setText(_translate("Form", "交易记录输入"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">证券代码</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">证券名称</span></p></body></html>"))
        self.pushButton_4.setText(_translate("Form", "关闭窗口"))
        self.comboBox_type.setItemText(0, _translate("Form", "可转债"))
        self.comboBox_type.setItemText(1, _translate("Form", "国债"))
        self.comboBox_type.setItemText(2, _translate("Form", "企业债"))
        self.comboBox_type.setItemText(3, _translate("Form", "金融债"))
        self.comboBox_type.setItemText(4, _translate("Form", "逆回购"))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">证券类型</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">交易日期（yyyy-mm-dd)</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">操作类型</span></p></body></html>"))
        self.comboBox_op_type.setItemText(0, _translate("Form", "买入"))
        self.comboBox_op_type.setItemText(1, _translate("Form", "卖出"))
        self.textBrowser_6.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">交易数量（手）</span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">交易价格</span></p></body></html>"))
        self.pushButton_createTable.setText(_translate("Form", "创建表"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "code"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "type"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "hold_vol"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "hold_cost"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "cur_date"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "cur_price"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "lst_trade_day"))
        self.pushButton_display.setText(_translate("Form", "当前持仓"))
        self.textBrowser_10.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">备用功能区：价格输入（当清算所无估值可用时）</span></p></body></html>"))
        self.pushButton_5.setText(_translate("Form", "更新持仓"))
        self.textEdit_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Ready?</span></p></body></html>"))
        self.pushButton_backup.setText(_translate("Form", "备份"))
        self.pushButton_update.setText(_translate("Form", "最新价格及持仓"))
        self.pushButton_curPrice.setText(_translate("Form", "录入"))
        self.textBrowser_8.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">证券代码</span></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">最新价格</span></p></body></html>"))
        self.toolButton.setText(_translate("Form", "选择路径"))
        self.label.setText(_translate("Form", "TextLabel"))
        item = self.tableWidget_insert.horizontalHeaderItem(0)
        item.setText(_translate("Form", "code"))
        item = self.tableWidget_insert.horizontalHeaderItem(1)
        item.setText(_translate("Form", "name"))
        item = self.tableWidget_insert.horizontalHeaderItem(2)
        item.setText(_translate("Form", "type"))
        item = self.tableWidget_insert.horizontalHeaderItem(3)
        item.setText(_translate("Form", "op_date"))
        item = self.tableWidget_insert.horizontalHeaderItem(4)
        item.setText(_translate("Form", "op_type"))
        item = self.tableWidget_insert.horizontalHeaderItem(5)
        item.setText(_translate("Form", "vol"))
        item = self.tableWidget_insert.horizontalHeaderItem(6)
        item.setText(_translate("Form", "price"))
