# -*- coding: UTF-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gui.ui_jugadores import Ui_Jugadores

class Jugadores(QWidget, Ui_Jugadores):
    
    def __init__(self, parent = None):
        
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.show()
        
        #Poner la cabecera a la tabla
        self.tabla_jugadores.setColumnCount(3)
        self.tabla_jugadores.setHorizontalHeaderLabels([
            'Nombre', 'Goles', 'Edad', ]) 