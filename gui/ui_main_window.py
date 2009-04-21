# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/main_window.ui'
#
# Created: Mon Apr 20 23:12:29 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        self.menuLigas = QtGui.QMenu(self.menubar)
        self.menuLigas.setObjectName("menuLigas")
        self.menuEquipos = QtGui.QMenu(self.menubar)
        self.menuEquipos.setObjectName("menuEquipos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.nueva_jornada = QtGui.QAction(MainWindow)
        self.nueva_jornada.setObjectName("nueva_jornada")
        self.menu_admin_ligas = QtGui.QAction(MainWindow)
        self.menu_admin_ligas.setObjectName("menu_admin_ligas")
        self.menu_admin_jugadores = QtGui.QAction(MainWindow)
        self.menu_admin_jugadores.setObjectName("menu_admin_jugadores")
        self.menu_admin_equipos = QtGui.QAction(MainWindow)
        self.menu_admin_equipos.setObjectName("menu_admin_equipos")
        self.menuLigas.addAction(self.nueva_jornada)
        self.menuEquipos.addAction(self.menu_admin_ligas)
        self.menuEquipos.addAction(self.menu_admin_equipos)
        self.menuEquipos.addAction(self.menu_admin_jugadores)
        self.menubar.addAction(self.menuLigas.menuAction())
        self.menubar.addAction(self.menuEquipos.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Administrar Ligas", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLigas.setTitle(QtGui.QApplication.translate("MainWindow", "&Estadisticas", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEquipos.setTitle(QtGui.QApplication.translate("MainWindow", "&Administrar", None, QtGui.QApplication.UnicodeUTF8))
        self.nueva_jornada.setText(QtGui.QApplication.translate("MainWindow", "Nueva Jornada", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_admin_ligas.setText(QtGui.QApplication.translate("MainWindow", "Ligas", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_admin_jugadores.setText(QtGui.QApplication.translate("MainWindow", "Jugadores", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_admin_equipos.setText(QtGui.QApplication.translate("MainWindow", "Equipos", None, QtGui.QApplication.UnicodeUTF8))

