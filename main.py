# -*- coding: UTF-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

from main_window import Main_Window #Importamos la ventan principal.

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setStyle("windows")
    main_window = Main_Window()
    main_window.show()
    sys.exit(app.exec_())
