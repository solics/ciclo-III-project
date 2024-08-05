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
        self.btnReporteInventario.clicked.connect(self.reporteInventario)
        self.btnReporteVentas.clicked.connect(self.reporteVentas)

    def configurar_botones(self):
        self.btnReporteInventario.setEnabled(True)
        self.btnReporteVentas.setEnabled(True)
    
    def reporteInventario(self):
        from Vista.FrmReporteInventario import FrmReporteInventario 
        self.abrir = FrmReporteInventario(self)
        self.abrir.show()
    
    def reporteVentas(self):
        from Vista.FrmReporteVentas import FrmReporteVentas 
        self.abrir = FrmReporteVentas(self)
        self.abrir.show()

    def regresar(self):
        from Vista.FrmPrincipal import FrmPrincipal
        self.venPrincipal = FrmPrincipal(self, self.user_role)
        self.venPrincipal.show()
        self.close()
