
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Reportes(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1259, 722)
        Form.setGeometry(
            (Form.screen().geometry().width() - Form.geometry().width()) // 2,
            (Form.screen().geometry().height() - Form.geometry().height()) // 2,
            Form.geometry().width(),
            Form.geometry().height()
        )
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1271, 771))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.widget_3 = QtWidgets.QWidget(parent=self.widget)
        self.widget_3.setGeometry(QtCore.QRect(70, 100, 1131, 591))
        self.widget_3.setStyleSheet("border: 1px solid rgb(239, 239, 239);\n"
        "border-radius: 8px;")
        self.widget_3.setObjectName("widget_3")
        self.btnBuscar = QtWidgets.QPushButton(parent=self.widget_3)
        self.btnBuscar.setGeometry(QtCore.QRect(390, 10, 141, 41))
        font = QtGui.QFont()
        font.setBold(True)
        self.btnBuscar.setFont(font)
        self.btnBuscar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnBuscar.setStyleSheet("QPushButton {\n"
        "    border-radius: 20px;\n"
        "    background-color: rgb(24, 71, 113);\n"
        "    color: rgb(255, 255, 255);\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(255, 255, 255);\n"
        "    color: rgb(24, 71, 113);\n"
        "    border: 1px solid rgb(24, 71, 113);\n"
        "}")
        self.btnBuscar.setObjectName("btnBuscar")
        self.label_10 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_10.setGeometry(QtCore.QRect(30, 30, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.txtTexto = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtTexto.setGeometry(QtCore.QRect(230, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtTexto.setFont(font)
        self.txtTexto.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.txtTexto.setObjectName("txtTexto")
        self.txtTexto2 = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtTexto2.setGeometry(QtCore.QRect(230, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtTexto2.setFont(font)
        self.txtTexto2.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"")
        self.txtTexto2.setObjectName("txtTexto2")
        self.txtTexto3 = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtTexto3.setGeometry(QtCore.QRect(230, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtTexto3.setFont(font)
        self.txtTexto3.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.txtTexto3.setObjectName("txtTexto3")
        self.btnGenerar = QtWidgets.QPushButton(parent=self.widget_3)
        self.btnGenerar.setGeometry(QtCore.QRect(280, 200, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.btnGenerar.setFont(font)
        self.btnGenerar.setStyleSheet("QPushButton {\n"
"    border-radius: 20px;\n"
"    background-color: rgb(15, 121, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(10, 90, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.btnGenerar.setObjectName("btnGenerar")
        self.label_11 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_11.setGeometry(QtCore.QRect(30, 80, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.txtLogo = QtWidgets.QLabel(parent=self.widget)
        self.txtLogo.setGeometry(QtCore.QRect(1163, 5, 91, 71))
        self.txtLogo.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.txtLogo.setMidLineWidth(-2)
        self.txtLogo.setText("")
        self.txtLogo.setPixmap(QtGui.QPixmap("logo2.PNG"))
        self.txtLogo.setScaledContents(True)
        self.txtLogo.setObjectName("txtLogo")
        self.frame = QtWidgets.QFrame(parent=self.widget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1261, 80))
        self.frame.setStyleSheet("background-color: rgb(24, 71, 113);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(530, 20, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(30)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.btnRegresar = QtWidgets.QPushButton(parent=self.frame)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 20, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.btnRegresar.setFont(font)
        self.btnRegresar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnRegresar.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(239, 239, 239);\n"
"    color:  rgb(24, 71, 113);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(24, 71, 113);\n"
"}")
        self.btnRegresar.setObjectName("btnRegresar")
        self.frame.raise_()
        self.widget_3.raise_()
        self.txtLogo.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.btnRegresar.clicked.connect(self.open_regresar)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnBuscar.setText(_translate("Form", "BUSCAR"))
        self.label_10.setText(_translate("Form", "TEXTO"))
        self.btnGenerar.setText(_translate("Form", "GENERAR"))
        self.label_11.setText(_translate("Form", "TEXTO"))
        self.label_3.setText(_translate("Form", "REPORTES"))
        self.btnRegresar.setText(_translate("Form", "REGRESAR"))

    def open_regresar(self):
        self.close()
        self.ventana_prin.show()

    def keyPressEvent(self, event):
        """Detecta si se presionó la tecla Escape y regresa a la ventana principal."""
        if event.key() == Qt.Key.Key_Escape:
            self.open_regresar()

    def __init__(self, dato, ventana_principal):
        super().__init__()
        self.id_user = dato
        self.ventana_prin = ventana_principal
        self.setupUi(self)

import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_Reportes()
    window.show()
    sys.exit(app.exec())