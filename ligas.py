# -*- coding: UTF-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from gui.ui_ligas import Ui_Ligas

class Ligas(QWidget, Ui_Ligas):
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.show()
        
        #Poner la cabecera de las ligas
        self.tabla_ligas.setColumnCount(2)
        self.tabla_ligas.setHorizontalHeaderLabels(['Liga', 'Jornadas'])
        
        #Colocar la fecha actual a los date edit
        self.dt_fecha_inicio.setDisplayFormat(u'dd/MM/yyyy')
        self.dt_fecha_inicio.setDate(QDate().currentDate())
        self.dt_fecha_final.setDisplayFormat(u'dd/MM/yyyy')
        self.dt_fecha_final.setDate(QDate().currentDate())