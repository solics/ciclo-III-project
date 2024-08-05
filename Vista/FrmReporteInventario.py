import os
from PyQt5 import QtWidgets, uic
from Vista.FrmAdministrador import FrmAdministrador
from connection import conexion
import openpyxl
wb = openpyxl.Workbook()

reporteInventario = os.path.join(os.path.dirname(__file__), '../UI/frmReporteInventario.ui')

class FrmReporteInventario(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(FrmReporteInventario, self).__init__(parent)
        uic.loadUi(reporteInventario, self)
        
        self.btnRegresar.clicked.connect(self.regresar)
        self.btnGenerar.clicked.connect(self.generar)
        self.btnConsultar.clicked.connect(self.consultar)

    def regresar(self):
        self.close()

    def generar(self):
        try:
            cursor = conexion.cursor()
            queryRepuestos = """SELECT i.codRepuesto, i.nombreRepuesto, m.nombreMarca,
                                c.nombreCategoria, i.stockActual, i.precioCompra, i.precioVenta
                                FROM Inventario i 
                                INNER JOIN categoria c on i.idCategoria = c.idCategoria
                                INNER JOIN marca m on m.idMarca = i.idMarca"""
            recordRepuestos = cursor.execute(queryRepuestos)
            repuestos = recordRepuestos.fetchall()
            
            hoja = wb.active
            hoja.append(('Codigo Producto','Nombre', 'Marca', 'Categoria', 'Cantidad', 'Precio Compra', 'Precio Venta'))
            for repuesto in repuestos:
                hoja.append(list(repuesto))

            carpetaReporte = 'Reportes Inventario'
            if not os.path.exists(carpetaReporte):
                os.makedirs(carpetaReporte)
            reportesPath = os.path.join(carpetaReporte, 'InventarioRepuestos.xlsx')
            wb.save(reportesPath)
            QtWidgets.QMessageBox.information(self, "Genial", "Se creo exitosamente el reporte en ReporteInventario.xlsx.")
            
                
        except FileNotFoundError:
            print("No se pudo traer la informacion de la tabla Inventario")
            QtWidgets.QMessageBox.information(self, "Genial", "No se pudo descargar el reporte.")
            
            
    def consultar(self):
        tabla = self.tblInventario
        try:
            cursor = conexion.cursor()
            queryRepuestos = """SELECT i.codRepuesto, i.nombreRepuesto, m.nombreMarca,
                                c.nombreCategoria, i.stockActual, i.precioCompra, i.precioVenta
                                FROM Inventario i 
                                INNER JOIN categoria c on i.idCategoria = c.idCategoria
                                INNER JOIN marca m on m.idMarca = i.idMarca"""
            recordRepuestos = cursor.execute(queryRepuestos)
            repuestos = recordRepuestos.fetchall()
            
            if len(repuestos) == 0:
                QtWidgets.QMessageBox.information(self, "Oh no", "No hay repuestos registrados en el inventario.")
            
            for i in range(len(repuestos)):
                tabla.setRowCount(len(repuestos))
                tabla.setItem(i, 0, QtWidgets.QTableWidgetItem(str(repuestos[i][0])))
                tabla.setItem(i, 1, QtWidgets.QTableWidgetItem(str(repuestos[i][1])))
                tabla.setItem(i, 2, QtWidgets.QTableWidgetItem(str(repuestos[i][2])))
                tabla.setItem(i, 3, QtWidgets.QTableWidgetItem(str(repuestos[i][3])))
                tabla.setItem(i, 4, QtWidgets.QTableWidgetItem(str(repuestos[i][4])))
                tabla.setItem(i, 5, QtWidgets.QTableWidgetItem(str(repuestos[i][5])))
                tabla.setItem(i, 6, QtWidgets.QTableWidgetItem(str(repuestos[i][6])))
                
        except FileNotFoundError:
            print("No se pudo traer la informacion de la tabla Inventario")