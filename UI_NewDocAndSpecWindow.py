# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewDocAndSpecWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 320)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 501, 321))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit_Doc_Fio = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_Doc_Fio.setMinimumSize(QtCore.QSize(200, 50))
        self.textEdit_Doc_Fio.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit_Doc_Fio.setFont(font)
        self.textEdit_Doc_Fio.setObjectName("textEdit_Doc_Fio")
        self.gridLayout.addWidget(self.textEdit_Doc_Fio, 3, 1, 1, 1)
        self.textEdit_New_Spec = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_New_Spec.setMinimumSize(QtCore.QSize(200, 50))
        self.textEdit_New_Spec.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit_New_Spec.setFont(font)
        self.textEdit_New_Spec.setObjectName("textEdit_New_Spec")
        self.gridLayout.addWidget(self.textEdit_New_Spec, 5, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 8, 1, 1, 1)
        self.label_Doc_Spec = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Doc_Spec.setMinimumSize(QtCore.QSize(200, 50))
        self.label_Doc_Spec.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_Doc_Spec.setFont(font)
        self.label_Doc_Spec.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Doc_Spec.setObjectName("label_Doc_Spec")
        self.gridLayout.addWidget(self.label_Doc_Spec, 4, 1, 1, 1)
        self.comboBox_Doc_Spec = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_Doc_Spec.setMinimumSize(QtCore.QSize(200, 50))
        self.comboBox_Doc_Spec.setMaximumSize(QtCore.QSize(200, 50))
        self.comboBox_Doc_Spec.setObjectName("comboBox_Doc_Spec")
        self.gridLayout.addWidget(self.comboBox_Doc_Spec, 5, 1, 1, 1)
        self.pushButton_Accept_New_Spec = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_Accept_New_Spec.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_Accept_New_Spec.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_Accept_New_Spec.setFont(font)
        self.pushButton_Accept_New_Spec.setObjectName("pushButton_Accept_New_Spec")
        self.gridLayout.addWidget(self.pushButton_Accept_New_Spec, 6, 2, 1, 1)
        self.pushButton_Accept_New_Doc = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_Accept_New_Doc.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_Accept_New_Doc.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_Accept_New_Doc.setFont(font)
        self.pushButton_Accept_New_Doc.setObjectName("pushButton_Accept_New_Doc")
        self.gridLayout.addWidget(self.pushButton_Accept_New_Doc, 6, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.label_Doc_Fio = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Doc_Fio.setMinimumSize(QtCore.QSize(200, 50))
        self.label_Doc_Fio.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_Doc_Fio.setFont(font)
        self.label_Doc_Fio.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Doc_Fio.setObjectName("label_Doc_Fio")
        self.gridLayout.addWidget(self.label_Doc_Fio, 1, 1, 1, 1)
        self.label_Doc_New_Spec = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Doc_New_Spec.setMinimumSize(QtCore.QSize(200, 50))
        self.label_Doc_New_Spec.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_Doc_New_Spec.setFont(font)
        self.label_Doc_New_Spec.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Doc_New_Spec.setObjectName("label_Doc_New_Spec")
        self.gridLayout.addWidget(self.label_Doc_New_Spec, 4, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_Doc_Spec.setText(_translate("Form", "Выбрать существующую \nспециальность"))
        self.pushButton_Accept_New_Spec.setText(_translate("Form", "Добавить новую \n"
"специальность"))
        self.pushButton_Accept_New_Doc.setText(_translate("Form", "Добавить Врача"))
        self.label_Doc_Fio.setText(_translate("Form", "Введите ФИО врача"))
        self.label_Doc_New_Spec.setText(_translate("Form", "Ввести новую \nспециальность"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
