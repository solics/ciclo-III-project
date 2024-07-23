import os
from PyQt5 import QtWidgets, uic
from Vista.FrmInventario import FrmInventario
from connection import conexion
import pyodbc

ventanaRegistrarRepuesto = os.path.join(os.path.dirname(__file__), '../UI/frmRegistrarRepuesto.ui')

class FrmRegistrarRepuesto(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(FrmRegistrarRepuesto, self).__init__(parent)
        uic.loadUi(ventanaRegistrarRepuesto, self)
        
        # BOTONES
        self.btnRegresar.clicked.connect(self.regresar)
        self.btnRegistrar.clicked.connect(self.registrar)
        
        # llenar combos marca y categoria
        cursor = conexion.cursor()
        
        comboMarca = self.cmbMarca
        queryMarcas = "SELECT * FROM Marca"
        recordMarcas = cursor.execute(queryMarcas)
        marcas = recordMarcas.fetchall()
        for code in marcas:
            comboMarca.addItem(code[1])
            
        comboCategoria = self.cmbCategoria
        queryCat = "SELECT * FROM Categoria"
        recordCat = cursor.execute(queryCat)
        cat = recordCat.fetchall()
        
        for code in cat:
            comboCategoria.addItem(code[1])

    def registrar(self):
        codRepuesto = self.txtCodigo.text()
        nombreRepuesto = self.txtNombre.text()
        nombreMarca = self.cmbMarca.currentText()
        nombreCategoria = self.cmbCategoria.currentText()
        cantidad = self.txtCantidad.text()
        pUnitario = self.txtPrecioCompra.text()
        pVenta = self.txtPrecioVenta.text()
        
        try:
            cursor = conexion.cursor()
            # Obtener idMarca a partir del nombre de la marca
            cursor.execute("SELECT idMarca FROM Marca WHERE nombreMarca = ?", (nombreMarca,))
            idMarca = cursor.fetchone()
            if not idMarca:
                QtWidgets.QMessageBox.warning(self, "Alerta", "La marca seleccionada no es válida.")
                return
            idMarca = idMarca[0]

            # Obtener idCategoria a partir del nombre de la categoría
            cursor.execute("SELECT idCategoria FROM Categoria WHERE nombreCategoria = ?", (nombreCategoria,))
            idCategoria = cursor.fetchone()
            if not idCategoria:
                QtWidgets.QMessageBox.warning(self, "Alerta", "La categoría seleccionada no es válida.")
                return
            idCategoria = idCategoria[0]
            
            query = """
                INSERT INTO Inventario (codRepuesto, nombreRepuesto, idMarca, idCategoria, stockActual, precioCompra, previoVenta)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (codRepuesto, nombreRepuesto, idMarca, idCategoria, cantidad, pUnitario, pVenta))
            conexion.commit()
            cursor.close()
            conexion.close()
            QtWidgets.QMessageBox.information(self, "Éxito", "Repuesto registrado correctamente.")
            self.limpiarFormulario()
            
        except pyodbc.Error as e:
            QtWidgets.QMessageBox.critical(self, "Error de Conexión", f"No se pudo conectar a la base de datos: {str(e)}")
    
    def regresar(self):
        self.ventInventario = FrmInventario()
        self.ventInventario.show()
        self.close()
        
    
    def limpiarFormulario(self):
        self.txtCodigo.clear()
        self.txtNombre.clear()
        self.cmbMarca.setCurrentIndex(0)  # Limpiar campo de texto de marca
        self.cmbCategoria.setCurrentIndex(0)  # Limpiar campo de texto de categoría
        self.txtCantidad.clear()
        self.txtPrecioCompra.clear()
        self.txtPrecioVenta.clear()