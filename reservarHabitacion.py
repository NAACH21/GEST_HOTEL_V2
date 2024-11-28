
import subprocess
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QDate, QDateTime, Qt, QCoreApplication, QRect
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QPushButton
from pyexpat.errors import messages
import conexion
from gestionCliente import Ui_GestClie
from images import resource_path

class Ui_ReserHabi(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1259, 722)
        MainWindow.setGeometry(
            (MainWindow.screen().geometry().width() - MainWindow.geometry().width()) // 2,
            (MainWindow.screen().geometry().height() - MainWindow.geometry().height()) // 2,
            MainWindow.geometry().width(),
            MainWindow.geometry().height()
        )
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1271, 771))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.widget_2.setGeometry(QtCore.QRect(40, 190, 1181, 211))
        self.widget_2.setStyleSheet("border: 1px solid rgb(239, 239, 239);\n"
                                    "border-radius: 8px;")
        self.widget_2.setObjectName("widget_2")
        self.tblHabitacion = QtWidgets.QTableWidget(parent=self.widget_2)
        self.tblHabitacion.setGeometry(QtCore.QRect(10, 40, 801, 161))
        self.tblHabitacion.setMaximumSize(QtCore.QSize(96100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.tblHabitacion.setFont(font)
        self.tblHabitacion.setStyleSheet("background-color: rgb(226, 245, 255);\n"
                                         "border-radius:8px;\n"
                                         "")
        self.tblHabitacion.setObjectName("tblHabitacion")
        self.tblHabitacion.setColumnCount(8)
        self.tblHabitacion.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tblHabitacion.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(7, item)
        self.tblHabitacion.verticalHeader().setMinimumSectionSize(24)
        self.txtBuscarHabitacion = QtWidgets.QLineEdit(parent=self.widget_2)
        self.txtBuscarHabitacion.setGeometry(QtCore.QRect(330, 10, 291, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txtBuscarHabitacion.setFont(font)
        self.txtBuscarHabitacion.setStyleSheet("background-color: rgb(239, 239, 239);\n"
                                               "border-radius:8px;")
        self.txtBuscarHabitacion.setObjectName("txtBuscarHabitacion")
        self.label_5 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txtImagenHabitacion = QtWidgets.QLabel(parent=self.widget_2)
        self.txtImagenHabitacion.setGeometry(QtCore.QRect(880, 50, 201, 151))
        self.txtImagenHabitacion.setText("")
        self.txtImagenHabitacion.setPixmap(QtGui.QPixmap(":/habitacion1.jpeg"))
        self.txtImagenHabitacion.setScaledContents(True)
        self.txtImagenHabitacion.setObjectName("txtImagenHabitacion")
        self.txtIdHabitacionSele = QtWidgets.QLineEdit(parent=self.widget_2)
        self.txtIdHabitacionSele.setEnabled(True)
        self.txtIdHabitacionSele.setGeometry(QtCore.QRect(1020, 20, 61, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtIdHabitacionSele.setFont(font)
        self.txtIdHabitacionSele.setStyleSheet("background-color: rgb(239, 239, 239);\n"
                                               "border-radius:4px;")
        self.txtIdHabitacionSele.setObjectName("txtIdHabitacionSele")
        self.label_22 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_22.setGeometry(QtCore.QRect(880, 30, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_21 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_21.setGeometry(QtCore.QRect(880, 10, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.widget_3 = QtWidgets.QWidget(parent=self.widget)
        self.widget_3.setGeometry(QtCore.QRect(40, 100, 671, 81))
        self.widget_3.setStyleSheet("border: 1px solid rgb(239, 239, 239);\n"
                                    "border-radius: 8px;")
        self.widget_3.setObjectName("widget_3")
        self.btnNuevoCliente = QtWidgets.QPushButton(parent=self.widget_3)
        self.btnNuevoCliente.setGeometry(QtCore.QRect(490, 30, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.btnNuevoCliente.setFont(font)
        self.btnNuevoCliente.setStyleSheet("QPushButton {\n"
                                           "    border-radius: 20px;\n"
                                           "    background-color: rgb(15, 121, 255);\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(10, 90, 200);\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "}")
        self.btnNuevoCliente.setObjectName("btnNuevoCliente")
        self.label_2 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtBuscarCliente = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtBuscarCliente.setGeometry(QtCore.QRect(230, 3, 231, 28))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        self.txtBuscarCliente.setFont(font)
        self.txtBuscarCliente.setStyleSheet("background-color: rgb(239, 239, 239);\n"
                                            "border-radius:8px;")
        self.txtBuscarCliente.setText("")
        self.txtBuscarCliente.setObjectName("txtBuscarCliente")
        self.cmbClientes = QtWidgets.QComboBox(parent=self.widget_3)
        self.cmbClientes.setGeometry(QtCore.QRect(20, 40, 441, 28))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        self.cmbClientes.setFont(font)
        self.cmbClientes.setStyleSheet("background-color: rgb(239, 239, 239);\n"
                                       "border-radius:4px;")
        self.cmbClientes.setObjectName("cmbClientes")
        self.cmbClientes.addItem("")
        self.cmbClientes.setItemText(0, "")
        self.btnLimpiar = QtWidgets.QPushButton(parent=self.widget)
        self.btnLimpiar.setGeometry(QtCore.QRect(480, 660, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.btnLimpiar.setFont(font)
        self.btnLimpiar.setStyleSheet("QPushButton {\n"
                                      "    border-radius: 20px;\n"
                                      "    background-color: rgb(15, 121, 255);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(10, 90, 200);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "}")
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.btnRegistrar = QtWidgets.QPushButton(parent=self.widget)
        self.btnRegistrar.setGeometry(QtCore.QRect(260, 660, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.btnRegistrar.setFont(font)
        self.btnRegistrar.setStyleSheet("QPushButton {\n"
                                        "    border-radius: 20px;\n"
                                        "    background-color: rgb(15, 121, 255);\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(10, 90, 200);\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "}")
        self.btnRegistrar.setObjectName("btnRegistrar")
        self.widget_5 = QtWidgets.QWidget(parent=self.widget)
        self.widget_5.setGeometry(QtCore.QRect(40, 410, 661, 111))
        self.widget_5.setStyleSheet("border: 1px solid rgb(239, 239, 239);\n"
                                    "border-radius: 8px;")
        self.widget_5.setObjectName("widget_5")
        self.label_16 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_16.setGeometry(QtCore.QRect(10, 10, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.cmbServiciosExtra = QtWidgets.QComboBox(parent=self.widget_5)
        self.cmbServiciosExtra.setGeometry(QtCore.QRect(10, 40, 431, 24))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(False)
        self.cmbServiciosExtra.setFont(font)
        self.cmbServiciosExtra.setStyleSheet("background-color: rgb(239, 239, 239);\n"
                                             "border-radius:4px;")
        self.cmbServiciosExtra.setPlaceholderText("")
        self.cmbServiciosExtra.setObjectName("cmbServiciosExtra")
        self.cmbServiciosExtra.addItem("")
        self.cmbServiciosExtra.setItemText(0, "")
        self.cmbServiciosExtra.addItem("")
        self.cmbServiciosExtra.addItem("")
        self.cmbServiciosExtra.addItem("")
        self.cmbServiciosExtra.addItem("")
        self.cmbServiciosExtra.addItem("")
        self.txtCantidadServicioExtra = QtWidgets.QLineEdit(parent=self.widget_5)
        self.txtCantidadServicioExtra.setEnabled(True)
        self.txtCantidadServicioExtra.setGeometry(QtCore.QRect(260, 80, 71, 24))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.txtCantidadServicioExtra.setFont(font)
        self.txtCantidadServicioExtra.setStyleSheet("background-color: rgb(239, 239, 239);\n"
                                                    "border-radius:4px;")
        self.txtCantidadServicioExtra.setObjectName("txtCantidadServicioExtra")
        self.label_14 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_14.setGeometry(QtCore.QRect(10, 80, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_17 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_17.setGeometry(QtCore.QRect(450, 40, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.txtPrecioServicioExtra = QtWidgets.QLineEdit(parent=self.widget_5)
        self.txtPrecioServicioExtra.setEnabled(False)
        self.txtPrecioServicioExtra.setGeometry(QtCore.QRect(560, 40, 81, 24))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.txtPrecioServicioExtra.setFont(font)
        self.txtPrecioServicioExtra.setStyleSheet("background-color: rgb(239, 239, 239);\n"
                                                  "border-radius:4px;")
        self.txtPrecioServicioExtra.setPlaceholderText("")
        self.txtPrecioServicioExtra.setObjectName("txtPrecioServicioExtra")
        self.widget_4 = QtWidgets.QWidget(parent=self.widget)
        self.widget_4.setGeometry(QtCore.QRect(40, 530, 661, 111))
        self.widget_4.setStyleSheet("border: 1px solid rgb(239, 239, 239);\n"
                                    "border-radius: 8px;")
        self.widget_4.setObjectName("widget_4")
        self.rbtTarjeta = QtWidgets.QRadioButton(parent=self.widget_4)
        self.rbtTarjeta.setGeometry(QtCore.QRect(430, 43, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rbtTarjeta.setFont(font)
        self.rbtTarjeta.setObjectName("rbtTarjeta")
        self.rbtYape = QtWidgets.QRadioButton(parent=self.widget_4)
        self.rbtYape.setGeometry(QtCore.QRect(320, 43, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rbtYape.setFont(font)
        self.rbtYape.setObjectName("rbtYape")
        self.rbtEfectivo = QtWidgets.QRadioButton(parent=self.widget_4)
        self.rbtEfectivo.setGeometry(QtCore.QRect(216, 43, 89, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rbtEfectivo.setFont(font)
        self.rbtEfectivo.setObjectName("rbtEfectivo")
        self.label_15 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_15.setGeometry(QtCore.QRect(12, 43, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.txtMontoTotal = QtWidgets.QLineEdit(parent=self.widget_4)
        self.txtMontoTotal.setEnabled(False)
        self.txtMontoTotal.setGeometry(QtCore.QRect(310, 10, 131, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtMontoTotal.setFont(font)
        self.txtMontoTotal.setStyleSheet("background-color: rgb(239, 239, 239);\n"
                                         "border-radius:4px;")
        self.txtMontoTotal.setText("")
        self.txtMontoTotal.setObjectName("txtMontoTotal")
        self.label_13 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_13.setGeometry(QtCore.QRect(12, 10, 291, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.rbtPendiente = QtWidgets.QRadioButton(parent=self.widget_4)
        self.rbtPendiente.setGeometry(QtCore.QRect(370, 80, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.rbtPendiente.setFont(font)
        self.rbtPendiente.setObjectName("rbtPendiente")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rbtPendiente)
        self.rbtCancelado = QtWidgets.QRadioButton(parent=self.widget_4)
        self.rbtCancelado.setGeometry(QtCore.QRect(216, 80, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rbtCancelado.setFont(font)
        self.rbtCancelado.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.rbtCancelado.setObjectName("rbtCancelado")
        self.buttonGroup.addButton(self.rbtCancelado)
        self.label_18 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_18.setGeometry(QtCore.QRect(12, 77, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.txtLogo = QtWidgets.QLabel(parent=self.widget)
        self.txtLogo.setGeometry(QtCore.QRect(1163, 5, 91, 71))
        self.txtLogo.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.txtLogo.setMidLineWidth(-2)
        self.txtLogo.setText("")
        #self.txtLogo.setPixmap(QtGui.QPixmap("logo2.PNG"))
        self.txtLogo.setPixmap(QtGui.QPixmap(resource_path("imagenes/logo2.PNG")))
        self.txtLogo.setScaledContents(True)
        self.txtLogo.setObjectName("txtLogo")
        self.frame = QtWidgets.QFrame(parent=self.widget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1261, 80))
        self.frame.setStyleSheet("background-color: rgb(24, 71, 113);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(370, 20, 681, 41))
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
        self.widget_6 = QtWidgets.QWidget(parent=self.widget)
        self.widget_6.setGeometry(QtCore.QRect(720, 410, 501, 111))
        self.widget_6.setStyleSheet("border: 1px solid rgb(239, 239, 239);\n"
                                    "border-radius: 8px;")
        self.widget_6.setObjectName("widget_6")
        self.dtFechaSalida = QtWidgets.QDateTimeEdit(parent=self.widget_6)
        self.dtFechaSalida.setGeometry(QtCore.QRect(216, 76, 221, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dtFechaSalida.setFont(font)
        self.dtFechaSalida.setObjectName("dtFechaSalida")
        self.dtFechaEntrada = QtWidgets.QDateTimeEdit(parent=self.widget_6)
        self.dtFechaEntrada.setGeometry(QtCore.QRect(216, 43, 221, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dtFechaEntrada.setFont(font)
        self.dtFechaEntrada.setObjectName("dtFechaEntrada")
        self.label_12 = QtWidgets.QLabel(parent=self.widget_6)
        self.label_12.setGeometry(QtCore.QRect(10, 76, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_10 = QtWidgets.QLabel(parent=self.widget_6)
        self.label_10.setGeometry(QtCore.QRect(12, 10, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.widget_6)
        self.label_11.setGeometry(QtCore.QRect(10, 43, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.txtNDiasHospedar = QtWidgets.QLineEdit(parent=self.widget_6)
        self.txtNDiasHospedar.setGeometry(QtCore.QRect(220, 10, 51, 24))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.txtNDiasHospedar.setFont(font)
        self.txtNDiasHospedar.setStyleSheet("background-color: rgb(239, 239, 239);\n"
                                            "border-radius:4px;")
        self.txtNDiasHospedar.setText("")
        self.txtNDiasHospedar.setObjectName("txtNDiasHospedar")
        self.widget_7 = QtWidgets.QWidget(parent=self.widget)
        self.widget_7.setGeometry(QtCore.QRect(720, 530, 501, 71))
        self.widget_7.setStyleSheet("border: 1px solid rgb(239, 239, 239);\n"
                                    "border-radius: 8px;")
        self.widget_7.setObjectName("widget_7")
        self.txtObservacionFactura = QtWidgets.QLineEdit(parent=self.widget_7)
        self.txtObservacionFactura.setEnabled(True)
        self.txtObservacionFactura.setGeometry(QtCore.QRect(10, 40, 481, 24))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        self.txtObservacionFactura.setFont(font)
        self.txtObservacionFactura.setStyleSheet("background-color: rgb(239, 239, 239);\n"
                                                 "border-radius:4px;")
        self.txtObservacionFactura.setObjectName("txtObservacionFactura")
        self.label_25 = QtWidgets.QLabel(parent=self.widget_7)
        self.label_25.setGeometry(QtCore.QRect(10, 10, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.frame.raise_()
        self.widget_4.raise_()
        self.widget_3.raise_()
        self.widget_2.raise_()
        self.btnLimpiar.raise_()
        self.btnRegistrar.raise_()
        self.widget_5.raise_()
        self.txtLogo.raise_()
        self.widget_6.raise_()
        self.widget_7.raise_()
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Ancho de columnas de tablas
        self.tblHabitacion.setColumnWidth(0, 60) # ID
        self.tblHabitacion.setColumnWidth(1, 100) #Tipo
        self.tblHabitacion.setColumnWidth(2, 80) #Piso
        self.tblHabitacion.setColumnWidth(3, 80) # tamaño
        self.tblHabitacion.setColumnWidth(4, 170)# descripcion
        self.tblHabitacion.setColumnWidth(5, 90) # camas
        self.tblHabitacion.setColumnWidth(6, 110) # baño
        self.tblHabitacion.setColumnWidth(7, 100)  # precio

        self.tblHabitacion.verticalHeader().setVisible(False)
        self.llenaTblHabitacion(False,"")
        self.tblHabitacion.selectionModel().selectionChanged.connect(self.selRegistroTabla)
        self.txtBuscarHabitacion.textChanged.connect(self.busquedaHabi)

        fecha_especifica = QDate(2000, 1, 1)
        self.dtFechaEntrada.setDate(fecha_especifica)
        self.dtFechaEntrada.setCalendarPopup(True)
        fecha_especifica = QDate(2000, 1, 1)
        self.dtFechaSalida.setDate(fecha_especifica)
        self.dtFechaSalida.setCalendarPopup(True)
        self.btnNuevoCliente.clicked.connect(self.openGestionClientes)
        self.filtro_busqueda = None
        self.cadBuscar = ""
        self.llenaCmbClientes(False, "")
        self.txtBuscarCliente.textChanged.connect(self.busqueda)

        self.cmbServiciosExtra.currentIndexChanged.connect(self.actualizaPrecioServicioExtra)
        self.txtCantidadServicioExtra.setEnabled(False)
        fecha_hora_actual = QDateTime.currentDateTime()
        self.dtFechaEntrada.setDateTime(fecha_hora_actual)
        self.dtFechaSalida.setDateTime(fecha_hora_actual.addDays(1))
        self.dtFechaSalida.dateTimeChanged.connect(self.actualizaNDiasHospedar)
        self.dtFechaEntrada.dateTimeChanged.connect(self.actualizaNDiasHospedar)
        self.txtNDiasHospedar.textChanged.connect(self.calculaFechaSalida)
        fecha_actual = QDateTime.currentDateTime()
        self.dtFechaEntrada.setMinimumDateTime(fecha_actual)
        self.dtFechaSalida.setMinimumDateTime(fecha_actual)

        self.tblHabitacion.selectionModel().selectionChanged.connect(self.calculaMontoTotal)
        self.txtPrecioServicioExtra.textChanged.connect(self.calculaMontoTotal)
        self.txtCantidadServicioExtra.textChanged.connect(self.calculaMontoTotal)
        self.btnLimpiar.clicked.connect(self.limpia)
        self.dni_clienteSele = None
        self.dni_empleadoSele= self.id_user
        print(self.dni_empleadoSele)
        self.cmbServiciosExtra.currentIndexChanged.connect(self.actualizaCantServicio)
        self.txtCantidadServicioExtra.textChanged.connect(self.actualizaCantServicio2)
        self.btnRegistrar.clicked.connect(self.registraReserva)
        self.cmbClientes.currentIndexChanged.connect(self.obtenerDNICliente)
        self.btnRegresar.clicked.connect(self.open_regresar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tblHabitacion.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nueva fila"))
        item = self.tblHabitacion.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tblHabitacion.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tipo"))
        item = self.tblHabitacion.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "N° piso"))
        item = self.tblHabitacion.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Tamaño"))
        item = self.tblHabitacion.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Descripción"))
        item = self.tblHabitacion.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Camas"))
        item = self.tblHabitacion.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Tipo Baño"))
        item = self.tblHabitacion.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Precio"))
        self.txtBuscarHabitacion.setPlaceholderText(_translate("MainWindow", "Buscar habitación por campos"))
        self.label_5.setText(_translate("MainWindow", "SELECCIONE UNA HABITACIÓN"))
        self.label_22.setText(_translate("MainWindow", "seleccionada"))
        self.label_21.setText(_translate("MainWindow", "ID habitación"))
        self.btnNuevoCliente.setText(_translate("MainWindow", "NUEVO CLIENTE"))
        self.label_2.setText(_translate("MainWindow", "NOMBRE DEL CLIENTE"))
        self.txtBuscarCliente.setPlaceholderText(_translate("MainWindow", " Buscar cliente"))
        self.cmbClientes.setPlaceholderText(_translate("MainWindow", " Seleccione un cliente"))
        self.btnLimpiar.setText(_translate("MainWindow", "LIMPIAR DATOS"))
        self.btnRegistrar.setText(_translate("MainWindow", "REGISTRAR"))
        self.label_16.setText(_translate("MainWindow", "SERVICIOS EXTRA"))
        self.cmbServiciosExtra.setItemText(1, _translate("MainWindow", "Bebidas (Cóctel, vino, cerveza)"))
        self.cmbServiciosExtra.setItemText(2, _translate("MainWindow", "Comida Gourmet (Cena gourmet, plato especial)"))
        self.cmbServiciosExtra.setItemText(3, _translate("MainWindow", "Decoración Especial para Eventos (Floral,temática)"))
        self.cmbServiciosExtra.setItemText(4, _translate("MainWindow", "Masaje Relajante (Piedras calientes, aromaterapia)"))
        self.cmbServiciosExtra.setItemText(5, _translate("MainWindow", "Cuidado de Mascotas (Cuidado completo)"))
        self.label_14.setText(_translate("MainWindow", "Cantidad de veces de servicio"))
        self.label_17.setText(_translate("MainWindow", "Precio en S/"))
        self.rbtTarjeta.setText(_translate("MainWindow", "Tarjeta de debito/credito"))
        self.rbtYape.setText(_translate("MainWindow", "Yape/Plin"))
        self.rbtEfectivo.setText(_translate("MainWindow", "Efectivo"))
        self.label_15.setText(_translate("MainWindow", "MÉTODOS DE PAGO:"))
        self.label_13.setText(_translate("MainWindow", "MONTO TOTAL A PAGAR EN S/"))
        self.rbtPendiente.setText(_translate("MainWindow", "PENDIENTE"))
        self.rbtCancelado.setText(_translate("MainWindow", "CANCELADO"))
        self.label_18.setText(_translate("MainWindow", "ESTADO DE PAGO:"))
        self.label_3.setText(_translate("MainWindow", "RESERVA DE HABITACIONES"))
        self.btnRegresar.setText(_translate("MainWindow", "REGRESAR"))
        self.label_12.setText(_translate("MainWindow", "Fecha/hora de salida"))
        self.label_10.setText(_translate("MainWindow", "N° de dias a hospedar"))
        self.label_11.setText(_translate("MainWindow", "Fecha/hora de entrada"))
        self.label_25.setText(_translate("MainWindow", "OBSERVACIÓN"))

    def llenaTblHabitacion(self, filtro_busqueda, cadBuscar):
        try:
            # Construir la consulta SQL para obtener habitaciones disponibles
            sql = "SELECT * FROM Habitacion WHERE Estado = 'Disponible'"  # 1

            # Si se aplica un filtro de búsqueda, añadir condiciones a la consulta
            if filtro_busqueda:
                sql += (f" AND (Tipo LIKE '{cadBuscar}%'"
                        f" OR Descripcion LIKE '{cadBuscar}%'"
                        f" OR Tipo_baño LIKE '{cadBuscar}%' "
                        f" OR CAST(Piso AS NVARCHAR) LIKE '{cadBuscar}%'"
                        f" OR CAST(Tamaño AS NVARCHAR) LIKE '{cadBuscar}%'"
                        f" OR CAST(N_camas AS NVARCHAR) LIKE '{cadBuscar}%'"
                        f" OR CAST(Precio AS NVARCHAR) LIKE '{cadBuscar}%')")  # 1

            # Ejecutar la consulta SQL y obtener la lista de habitaciones
            list_habitacion = conexion.resultadoSQL(sql)  # 1

            # Limpiar la tabla antes de llenarla
            self.tblHabitacion.setRowCount(0)  # 1

            # Obtener el número de filas en la lista de habitaciones
            num_rows = len(list_habitacion)  # 1
            self.tblHabitacion.setRowCount(num_rows)  # 1

            # Configurar la fuente para los elementos de la tabla
            font3 = QtGui.QFont()
            font3.setFamily("Segoe UI")
            font3.setPointSize(11)

            # Rellenar la tabla con los datos de las habitaciones
            for row_index, row_data in enumerate(list_habitacion):  # O(n)
                for col_index, col_data in enumerate(row_data):  # O(m)
                    item = QTableWidgetItem(str(col_data))  # 1
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # 1
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)  # 1
                    item.setFont(font3)  # 1
                    self.tblHabitacion.setItem(row_index, col_index, item)  # 1

        except Exception as e:
            QMessageBox.warning(None, "Error", str(e))  # 1
    # Complejidad total: O(n * m)

    def busquedaHabi(self):
        try:
            # Obtener el texto de búsqueda y eliminar espacios en blanco
            cadBuscar = self.txtBuscarHabitacion.text().strip()  # 1

            # Si no hay texto de búsqueda, llenar la tabla con todas las habitaciones disponibles
            if cadBuscar == "":
                self.llenaTblHabitacion(False, "")  # 1
            else:
                # Llenar la tabla con las habitaciones que coinciden con el texto de búsqueda
                self.llenaTblHabitacion(True, cadBuscar)  # 1

        except Exception as e:
            QMessageBox.warning(None, "Error", str(e))  # 1
    # Complejidad total: O(1)

    def llenaCmbClientes(self, filtro_busqueda, cadBuscar):
        # Construye la consulta SQL para obtener clientes
        sql = ("SELECT DNI_Cliente, Nombres || ' ' || Apellidos AS nombre_completo "
               "FROM Cliente ")

        # Añade un filtro de búsqueda si es necesario
        if filtro_busqueda:
            sql += (f" WHERE Nombres LIKE '{cadBuscar}%'"
                    f" OR Apellidos LIKE '{cadBuscar}%'")  # 1

        try:
            list_cliente = conexion.resultadoSQL(sql)  # 1
            self.cmbClientes.clear()  # 1
            self.cmbClientes.addItem("")  # 1

            # Verifica si solo hay un cliente y lo añade
            if len(list_cliente) == 1:
                dni_cliente = list_cliente[0][0]  # 1
                nombre_completo = list_cliente[0][1]  # 1
                self.cmbClientes.addItem(nombre_completo, dni_cliente)  # 1
                self.cmbClientes.setCurrentText(nombre_completo)  # 1
            else:
                # Añade todos los clientes a la lista
                for cliente in list_cliente:  # n
                    dni_cliente = cliente[0]  # 1
                    nombre_completo = cliente[1]  # 1
                    self.cmbClientes.addItem(nombre_completo, dni_cliente)  # 1
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")  # 1
    # Complejidad total: O(n)

    def obtenerDNICliente(self):
        try:
            indice_seleccionado = self.cmbClientes.currentIndex()  # 1

            if indice_seleccionado > 0:  # 1
                dni_cliente = self.cmbClientes.itemData(indice_seleccionado)  # 1
                if dni_cliente:  # 1
                    print(f"DNI del cliente seleccionado: {dni_cliente}")  # 1
                    self.dni_clienteSele = dni_cliente  # 1
                else:
                    pass  # 1
                    # print("No hay DNI asociado al cliente seleccionado.")
            else:
                pass  # 1
                # print("No se ha seleccionado un cliente válido.")
        except Exception as e:
            print(f"Error al obtener el DNI del cliente: {e}")  # 1
    # Complejidad total: O(1)

    def selRegistroTabla(self):
        if self.tblHabitacion.selectedItems():
            selected_row = self.tblHabitacion.currentRow()
            id_habitacion = self.tblHabitacion.item(selected_row, 0).text()
            tipo_habitacion = self.tblHabitacion.item(selected_row, 1).text()
            self.txtIdHabitacionSele.setText(id_habitacion)

            imagen_map = {
                    "Simple": "sencilla.jpeg",
                    "Suite": "suite.jpeg",
                    "Doble": "doble.jpeg",
                    "Familiar": "familiar.jpeg",
                    "Matrimonial": "matrimonial.jpeg"
            }


            imagen_archivo = imagen_map.get(tipo_habitacion, "default.jpeg")
            pixmap = QtGui.QPixmap(resource_path(imagen_archivo))
            self.txtImagenHabitacion.setPixmap(pixmap)

    def busqueda(self):
        try:
            cadBuscar = self.txtBuscarCliente.text().strip()
            if cadBuscar=="":
                self.llenaCmbClientes(False,"")
            else:
                self.llenaCmbClientes(True, cadBuscar)
        except Exception as e:
            QMessageBox.warning(None, "Error", str(e))

    def actualizaPrecioServicioExtra(self):
        precios_servicios = {
            "Bebidas (Cóctel, vino, cerveza)": 25.00,
            "Comida Gourmet (Cena gourmet, plato especial)": 30.00,
            "Decoración Especial para Eventos (Floral,temática)": 40.00,
            "Masaje Relajante (Piedras calientes, aromaterapia)": 35.00,
            "Cuidado de Mascotas (Cuidado completo)": 30.00
        }
        servicio_seleccionado = self.cmbServiciosExtra.currentText()

        if servicio_seleccionado in precios_servicios:
            precio = precios_servicios[servicio_seleccionado]
            self.txtPrecioServicioExtra.setText(f"{precio:.2f}")
            self.txtCantidadServicioExtra.setEnabled(True)
        else:
            self.txtPrecioServicioExtra.clear()
            self.txtCantidadServicioExtra.setEnabled(False)

    def calculaFechaSalida(self):
        try:
            texto_dias = self.txtNDiasHospedar.text().strip()
            if texto_dias:
                n_dias = int(texto_dias)
                if n_dias < 1:
                    self.txtNDiasHospedar.setText("1")
                    self.mostrarMensajeError("El número de días debe ser al menos 1.")
                    return
            else:
                n_dias = 1
            fecha_entrada = self.dtFechaEntrada.dateTime()
            fecha_salida = fecha_entrada.addDays(n_dias)
            self.dtFechaSalida.setDateTime(fecha_salida)

        except ValueError:
            self.mostrarMensajeError("El número de días debe ser un valor entero.")

    def actualizaNDiasHospedar(self):
        try:
            fecha_entrada = self.dtFechaEntrada.dateTime()
            fecha_salida = self.dtFechaSalida.dateTime()
            if fecha_salida < fecha_entrada:
                if self.txtNDiasHospedar.text():
                    self.mostrarMensajeError("La fecha de salida debe ser posterior a la fecha de entrada.")
                self.dtFechaSalida.setDateTime(fecha_entrada.addDays(1))
                return
            diferencia_dias = fecha_entrada.daysTo(fecha_salida)
            if diferencia_dias >= 1:
                self.txtNDiasHospedar.setText(str(diferencia_dias))
            self.calculaMontoTotal()

        except ValueError as e:
            self.mostrarMensajeError(f"Error: {e}")

    def calculaMontoTotal(self):
        try:
            # Verifica si hay una fila seleccionada
            selected_row = self.tblHabitacion.currentRow()
            if selected_row == -1:
                # No hay fila seleccionada, así que simplemente vacía el campo de monto total
                self.txtMontoTotal.clear()
                return

            # Obtiene el precio de la habitación y verifica si es numérico
            precio_item = self.tblHabitacion.item(selected_row, 7)
            if precio_item is None or not precio_item.text().replace('.', '', 1).isdigit():
                # El precio no es válido, así que vacía el campo de monto total
                self.txtMontoTotal.clear()
                return

            precio_habitacion = float(precio_item.text())

            # Obtiene la cantidad de servicios extra y el precio del servicio extra
            cantidad_servicio_extra = int(self.txtCantidadServicioExtra.text() or 1)
            precio_servicio_extra = float(self.txtPrecioServicioExtra.text() or 0)

            # Calcula el monto de la habitación
            fecha_entrada = self.dtFechaEntrada.dateTime()
            fecha_salida = self.dtFechaSalida.dateTime()
            diferencia_dias = fecha_entrada.daysTo(fecha_salida)
            if diferencia_dias < 1:
                diferencia_dias = 1
            monto_habitacion = precio_habitacion * diferencia_dias

            # Calcula el monto de los servicios extra
            monto_servicios_extra = precio_servicio_extra * cantidad_servicio_extra

            # Calcula el monto total
            monto_total = monto_habitacion + monto_servicios_extra

            # Muestra el monto total en el campo correspondiente
            self.txtMontoTotal.setText(f"{monto_total:.2f}")

        except ValueError as e:
            # Si ocurre una excepción, vacía el campo de monto total
            self.txtMontoTotal.clear()

    def mostrarMensajeError(self, mensaje):
        QMessageBox.critical(self, "Error", mensaje, QMessageBox.StandardButton.Ok)

    def mostrarMensajeInfo(self, mensaje):
        QMessageBox.information(self, "Información", mensaje, QMessageBox.StandardButton.Ok)

    def limpia(self):
        self.txtNDiasHospedar.clear()
        self.txtCantidadServicioExtra.clear()
        self.txtPrecioServicioExtra.clear()
        self.txtMontoTotal.clear()
        self.txtObservacionFactura.clear()
        self.txtMontoTotal.clear()
        self.txtIdHabitacionSele.clear()
        self.dtFechaEntrada.setDateTime(QDateTime.currentDateTime())  # Fecha y hora actual
        self.dtFechaSalida.setDateTime(QDateTime.currentDateTime().addDays(1))  # Fecha y hora actual

        self.cmbClientes.setCurrentIndex(0)
        self.cmbServiciosExtra.setCurrentIndex(0)

        self.rbtEfectivo.setAutoExclusive(False)
        self.rbtEfectivo.setChecked(False)
        self.rbtYape.setAutoExclusive(False)
        self.rbtYape.setChecked(False)
        self.rbtTarjeta.setAutoExclusive(False)
        self.rbtTarjeta.setChecked(False)
        # Volver a activar la exclusividad para el comportamiento normal
        self.rbtEfectivo.setAutoExclusive(True)
        self.rbtYape.setAutoExclusive(True)
        self.rbtTarjeta.setAutoExclusive(True)

        # Limpiar radio buttons de estado de pago dentro del QButtonGroup
        self.buttonGroup.setExclusive(False)
        for button in self.buttonGroup.buttons():
            button.setChecked(False)
        self.buttonGroup.setExclusive(True)

        for button in self.buttonGroup.buttons():
            button.update()

        self.tblHabitacion.clearSelection()
        self.txtImagenHabitacion.clear()
        self.txtMontoTotal.setText("")

    def valida(self):
        mensajes = ""
        if self.cmbClientes.currentText().strip() == "":
            mensajes +="Debe seleccionar un cliente\n"
        if self.txtIdHabitacionSele.text().strip() == "":
            mensajes += "Debe seleccionar unn habitación\n"
        if not (self.rbtEfectivo.isChecked() or self.rbtYape.isChecked() or self.rbtTarjeta.isChecked()):
            mensajes +="Debe seleccionar un método de pago\n"
        if not (self.rbtPendiente.isChecked() or self.rbtCancelado.isChecked() ):
            mensajes +="Debe seleccionar un estado de pago\n"
        if not self.txtObservacionFactura.text().strip():
            mensajes +="Debe ingresar una observación en la factura\n"
        if mensajes =="":
            return True
        else:
            self.mostrarMensajeError(mensajes)

    def actualizaCantServicio(self):
        if not self.cmbServiciosExtra.currentText().strip() == "" and len(self.txtCantidadServicioExtra.text().strip())<1:
            textCan = self.txtCantidadServicioExtra.text().strip()
            if textCan:
                cant = int(textCan)
                if cant < 1:
                    self.txtCantidadServicioExtra.setText("1")
        else:
            self.txtCantidadServicioExtra.setText("")

    def actualizaCantServicio2(self):
        if self.txtCantidadServicioExtra.text().strip() =="0":
            self.txtCantidadServicioExtra.setText("1")

    def registraReserva(self):
        if self.valida():
            id_reserva = self.id_siguiente("Reserva", "Reserva_ID")
            if id_reserva is None:
                self.mostrarMensajeError("No se pudo obtener el ID de la reserva.")
                return
            dni_empleado = self.dni_empleadoSele
            dni_cliente = self.dni_clienteSele
            id_habitacion = self.txtIdHabitacionSele.text().strip()
            fecha_entrada = self.dtFechaEntrada.dateTime().toPyDateTime().strftime('%Y-%m-%dT%H:%M:%S')
            fecha_salida = self.dtFechaSalida.dateTime().toPyDateTime().strftime('%Y-%m-%dT%H:%M:%S')
            estado_reserva = "Cancelado" if self.rbtCancelado.isChecked() else \
                "Pendiente"
            sql_reserva = f"""
            INSERT INTO Reserva (Reserva_ID, DNI_Empleado, DNI_Cliente, Habitacion_ID, Fech_Entrada, Fech_Salida, Estado)
            VALUES ({id_reserva}, {dni_empleado}, {dni_cliente}, {id_habitacion}, '{fecha_entrada}', '{fecha_salida}', '{estado_reserva}')
            """
            try:
                #print(sql_reserva)
                conexion.ejecutaSQL(sql_reserva)
            except Exception as e:
                self.mostrarMensajeError(f"Error al registrar la reserva: {e}")
                return
            # Registrar servicios extra si se han seleccionado
            servicio_extra = self.cmbServiciosExtra.currentText().strip()
            if servicio_extra:
                id_servicioExtra = self.id_siguiente("ServiciosExtra", "ServiciosExtra_ID")
                precio_servicio_extra = float(self.txtPrecioServicioExtra.text().strip())
                estado_servicio_extra = "Registrado"  # Puedes ajustar esto según tus necesidades

                sql_servicios_extra = f"""
                INSERT INTO ServiciosExtra (Reserva_ID, Descripcion, Precio, Estado)
                VALUES ({id_reserva}, '{servicio_extra}', {precio_servicio_extra}, '{estado_servicio_extra}')
                """
                try:
                    #print(sql_servicios_extra)
                    conexion.ejecutaSQL(sql_servicios_extra)
                except Exception as e:
                    self.mostrarMensajeError(f"Error al registrar los servicios extra: {e}")
            # Registrar la factura
            id_factura = self.id_siguiente("Factura", "Factura_ID")
            monto_total = float(self.txtMontoTotal.text().strip())
            metodo_pago = "Efectivo" if self.rbtEfectivo.isChecked() else \
                "Yape" if self.rbtYape.isChecked() else \
                    "Tarjeta"
            observacion = self.txtObservacionFactura.text().strip()

            sql_factura = f"""
            INSERT INTO Factura (Factura_ID, Monto, Reserva_ID, Fecha, Metodo_Pago, Observacion)
            VALUES ({id_factura}, {monto_total}, {id_reserva}, '{fecha_entrada}', '{metodo_pago}', '{observacion}')
            """
            try:
                #print(sql_factura)
                conexion.ejecutaSQL(sql_factura)
            except Exception as e:
                self.mostrarMensajeError(f"Error al registrar la factura: {e}")
            # Registrar en el historial de cambios de reserva
            id_cambio = self.id_siguiente("HistorialCambiosReserva", "Cambio_ID")
            descripcion_cambio = "Reserva creada"
            sql_historial = f"""
            INSERT INTO HistorialCambiosReserva (Cambio_ID, Reserva_ID, FechaCambio, Descripcion)
            VALUES ({id_cambio}, {id_reserva}, '{fecha_entrada}', '{descripcion_cambio}')
            """
            try:
                #print(sql_historial)
                conexion.ejecutaSQL(sql_historial)
            except Exception as e:
                self.mostrarMensajeError(f"Error al registrar el historial de cambios: {e}")
            self.limpia()
            self.mostrarMensajeInfo("Reserva registrada exitosamente.")

    def id_siguiente(self, nombTbl, nombCamp):
        try:
            sql_count = f"SELECT COUNT({nombCamp}) AS total FROM {nombTbl}"
            result_count = conexion.resultadoSQL(sql_count)

            if result_count:
                countReg = result_count[0][0]

                if countReg > 0:
                    sql_max = f"SELECT MAX({nombCamp}) AS idMax FROM {nombTbl}"
                    result_max = conexion.resultadoSQL(sql_max)

                    if result_max:
                        max_id = result_max[0][0]  # Extraer el valor del máximo ID
                        return max_id + 1  # Retornar el siguiente ID
                else:
                    return 1
            else:
                return 1
        except Exception as e:
            QMessageBox.warning(None, "Error", str(e))
            return None

    def open_regresar(self):
        self.close()
        self.ventana_prin.show()

    def openGestionClientes(self):
        #se pasa el id usuario y la ventana
        self.gesClie = Ui_GestClie(self.id_user, self)
        self.gesClie.show()
        self.close()

    def keyPressEvent(self, event):
        """Detecta si se presionó la tecla Escape y regresa a la ventana principal."""
        if event.key() == Qt.Key.Key_Escape:
            self.open_regresar()


    def __init__(self, dato,ventana_principal):
        super().__init__()
        self.id_user = dato
        self.ventana_prin = ventana_principal
        self.setupUi(self)

import sys
class MainWindow(QMainWindow, Ui_ReserHabi):
        def __init__(self):
                super().__init__()
                self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
