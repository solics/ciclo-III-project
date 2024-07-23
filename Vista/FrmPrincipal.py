import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox 


ventanaPrincipal = os.path.join(os.path.dirname(__file__), '../UI/frmPrincipal.ui')

class FrmPrincipal(QtWidgets.QMainWindow):
    def __init__(self, parent=None, user_role=None):
        super(FrmPrincipal, self).__init__(parent)
        uic.loadUi(ventanaPrincipal, self)

        self.user_role = user_role 

        # BOTONES
        self.btnSalir.clicked.connect(self.salir)
        self.btnInventario.clicked.connect(self.inventario)
        self.btnVentas.clicked.connect(self.ventas)
        self.btnAdministrador.clicked.connect(self.administrador)
        
        # Configurar la visibilidad de los botones según el rol
        self.configurar_botones()

        self.show()

    def configurar_botones(self):
        if self.user_role == 'admin':
            self.btnInventario.setEnabled(True)
            self.btnVentas.setEnabled(True)
            self.btnAdministrador.setEnabled(True)
        elif self.user_role == 'ventas':
            self.btnInventario.setEnabled(False)
            self.btnVentas.setEnabled(True)
            self.btnAdministrador.setEnabled(False)
        elif self.user_role == 'inventario':
            self.btnInventario.setEnabled(True)
            self.btnVentas.setEnabled(False)
            self.btnAdministrador.setEnabled(False)
        else:
            # Si el rol no es reconocido, deshabilitar todos los botones
            self.btnInventario.setEnabled(False)
            self.btnVentas.setEnabled(False)
            self.btnAdministrador.setEnabled(False)


    def salir(self):
        reply = QMessageBox.question(self, 'Salir', '¿Estás seguro de que quieres salir?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()  # Cierra solo el formulario actual

    def inventario(self):
        from Vista.FrmInventario import FrmInventario 
        self.abrir = FrmInventario(self, self.user_role)
        self.abrir.show()


    def ventas(self):
        from Vista.FrmVentas import FrmVentas 
        self.abrir = FrmVentas(self, self.user_role)
        self.abrir.show()


    def administrador(self):
        from Vista.FrmAdministrador import FrmAdministrador  
        self.abrir = FrmAdministrador(self, self.user_role)
        self.abrir.show()

