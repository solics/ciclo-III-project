import os
from PyQt5 import QtWidgets, uic
from Vista.FrmInventario import FrmInventario

ventanaRegistrarRepuesto = os.path.join(os.path.dirname(__file__), '../UI/frmRegistrarRepuesto.ui')

class FrmRegistrarRepuesto(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(FrmRegistrarRepuesto, self).__init__(parent)
        uic.loadUi(ventanaRegistrarRepuesto, self)
        
        # BOTONES
        self.btnRegresar.clicked.connect(self.regresar)

    def registrar(self):
        
    def regresar(self):
        self.ventInventario = FrmInventario()
        self.ventInventario.show()
        self.close()
        
    