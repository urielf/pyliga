# -*- coding: UTF-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gui.ui_equipos import Ui_Equipos

class Equipos(QWidget, Ui_Equipos):
    
    def __init__(self, parent = None):
        
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.show()
        
        #Poner la cabecera a la tabla
        self.tabla_equipos.setColumnCount(8)
        self.tabla_equipos.setHorizontalHeaderLabels([
            'Equipo', 'Diferencia', 'Puntos', 'Jornadas', 
            'G. Favor', 'G. Contra', 'Contacto', u'Teléfono'])