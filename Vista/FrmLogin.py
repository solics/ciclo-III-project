import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from Vista.FrmPrincipal import FrmPrincipal
from connection import conexion
import pyodbc

ventanaLogin = os.path.join(os.path.dirname(__file__), '../UI/frmLogin.ui')

class FrmLogin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(FrmLogin, self).__init__(parent)
        uic.loadUi(ventanaLogin, self)
        self.btnIngresar.clicked.connect(self.ingresar)
        self.txtUsuario.setFocus()
        self.show()
        
    def ingresar(self):
        usuario = self.txtUsuario.text()
        password = self.txtContrasena.text()
        
        if not usuario or not password:
            QMessageBox.warning(self, "Alerta", "Debe ingresar sus credenciales.")
            return

        if conexion is None:
            QMessageBox.critical(self, "Error de Conexión", "No se pudo establecer una conexión a la base de datos.")
            self.txtUsuario.clear()
            self.txtContrasena.clear()
            self.txtUsuario.setFocus()
            return

        try:
            cursor = conexion.cursor()
            sSql = f"SELECT usuario FROM Usuario WHERE usuario = '{usuario}' AND contrasena = '{password}'"
            cursor.execute(sSql)
            sqlResultf = cursor.fetchone()

            cursor.close()
            if sqlResultf:
                sqlR = sqlResultf[0]
                self.abrir = FrmPrincipal(self, sqlR)  
                self.abrir.show()
                self.hide()
            else:
                QMessageBox.warning(self, "Alerta", "Credenciales incorrectas, vuelva a intentar.")
                self.txtUsuario.clear()
                self.txtContrasena.clear()
                self.txtUsuario.setFocus()

        except pyodbc.Error as e:
            QMessageBox.critical(self, "Error de Conexión", f"No se pudo conectar a la base de datos: {str(e)}")
            self.txtUsuario.clear()
            self.txtContrasena.clear()
            self.txtUsuario.setFocus()
