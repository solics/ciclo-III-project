# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\PC\IDAT\CICLO III\ADSOO\PROYECTO\AutopartesOcampoSoli\UI\frmEliminarRepuesto.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(930, 505)
        MainWindow.setMinimumSize(QtCore.QSize(930, 505))
        MainWindow.setMaximumSize(QtCore.QSize(930, 505))
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.829, y1:0.107455, x2:0, y2:1, stop:0.295455 rgba(0, 105, 114, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(21, 22, 381, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:\'white\';")
        self.label.setObjectName("label")
        self.btnEliminar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEliminar.setGeometry(QtCore.QRect(652, 370, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.btnEliminar.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\PC\\IDAT\\CICLO III\\ADSOO\\PROYECTO\\AutopartesOcampoSoli\\UI\\../Img/deleting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEliminar.setIcon(icon)
        self.btnEliminar.setIconSize(QtCore.QSize(28, 28))
        self.btnEliminar.setObjectName("btnEliminar")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(678, 12, 241, 81))
        self.label_10.setStyleSheet("")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("c:\\Users\\PC\\IDAT\\CICLO III\\ADSOO\\PROYECTO\\AutopartesOcampoSoli\\UI\\../Img/LOGO PNG 1.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(120, 115, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:\'white\';")
        self.label_11.setObjectName("label_11")
        self.txtCodigo = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCodigo.setGeometry(QtCore.QRect(34, 139, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.txtCodigo.setFont(font)
        self.txtCodigo.setObjectName("txtCodigo")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(719, 115, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:\'white\';")
        self.label_13.setObjectName("label_13")
        self.lblCodigo_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblCodigo_2.setGeometry(QtCore.QRect(34, 115, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblCodigo_2.setFont(font)
        self.lblCodigo_2.setStyleSheet("color:\'white\';")
        self.lblCodigo_2.setObjectName("lblCodigo_2")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(527, 115, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color:\'white\';")
        self.label_14.setObjectName("label_14")
        self.txtNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(119, 139, 391, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.txtNombre.setFont(font)
        self.txtNombre.setObjectName("txtNombre")
        self.cmbMarca = QtWidgets.QComboBox(self.centralwidget)
        self.cmbMarca.setGeometry(QtCore.QRect(526, 138, 181, 22))
        self.cmbMarca.setObjectName("cmbMarca")
        self.cmbMarca.addItem("")
        self.cmbCategoria = QtWidgets.QComboBox(self.centralwidget)
        self.cmbCategoria.setGeometry(QtCore.QRect(716, 138, 191, 22))
        self.cmbCategoria.setObjectName("cmbCategoria")
        self.cmbCategoria.addItem("")
        self.tblRepuestos = QtWidgets.QTableWidget(self.centralwidget)
        self.tblRepuestos.setGeometry(QtCore.QRect(30, 169, 881, 191))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.tblRepuestos.setFont(font)
        self.tblRepuestos.setObjectName("tblRepuestos")
        self.tblRepuestos.setColumnCount(7)
        self.tblRepuestos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblRepuestos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblRepuestos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblRepuestos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblRepuestos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblRepuestos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblRepuestos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblRepuestos.setHorizontalHeaderItem(6, item)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 92, 901, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 410, 901, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(6, 101, 31, 321))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(906, 101, 31, 320))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.btnRegresar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 430, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnRegresar.setFont(font)
        self.btnRegresar.setStyleSheet("border-radius:5px;\n"
"color:white;\n"
"background-color: rgb(0, 65, 108);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\PC\\IDAT\\CICLO III\\ADSOO\\PROYECTO\\AutopartesOcampoSoli\\UI\\../Img/left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRegresar.setIcon(icon1)
        self.btnRegresar.setIconSize(QtCore.QSize(25, 25))
        self.btnRegresar.setObjectName("btnRegresar")
        self.btnBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscar.setGeometry(QtCore.QRect(789, 370, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.btnBuscar.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\PC\\IDAT\\CICLO III\\ADSOO\\PROYECTO\\AutopartesOcampoSoli\\UI\\../Img/loupe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscar.setIcon(icon2)
        self.btnBuscar.setIconSize(QtCore.QSize(28, 28))
        self.btnBuscar.setObjectName("btnBuscar")
        self.btnLimpiar = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimpiar.setGeometry(QtCore.QRect(520, 370, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.btnLimpiar.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\PC\\IDAT\\CICLO III\\ADSOO\\PROYECTO\\AutopartesOcampoSoli\\UI\\../Img/limpiar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLimpiar.setIcon(icon3)
        self.btnLimpiar.setIconSize(QtCore.QSize(28, 28))
        self.btnLimpiar.setObjectName("btnLimpiar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 930, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Eliminar Repuesto"))
        self.btnEliminar.setText(_translate("MainWindow", "Eliminar"))
        self.label_11.setText(_translate("MainWindow", "Nombre:"))
        self.label_13.setText(_translate("MainWindow", "Categoría"))
        self.lblCodigo_2.setText(_translate("MainWindow", "Código:"))
        self.label_14.setText(_translate("MainWindow", "Marca"))
        self.cmbMarca.setItemText(0, _translate("MainWindow", "Seleccionar Marca"))
        self.cmbCategoria.setItemText(0, _translate("MainWindow", "Seleccionar Categoría"))
        item = self.tblRepuestos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Código"))
        item = self.tblRepuestos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tblRepuestos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Marca"))
        item = self.tblRepuestos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Categoría"))
        item = self.tblRepuestos.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Stock Actual"))
        item = self.tblRepuestos.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Precio Unitario"))
        item = self.tblRepuestos.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Precio de Venta"))
        self.btnRegresar.setText(_translate("MainWindow", "Regresar"))
        self.btnBuscar.setText(_translate("MainWindow", "Buscar"))
        self.btnLimpiar.setText(_translate("MainWindow", "Limpiar"))