import os
from PyQt5 import QtWidgets, uic

ventanaAdministrador = os.path.join(os.path.dirname(__file__), '../UI/frmAdministrador.ui')

class FrmAdministrador(QtWidgets.QMainWindow):
    def __init__(self, parent=None, user_role=None):
        super(FrmAdministrador, self).__init__(parent)
        uic.loadUi(ventanaAdministrador, self)
        self.user_role = user_role

        # BOTONES
        self.btnRegresar.clicked.connect(self.regresar)

    def regresar(self):
        from Vista.FrmPrincipal import FrmPrincipal
        self.venPrincipal = FrmPrincipal(self, self.user_role)
        self.venPrincipal.show()
        self.close()
