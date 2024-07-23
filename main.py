import sys
from PyQt5 import QtWidgets
from Vista.FrmLogin import FrmLogin

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FrmLogin()
    window.show()
    sys.exit(app.exec())

