import os
from PyQt5 import QtWidgets, uic
from Vista.FrmInventario import FrmInventario

ventanaEliminarRepuesto = os.path.join(os.path.dirname(__file__), '../UI/frmEliminarRepuesto.ui')

class FrmEliminarRepuesto(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(FrmEliminarRepuesto, self).__init__(parent)
        uic.loadUi(ventanaEliminarRepuesto, self)


        # BOTONES
        self.btnRegresar.clicked.connect(self.regresar)  



    def regresar(self):
        self.ventInventario = FrmInventario()
        self.ventInventario.show()
        self.close()