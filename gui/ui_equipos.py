# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/equipos.ui'
#
# Created: Mon Apr 20 23:22:37 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Equipos(object):
    def setupUi(self, Equipos):
        Equipos.setObjectName("Equipos")
        Equipos.resize(800, 550)
        self.formLayoutWidget = QtGui.QWidget(Equipos)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 0, 271, 41))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.comboBox = QtGui.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.tabla_equipos = QtGui.QTableWidget(Equipos)
        self.tabla_equipos.setGeometry(QtCore.QRect(10, 40, 531, 501))
        self.tabla_equipos.setObjectName("tabla_equipos")
        self.tabla_equipos.setColumnCount(0)
        self.tabla_equipos.setRowCount(0)
        self.formLayoutWidget_2 = QtGui.QWidget(Equipos)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(540, 40, 251, 71))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.comboBox_2 = QtGui.QComboBox(self.formLayoutWidget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox_2)
        self.pushButton = QtGui.QPushButton(Equipos)
        self.pushButton.setGeometry(QtCore.QRect(700, 120, 80, 28))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtGui.QWidget(Equipos)
        self.layoutWidget.setGeometry(QtCore.QRect(551, 454, 101, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.retranslateUi(Equipos)
        QtCore.QMetaObject.connectSlotsByName(Equipos)

    def retranslateUi(self, Equipos):
        Equipos.setWindowTitle(QtGui.QApplication.translate("Equipos", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Equipos", "Liga: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Equipos", "Nombre: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Equipos", "Grupo: ", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Equipos", "Añadir", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Equipos", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Equipos", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))

