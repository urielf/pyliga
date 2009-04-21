# -*- coding: UTF-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gui.ui_main_window import Ui_MainWindow
from ligas import Ligas
from equipos import Equipos
from jugadores import Jugadores

class Main_Window(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        
        self.connect(self.menu_admin_ligas, SIGNAL('activated()'),
                     self.menu_admin_ligas_clicked)
        self.connect(self.menu_admin_equipos, SIGNAL('activated()'),
                     self.menu_admin_equipos_clicked)
        self.connect(self.menu_admin_jugadores, SIGNAL('activated()'),
                     self.menu_admin_jugadores_clicked)

    def menu_admin_ligas_clicked(self):
        
        ligas = Ligas(self)
        self.setCentralWidget(ligas)
        self.statusbar.showMessage(u'Añadir, editar y eliminar ligas')
    
    def menu_admin_equipos_clicked(self):
        
        equipos = Equipos(self)
        self.setCentralWidget(equipos)
        self.statusbar.showMessage(u'Añadir, editar y eliminar equipos')
        
    def menu_admin_jugadores_clicked(self):
        
        jugadores = Jugadores(self)
        self.setCentralWidget(jugadores)
        self.statusbar.showMessage(u'Añadir, editar y eliminar Jugadores')