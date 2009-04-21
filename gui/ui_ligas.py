# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ligas.ui'
#
# Created: Mon Apr 20 18:22:42 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Ligas(object):
    def setupUi(self, Ligas):
        Ligas.setObjectName("Ligas")
        Ligas.resize(800, 550)
        Ligas.setAutoFillBackground(False)
        self.formLayoutWidget = QtGui.QWidget(Ligas)
        self.formLayoutWidget.setGeometry(QtCore.QRect(400, 10, 341, 101))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.dt_fecha_inicio = QtGui.QDateEdit(self.formLayoutWidget)
        self.dt_fecha_inicio.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dt_fecha_inicio.setCalendarPopup(True)
        self.dt_fecha_inicio.setObjectName("dt_fecha_inicio")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.dt_fecha_inicio)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.dt_fecha_final = QtGui.QDateEdit(self.formLayoutWidget)
        self.dt_fecha_final.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dt_fecha_final.setCalendarPopup(True)
        self.dt_fecha_final.setObjectName("dt_fecha_final")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.dt_fecha_final)
        self.btn_agregar = QtGui.QPushButton(Ligas)
        self.btn_agregar.setGeometry(QtCore.QRect(660, 120, 80, 28))
        self.btn_agregar.setObjectName("btn_agregar")
        self.tabla_ligas = QtGui.QTableWidget(Ligas)
        self.tabla_ligas.setGeometry(QtCore.QRect(10, 10, 341, 491))
        self.tabla_ligas.setObjectName("tabla_ligas")
        self.tabla_ligas.setColumnCount(0)
        self.tabla_ligas.setRowCount(0)
        self.widget = QtGui.QWidget(Ligas)
        self.widget.setGeometry(QtCore.QRect(180, 500, 168, 41))
        self.widget.setObjectName("widget")
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_editar = QtGui.QPushButton(self.widget)
        self.btn_editar.setObjectName("btn_editar")
        self.gridLayout.addWidget(self.btn_editar, 0, 0, 1, 1)
        self.btn_eliminar = QtGui.QPushButton(self.widget)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.gridLayout.addWidget(self.btn_eliminar, 0, 1, 1, 1)

        self.retranslateUi(Ligas)
        QtCore.QMetaObject.connectSlotsByName(Ligas)

    def retranslateUi(self, Ligas):
        Ligas.setWindowTitle(QtGui.QApplication.translate("Ligas", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Ligas", "Nombre: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Ligas", "Fecha inicio: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Ligas", "Fecha final:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_agregar.setText(QtGui.QApplication.translate("Ligas", "Añadir", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_editar.setText(QtGui.QApplication.translate("Ligas", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_eliminar.setText(QtGui.QApplication.translate("Ligas", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))

