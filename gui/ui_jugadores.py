# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/jugadores.ui'
#
# Created: Mon Apr 20 23:16:06 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Jugadores(object):
    def setupUi(self, Jugadores):
        Jugadores.setObjectName("Jugadores")
        Jugadores.resize(800, 550)
        self.gridLayoutWidget = QtGui.QWidget(Jugadores)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 401, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 0, 4, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.tabla_jugadores = QtGui.QTableWidget(Jugadores)
        self.tabla_jugadores.setGeometry(QtCore.QRect(10, 50, 501, 461))
        self.tabla_jugadores.setObjectName("tabla_jugadores")
        self.tabla_jugadores.setColumnCount(0)
        self.tabla_jugadores.setRowCount(0)
        self.formLayoutWidget = QtGui.QWidget(Jugadores)
        self.formLayoutWidget.setGeometry(QtCore.QRect(510, 50, 281, 41))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.pushButton_3 = QtGui.QPushButton(Jugadores)
        self.pushButton_3.setGeometry(QtCore.QRect(700, 100, 80, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.layoutWidget = QtGui.QWidget(Jugadores)
        self.layoutWidget.setGeometry(QtCore.QRect(330, 510, 178, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.retranslateUi(Jugadores)
        QtCore.QMetaObject.connectSlotsByName(Jugadores)

    def retranslateUi(self, Jugadores):
        Jugadores.setWindowTitle(QtGui.QApplication.translate("Jugadores", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Jugadores", "Liga: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Jugadores", "Equipo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Jugadores", "Nombre: ", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Jugadores", "Añadir", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Jugadores", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Jugadores", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))

