import os
from PyQt5 import QtWidgets, uic
from Vista.FrmInventario import FrmInventario
from connection import conexion

ventaBuscarRepuesto = os.path.join(os.path.dirname(__file__), '../UI/frmBuscarRepuesto.ui')

class FrmBuscarRepuesto(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(FrmBuscarRepuesto, self).__init__(parent)
        uic.loadUi(ventaBuscarRepuesto, self)
        
        self.btnRegresar.clicked.connect(self.regresar)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnBuscar.clicked.connect(self.buscar)

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

    def regresar(self):
        self.ventInventario = FrmInventario()
        self.ventInventario.show()
        self.close()
        
    def buscar(self):
        nombre = self.txtNombre.text()
        codigo = self.txtCodigo.text()
        marca = self.cmbMarca.currentText()
        
        marca = ''
        if self.cmbMarca.currentText() != 'Seleccionar Marca':
            marca = self.cmbMarca.currentText()
            
        categ = ''
        if self.cmbCategoria.currentText() != 'Seleccionar Categoría':
            categ = self.cmbCategoria.currentText()
            
        tabla = self.tblRepuestos
        try:
            cursor = conexion.cursor()
            queryRepuestos = """SELECT i.*,c.nombreCategoria,m.nombreMarca FROM Inventario i
                    INNER JOIN categoria c on i.idCategoria = c.idCategoria
                    INNER JOIN marca m on m.idMarca = i.idMarca
                    WHERE (i.codRepuesto LIKE ? OR ? = '')
                    AND (LOWER(i.nombreRepuesto) LIKE LOWER(?) OR ? = '')
                    AND (c.nombreCategoria = ? OR ? = '')
                    AND (m.nombreMarca = ? OR ? = '')"""
                    
                
            params = ('%' + codigo + '%' , codigo, '%' +nombre+ '%', nombre, categ, categ, marca, marca)
            recordRepuestos = cursor.execute(queryRepuestos, params)
            repuestos = recordRepuestos.fetchall()
            
            self.clearRows()
            
            if len(repuestos) == 0:
                QtWidgets.QMessageBox.information(self, "Oh no", "No hay repuestos con los datos ingresados.")

            for i in range(len(repuestos)):
                tabla.setRowCount(len(repuestos))
                tabla.setItem(i, 0, QtWidgets.QTableWidgetItem(str(repuestos[i][1])))
                tabla.setItem(i, 1, QtWidgets.QTableWidgetItem(str(repuestos[i][2])))
                tabla.setItem(i, 2, QtWidgets.QTableWidgetItem(str(repuestos[i][9])))
                tabla.setItem(i, 3, QtWidgets.QTableWidgetItem(str(repuestos[i][8])))
                tabla.setItem(i, 4, QtWidgets.QTableWidgetItem(str(repuestos[i][5])))
                tabla.setItem(i, 5, QtWidgets.QTableWidgetItem(str(repuestos[i][6])))
                tabla.setItem(i, 6, QtWidgets.QTableWidgetItem(str(repuestos[i][7])))
        except FileNotFoundError:
            print("No se pudo traer la informacion de la tabla Inventario")
            
    def limpiar(self):
        self.txtNombre.clear()
        self.txtCodigo.clear()
        self.cmbMarca.setCurrentIndex(0)
        self.cmbCategoria.setCurrentIndex(0)
        self.clearRows()

    def clearRows(self):
        for i in range(self.tblRepuestos.rowCount()):
            self.tblRepuestos.removeRow(i)