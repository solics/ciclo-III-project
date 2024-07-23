import os
from PyQt5 import QtWidgets, uic

ventaInventario = os.path.join(os.path.dirname(__file__), '../UI/frmInventario.ui')

class FrmInventario(QtWidgets.QMainWindow):
    def __init__(self, parent=None, user_role=None):
        super(FrmInventario, self).__init__(parent)
        uic.loadUi(ventaInventario, self)
        self.user_role = user_role

        # Conectar botones
        self.btnBuscarRepuesto.clicked.connect(self.buscarRepuesto)
        self.btnRegistrarRepuesto.clicked.connect(self.registrarRepuesto)
        self.btnEliminarRepuesto.clicked.connect(self.eliminarRepuesto)
        self.btnRegresar.clicked.connect(self.regresar)


    def buscarRepuesto(self):
        from Vista.FrmBuscaRepuesto import FrmBuscarRepuesto 
        self.abrir = FrmBuscarRepuesto(self)
        self.abrir.show()

    def registrarRepuesto(self):
        from Vista.FrmRegistrarRepuesto import FrmRegistrarRepuesto 
        self.abrir = FrmRegistrarRepuesto(self)
        self.abrir.show()

    def eliminarRepuesto(self):
        from Vista.FrmEliminarRepuesto import FrmEliminarRepuesto  
        self.abrir = FrmEliminarRepuesto(self)
        self.abrir.show()


    def regresar(self):
        from Vista.FrmPrincipal import FrmPrincipal
        self.venPrincipal = FrmPrincipal(self, self.user_role)
        self.venPrincipal.show()
        self.close()