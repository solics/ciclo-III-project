import os
from PyQt5 import QtWidgets, uic
from Vista.FrmAdministrador import FrmAdministrador
from connection import conexion
import openpyxl
from datetime import date

today = date.today()

wb = openpyxl.Workbook()

reporteVentas = os.path.join(os.path.dirname(__file__), '../UI/frmReporteVentas.ui')

class FrmReporteVentas(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(FrmReporteVentas, self).__init__(parent)
        uic.loadUi(reporteVentas, self)
        
        self.btnRegresar.clicked.connect(self.regresar)
        self.btnGenerar.clicked.connect(self.generar)
        self.btnConsultar.clicked.connect(self.consultar)
        
        self.fechaInicio.setDate(today)
        self.fechaFin.setDate(today)
        self.fechaInicio.setCalendarPopup(True)
        self.fechaFin.setCalendarPopup(True)

    def regresar(self):
        self.close()
        
    def generar(self):
        # fecha_actual = datetime.now().strftime('%d/%m/%Y')
        # print(fecha_actual)
        fInicio = self.fechaInicio.date()
        fFin = self.fechaFin.date()
        fInicioStr = str(fInicio.day())+'/'+str(fInicio.month())+'/'+str(fInicio.year())
        fFinStr =  str(fFin.day())+'/'+str(fFin.month())+'/'+str(fFin.year())
        fInicioStrFile = str(fInicio.day())+'-'+str(fInicio.month())+'-'+str(fInicio.year())
        fFinStrFile =  str(fFin.day())+'-'+str(fFin.month())+'-'+str(fFin.year())

        try:
            cursor = conexion.cursor()
            queryVentas = """SELECT * from Ventas where fecha BETWEEN ? AND ? """
            params= (fInicioStr,fFinStr)
            recordVentas = cursor.execute(queryVentas, params)
            ventas = recordVentas.fetchall()
            
            hoja = wb.active
            hoja.append(('Nro. Venta','Tipo Comprobante', 'Fecha'))
            for venta in ventas:
                hoja.append(list(venta))

            carpetaReporte = 'Reporte Ventas'
            if not os.path.exists(carpetaReporte):
                os.makedirs(carpetaReporte)
            
            nombreArchivo = f'ReporteVentas de {fInicioStrFile} a {fFinStrFile}.xlsx'
            print(nombreArchivo)
            reportesPath = os.path.join(carpetaReporte, nombreArchivo)
            
            wb.save(reportesPath)
            
            QtWidgets.QMessageBox.information(self, "Genial", "Se creo exitosamente el reporte en ReporteVentasFecha.xlsx.")
            
                
        except FileNotFoundError:
            print("No se pudo traer la informacion de la tabla Inventario")
            QtWidgets.QMessageBox.information(self, "Genial", "No se pudo descargar el reporte.")
            
            
    def consultar(self):
        fInicio = self.fechaInicio.date()
        fFin = self.fechaFin.date()
        fInicioStr = str(fInicio.day())+'/'+str(fInicio.month())+'/'+str(fInicio.year())
        fFinStr =  str(fFin.day())+'/'+str(fFin.month())+'/'+str(fFin.year())
        tabla = self.tblInventario
        
        try:
            cursor = conexion.cursor()
            queryVentas = """SELECT * from Ventas where fecha BETWEEN ? AND ? """
            params= (fInicioStr,fFinStr)
            recordVentas = cursor.execute(queryVentas, params)
            ventas = recordVentas.fetchall()
            
            print(ventas)
            if len(ventas) == 0:
                QtWidgets.QMessageBox.information(self, "Oh no", "No hay ventas registradas.")
            
            for i in range(len(ventas)):
                tabla.setRowCount(len(ventas))
                tabla.setItem(i, 0, QtWidgets.QTableWidgetItem(str(ventas[i][0])))
                tabla.setItem(i, 1, QtWidgets.QTableWidgetItem(str(ventas[i][1])))
                tabla.setItem(i, 2, QtWidgets.QTableWidgetItem(str(ventas[i][2])))
                
        except FileNotFoundError:
            print("No se pudo traer la informacion de la tabla Ventas")