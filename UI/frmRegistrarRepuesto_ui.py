# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\PC\IDAT\CICLO III\ADSOO\PROYECTO\AutopartesOcampoSoli\UI\frmRegistrarRepuesto.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(930, 558)
        MainWindow.setMinimumSize(QtCore.QSize(930, 558))
        MainWindow.setMaximumSize(QtCore.QSize(930, 558))
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.829, y1:0.107455, x2:0, y2:1, stop:0.295455 rgba(0, 105, 114, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 18, 341, 61))
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
        self.lblCodigo = QtWidgets.QLabel(self.centralwidget)
        self.lblCodigo.setGeometry(QtCore.QRect(37, 115, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblCodigo.setFont(font)
        self.lblCodigo.setStyleSheet("color:\'white\';")
        self.lblCodigo.setObjectName("lblCodigo")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(128, 116, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:\'white\';")
        self.label_4.setObjectName("label_4")
        self.txtNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(126, 139, 371, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.txtNombre.setFont(font)
        self.txtNombre.setObjectName("txtNombre")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(36, 172, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:\'white\';")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(127, 173, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:\'white\';")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(256, 172, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:\'white\';")
        self.label_9.setObjectName("label_9")
        self.tblRepuestos = QtWidgets.QTableWidget(self.centralwidget)
        self.tblRepuestos.setGeometry(QtCore.QRect(27, 230, 871, 191))
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
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(514, 119, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:\'white\';")
        self.label_5.setObjectName("label_5")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(701, 117, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:\'white\';")
        self.label_12.setObjectName("label_12")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(663, 12, 241, 81))
        self.label_10.setStyleSheet("")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("c:\\Users\\PC\\IDAT\\CICLO III\\ADSOO\\PROYECTO\\AutopartesOcampoSoli\\UI\\../Img/LOGO PNG 1.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(897, 100, 31, 381))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.btnRegresar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegresar.setGeometry(QtCore.QRect(18, 486, 171, 41))
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\PC\\IDAT\\CICLO III\\ADSOO\\PROYECTO\\AutopartesOcampoSoli\\UI\\../Img/left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRegresar.setIcon(icon)
        self.btnRegresar.setIconSize(QtCore.QSize(25, 25))
        self.btnRegresar.setObjectName("btnRegresar")
        self.btnRegistrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegistrar.setGeometry(QtCore.QRect(768, 430, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.btnRegistrar.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\PC\\IDAT\\CICLO III\\ADSOO\\PROYECTO\\AutopartesOcampoSoli\\UI\\../Img/registrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRegistrar.setIcon(icon1)
        self.btnRegistrar.setIconSize(QtCore.QSize(28, 28))
        self.btnRegistrar.setObjectName("btnRegistrar")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(16, 469, 897, 20))
        self.line_10.setMaximumSize(QtCore.QSize(897, 20))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.txtCodigo = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCodigo.setGeometry(QtCore.QRect(36, 139, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.txtCodigo.setFont(font)
        self.txtCodigo.setObjectName("txtCodigo")
        self.txtPrecioCompra = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPrecioCompra.setGeometry(QtCore.QRect(130, 198, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.txtPrecioCompra.setFont(font)
        self.txtPrecioCompra.setObjectName("txtPrecioCompra")
        self.txtPrecioVenta = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPrecioVenta.setGeometry(QtCore.QRect(258, 198, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.txtPrecioVenta.setFont(font)
        self.txtPrecioVenta.setObjectName("txtPrecioVenta")
        self.txtCantidad = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCantidad.setGeometry(QtCore.QRect(38, 199, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.txtCantidad.setFont(font)
        self.txtCantidad.setObjectName("txtCantidad")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(16, 91, 897, 20))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(0, 100, 31, 381))
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.txtMarca = QtWidgets.QLineEdit(self.centralwidget)
        self.txtMarca.setGeometry(QtCore.QRect(510, 140, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.txtMarca.setFont(font)
        self.txtMarca.setObjectName("txtMarca")
        self.txtCategoria = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCategoria.setGeometry(QtCore.QRect(700, 140, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.txtCategoria.setFont(font)
        self.txtCategoria.setObjectName("txtCategoria")
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
        self.label.setText(_translate("MainWindow", "Registrar Repuesto"))
        self.lblCodigo.setText(_translate("MainWindow", "Código"))
        self.label_4.setText(_translate("MainWindow", "Nombre"))
        self.label_6.setText(_translate("MainWindow", "Cantidad"))
        self.label_8.setText(_translate("MainWindow", "Precio Unitario"))
        self.label_9.setText(_translate("MainWindow", "Precio de Venta"))
        item = self.tblRepuestos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Código"))
        item = self.tblRepuestos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tblRepuestos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Marca"))
        item = self.tblRepuestos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Categoría"))
        item = self.tblRepuestos.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cantidad"))
        item = self.tblRepuestos.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Precio Compra"))
        item = self.tblRepuestos.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Precio de Venta"))
        self.label_5.setText(_translate("MainWindow", "Marca"))
        self.label_12.setText(_translate("MainWindow", "Categoría"))
        self.btnRegresar.setText(_translate("MainWindow", "Regresar"))
        self.btnRegistrar.setText(_translate("MainWindow", "Registrar"))