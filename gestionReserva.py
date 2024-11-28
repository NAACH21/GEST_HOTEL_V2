from datetime import datetime
from types import LambdaType
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QDateTime, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QVBoxLayout, QAbstractItemView, QTableWidgetItem
import conexion
from  met_pago import PaymentWindow
from sel_habitacion import HabitacionWindow
from images import resource_path

class Ui_GestReser(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1259, 683)
        Form.setGeometry(
            (Form.screen().geometry().width() - Form.geometry().width()) // 2,
            (Form.screen().geometry().height() - Form.geometry().height()) // 2,
            Form.geometry().width(),
            Form.geometry().height()
        )
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1481, 81))
        self.label_3.setMouseTracking(False)
        self.label_3.setStyleSheet("background-color: rgba(24, 71, 113,0.9);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(430, 10, 561, 61))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(30)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(189, 103, 1291, 621))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setObjectName("frame")
        self.label_6 = QtWidgets.QLabel(parent=self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 0, 1271, 601))
        self.label_6.setStyleSheet("background-color: rgba(255, 255, 255,0.9);\n"
                                   "border-radius:20px;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.frame)
        self.label_7.setGeometry(QtCore.QRect(10, 0, 1271, 551))
        self.label_7.setStyleSheet("background-color: rgba(255, 255, 255,0.9);\n"
                                   "border-radius:20px;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=Form)
        self.label_8.setGeometry(QtCore.QRect(10, 100, 181, 601))
        self.label_8.setStyleSheet("background-color: rgba(24, 71, 113,0.9);\n"
                                   "border-radius: 20px;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.bnt_Lis_reserva = QtWidgets.QPushButton(parent=Form)
        self.bnt_Lis_reserva.setGeometry(QtCore.QRect(30, 133, 141, 51))
        font = QtGui.QFont()
        font.setBold(True)
        self.bnt_Lis_reserva.setFont(font)
        self.bnt_Lis_reserva.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bnt_Lis_reserva.setStyleSheet("QPushButton {\n"
                                           "    border-radius: 20px;\n"
                                           "    background-color: rgb(255, 255, 255);\n"
                                           "    color:  rgb(24, 71, 113);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(24, 71, 113);\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    border: 1px solid rgb(255, 255, 255);\n"
                                           "}")
        self.bnt_Lis_reserva.setObjectName("bnt_Lis_reserva")
        self.bnt_mod_reserv = QtWidgets.QPushButton(parent=Form)
        self.bnt_mod_reserv.setGeometry(QtCore.QRect(30, 210, 141, 51))
        font = QtGui.QFont()
        font.setBold(True)
        self.bnt_mod_reserv.setFont(font)
        self.bnt_mod_reserv.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bnt_mod_reserv.setStyleSheet("QPushButton {\n"
                                          "    border-radius: 20px;\n"
                                          "    background-color: rgb(255, 255, 255);\n"
                                          "    color:  rgb(24, 71, 113);\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "    background-color: rgb(24, 71, 113);\n"
                                          "    color: rgb(255, 255, 255);\n"
                                          "    border: 1px solid rgb(255, 255, 255);\n"
                                          "}")
        self.bnt_mod_reserv.setObjectName("bnt_mod_reserv")
        self.label_15 = QtWidgets.QLabel(parent=Form)
        self.label_15.setGeometry(QtCore.QRect(-10, 0, 1491, 81))
        self.label_15.setStyleSheet("background-color: rgba(24, 71, 113,0.9);\n"
                                    "border-radius: 20px;")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_32 = QtWidgets.QLabel(parent=Form)
        self.label_32.setGeometry(QtCore.QRect(0, 0, 1481, 781))
        self.label_32.setStyleSheet("\n"
                                    "background-color: rgb(247, 247, 247);")
        self.label_32.setText("")
        self.label_32.setScaledContents(True)
        self.label_32.setObjectName("label_32")
        self.txtLogo = QtWidgets.QLabel(parent=Form)
        self.txtLogo.setGeometry(QtCore.QRect(1162, 5, 91, 71))
        self.txtLogo.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.txtLogo.setMidLineWidth(-2)
        self.txtLogo.setText("")
        #self.txtLogo.setPixmap(QtGui.QPixmap("logo2.PNG"))
        self.txtLogo.setPixmap(QtGui.QPixmap(resource_path("imagenes/logo2.PNG")))
        self.txtLogo.setScaledContents(True)
        self.txtLogo.setObjectName("txtLogo")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=Form)
        self.stackedWidget.setGeometry(QtCore.QRect(200, 100, 1061, 611))
        self.stackedWidget.setStyleSheet("background-color: rgba(255, 255, 255,0.0);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.ListadeReserva = QtWidgets.QWidget()
        self.ListadeReserva.setObjectName("ListadeReserva")
        self.bnt_BUSCAR = QtWidgets.QPushButton(parent=self.ListadeReserva)
        self.bnt_BUSCAR.setGeometry(QtCore.QRect(400, 10, 141, 47))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bnt_BUSCAR.setFont(font)
        self.bnt_BUSCAR.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bnt_BUSCAR.setStyleSheet("QPushButton {\n"
                                      "    border-radius: 20px;\n"
                                      "    background-color: rgb(24, 71, 113);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "    color: rgb(24, 71, 113);\n"
                                      "}")
        self.bnt_BUSCAR.setObjectName("bnt_BUSCAR")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.ListadeReserva)
        self.tableWidget.setGeometry(QtCore.QRect(60, 70, 821, 481))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: rgb(226, 245, 255);\n"
                                       "border-radius:8px;\n"
                                       "")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.txt_busc2 = QtWidgets.QLineEdit(parent=self.ListadeReserva)
        self.txt_busc2.setGeometry(QtCore.QRect(60, 20, 321, 34))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_busc2.setFont(font)
        self.txt_busc2.setStyleSheet("background-color: rgb(239, 239, 239);\n"
                                     "border-radius:8px;")
        self.txt_busc2.setObjectName("txt_busc2")
        self.stackedWidget.addWidget(self.ListadeReserva)
        self.modificar = QtWidgets.QWidget()
        self.modificar.setObjectName("modificar")
        self.label_10 = QtWidgets.QLabel(parent=self.modificar)
        self.label_10.setGeometry(QtCore.QRect(60, 30, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.txt_busc1 = QtWidgets.QLineEdit(parent=self.modificar)
        self.txt_busc1.setGeometry(QtCore.QRect(260, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_busc1.setFont(font)
        self.txt_busc1.setStyleSheet("")
        self.txt_busc1.setObjectName("txt_busc1")
        self.bntt_buscar = QtWidgets.QPushButton(parent=self.modificar)
        self.bntt_buscar.setGeometry(QtCore.QRect(400, 10, 141, 47))
        font = QtGui.QFont()
        font.setBold(True)
        self.bntt_buscar.setFont(font)
        self.bntt_buscar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bntt_buscar.setStyleSheet("QPushButton {\n"
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
        self.bntt_buscar.setObjectName("bntt_buscar")
        self.label_11 = QtWidgets.QLabel(parent=self.modificar)
        self.label_11.setGeometry(QtCore.QRect(60, 80, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.txt_usuario_reser = QtWidgets.QLineEdit(parent=self.modificar)
        self.txt_usuario_reser.setGeometry(QtCore.QRect(60, 130, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.txt_usuario_reser.setFont(font)
        self.txt_usuario_reser.setStyleSheet("QLineEdit{\n"
                                             "border:opx;\n"
                                             "border-bottom:2px solid rgb(24, 71, 113);\n"
                                             "}")
        self.txt_usuario_reser.setText("")
        self.txt_usuario_reser.setObjectName("txt_usuario_reser")
        self.label_12 = QtWidgets.QLabel(parent=self.modificar)
        self.label_12.setGeometry(QtCore.QRect(60, 170, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.txt_habitacion = QtWidgets.QLineEdit(parent=self.modificar)
        self.txt_habitacion.setEnabled(False)
        self.txt_habitacion.setGeometry(QtCore.QRect(60, 220, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        self.txt_habitacion.setFont(font)
        self.txt_habitacion.setStyleSheet("QLineEdit{\n"
                                          "border:opx;\n"
                                          "border-bottom:2px solid rgb(24, 71, 113);\n"
                                          "}")
        self.txt_habitacion.setObjectName("txt_habitacion")
        self.label_13 = QtWidgets.QLabel(parent=self.modificar)
        self.label_13.setGeometry(QtCore.QRect(60, 260, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.modificar)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 320, 281, 31))
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
                                      "border:opx;\n"
                                      "border-bottom:2px solid rgb(24, 71, 113);\n"
                                      "}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_14 = QtWidgets.QLabel(parent=self.modificar)
        self.label_14.setGeometry(QtCore.QRect(60, 360, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.modificar)
        self.lineEdit_4.setGeometry(QtCore.QRect(60, 410, 281, 31))
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
                                      "border:opx;\n"
                                      "border-bottom:2px solid rgb(24, 71, 113);\n"
                                      "}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.bntt_sel_habi = QtWidgets.QPushButton(parent=self.modificar)
        self.bntt_sel_habi.setGeometry(QtCore.QRect(350, 200, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.bntt_sel_habi.setFont(font)
        self.bntt_sel_habi.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bntt_sel_habi.setStyleSheet("QPushButton {\n"
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
        self.bntt_sel_habi.setObjectName("bntt_sel_habi")
        self.dateTimeingreso = QtWidgets.QDateTimeEdit(parent=self.modificar)
        self.dateTimeingreso.setGeometry(QtCore.QRect(60, 311, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.dateTimeingreso.setFont(font)
        self.dateTimeingreso.setObjectName("dateTimeingreso")
        self.dateTimeEditSalida = QtWidgets.QDateTimeEdit(parent=self.modificar)
        self.dateTimeEditSalida.setGeometry(QtCore.QRect(60, 410, 281, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateTimeEditSalida.setFont(font)
        self.dateTimeEditSalida.setObjectName("dateTimeEditSalida")
        self.label_16 = QtWidgets.QLabel(parent=self.modificar)
        self.label_16.setGeometry(QtCore.QRect(550, 80, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(parent=self.modificar)
        self.label_18.setGeometry(QtCore.QRect(550, 170, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.txt_met_PAgo = QtWidgets.QLineEdit(parent=self.modificar)
        self.txt_met_PAgo.setEnabled(True)
        self.txt_met_PAgo.setGeometry(QtCore.QRect(550, 220, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        self.txt_met_PAgo.setFont(font)
        self.txt_met_PAgo.setStyleSheet("QLineEdit{\n"
                                        "border:opx;\n"
                                        "border-bottom:2px solid rgb(24, 71, 113);\n"
                                        "}")
        self.txt_met_PAgo.setObjectName("txt_met_PAgo")
        self.txt_descripcion = QtWidgets.QLineEdit(parent=self.modificar)
        self.txt_descripcion.setGeometry(QtCore.QRect(550, 130, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        self.txt_descripcion.setFont(font)
        self.txt_descripcion.setStyleSheet("QLineEdit{\n"
                                           "border:opx;\n"
                                           "border-bottom:2px solid rgb(24, 71, 113);\n"
                                           "}")
        self.txt_descripcion.setObjectName("txt_descripcion")
        self.txt_met_PAgo_2 = QtWidgets.QLineEdit(parent=self.modificar)
        self.txt_met_PAgo_2.setEnabled(True)
        self.txt_met_PAgo_2.setGeometry(QtCore.QRect(550, 320, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        self.txt_met_PAgo_2.setFont(font)
        self.txt_met_PAgo_2.setStyleSheet("QLineEdit{\n"
                                          "border:opx;\n"
                                          "border-bottom:2px solid rgb(24, 71, 113);\n"
                                          "}")
        self.txt_met_PAgo_2.setObjectName("txt_met_PAgo_2")
        self.label_19 = QtWidgets.QLabel(parent=self.modificar)
        self.label_19.setGeometry(QtCore.QRect(550, 270, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.bntt_sle_MEt_Pago = QtWidgets.QPushButton(parent=self.modificar)
        self.bntt_sle_MEt_Pago.setGeometry(QtCore.QRect(840, 190, 141, 51))
        self.bntt_sle_MEt_Pago.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bntt_sle_MEt_Pago.setStyleSheet("QPushButton {\n"
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
        self.bntt_sle_MEt_Pago.setObjectName("bntt_sle_MEt_Pago")
        self.bntt_actualizar = QtWidgets.QPushButton(parent=self.modificar)
        self.bntt_actualizar.setGeometry(QtCore.QRect(550, 490, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.bntt_actualizar.setFont(font)
        self.bntt_actualizar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bntt_actualizar.setStyleSheet("QPushButton {\n"
                                           "    border-radius: 20px;\n"
                                           "    background-color: rgb(15, 121, 255);\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(10, 90, 200);\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "}")
        self.bntt_actualizar.setObjectName("bntt_actualizar")
        self.label_20 = QtWidgets.QLabel(parent=self.modificar)
        self.label_20.setGeometry(QtCore.QRect(550, 392, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        font.setBold(True)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.labelmontfin = QtWidgets.QLabel(parent=self.modificar)
        self.labelmontfin.setGeometry(QtCore.QRect(730, 390, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        self.labelmontfin.setFont(font)
        self.labelmontfin.setObjectName("labelmontfin")
        self.label_22 = QtWidgets.QLabel(parent=self.modificar)
        self.label_22.setGeometry(QtCore.QRect(60, 460, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.frame_2 = QtWidgets.QFrame(parent=self.modificar)
        self.frame_2.setGeometry(QtCore.QRect(50, 461, 391, 91))
        self.frame_2.setStyleSheet("border-radius: 15px;\n"
                                   "background-color: rgb(239, 239, 239);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setObjectName("frame_2")
        self.bntt_cancel = QtWidgets.QPushButton(parent=self.frame_2)
        self.bntt_cancel.setGeometry(QtCore.QRect(50, 30, 141, 51))
        font = QtGui.QFont()
        font.setBold(True)
        self.bntt_cancel.setFont(font)
        self.bntt_cancel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bntt_cancel.setStyleSheet("QPushButton {\n"
                                       "    border-radius: 20px;\n"
                                       "    background-color: rgb(68, 203, 99);\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(50, 150, 75);\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "}")
        self.bntt_cancel.setObjectName("bntt_cancel")
        self.btnPendiente = QtWidgets.QPushButton(parent=self.frame_2)
        self.btnPendiente.setGeometry(QtCore.QRect(210, 30, 141, 51))
        font = QtGui.QFont()
        font.setBold(True)
        self.btnPendiente.setFont(font)
        self.btnPendiente.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnPendiente.setStyleSheet("QPushButton {\n"
                                         "    border-radius: 20px;\n"
                                         "    background-color: rgb(236, 112, 99 );\n"
                                         "    color: rgb(255, 255, 255);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(200, 80, 70);\n"
                                         "    color: rgb(255, 255, 255);\n"
                                         "}")
        self.btnPendiente.setObjectName("btnPendiente")
        self.frame_2.raise_()
        self.label_10.raise_()
        self.txt_busc1.raise_()
        self.bntt_buscar.raise_()
        self.label_11.raise_()
        self.txt_usuario_reser.raise_()
        self.label_12.raise_()
        self.txt_habitacion.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.lineEdit_4.raise_()
        self.bntt_sel_habi.raise_()
        self.lineEdit_3.raise_()
        self.dateTimeingreso.raise_()
        self.dateTimeEditSalida.raise_()
        self.label_16.raise_()
        self.label_18.raise_()
        self.txt_met_PAgo.raise_()
        self.txt_descripcion.raise_()
        self.txt_met_PAgo_2.raise_()
        self.label_19.raise_()
        self.bntt_sle_MEt_Pago.raise_()
        self.bntt_actualizar.raise_()
        self.labelmontfin.raise_()
        self.label_20.raise_()
        self.label_22.raise_()
        self.stackedWidget.addWidget(self.modificar)
        self.bntt_regresar = QtWidgets.QPushButton(parent=Form)
        self.bntt_regresar.setGeometry(QtCore.QRect(20, 20, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.bntt_regresar.setFont(font)
        self.bntt_regresar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bntt_regresar.setStyleSheet("QPushButton {\n"
                                         "    border-radius: 10px;\n"
                                         "    background-color: rgb(239, 239, 239);\n"
                                         "    color:  rgb(24, 71, 113);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         "    color: rgb(24, 71, 113);\n"
                                         "}")
        self.bntt_regresar.setObjectName("bntt_regresar")
        self.label_32.raise_()
        self.label_8.raise_()
        self.frame.raise_()
        self.bnt_mod_reserv.raise_()
        self.bnt_Lis_reserva.raise_()
        self.label_3.raise_()
        self.label_15.raise_()
        self.label_5.raise_()
        self.txtLogo.raise_()
        self.stackedWidget.raise_()
        self.bntt_regresar.raise_()

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Ancho de columnas de tablas
        self.tableWidget.setColumnWidth(0, 110)  #codigo reserva
        self.tableWidget.setColumnWidth(1, 110) # DNI cliente
        self.tableWidget.setColumnWidth(2, 200) # fecha/hora entrada
        self.tableWidget.setColumnWidth(3, 200) # fecha/hora salida
        self.tableWidget.setColumnWidth(4, 150) #estado

        self.bntt_regresar.clicked.connect(self.open_regresar)
        self.bnt_mod_reserv.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.modificar))
        self.bnt_mod_reserv.clicked.connect(self.limpiar_fmr_reserv)
        self.bnt_Lis_reserva.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.ListadeReserva))
        self.bnt_mod_reserv.clicked.connect(self.ocultar_botones)
        self.bntt_cancel.clicked.connect(self.cancelar_reserva)
        self.btnPendiente.clicked.connect(self.reserva_pendiente)
        self.bntt_actualizar.clicked.connect(self.actualizar_reserva)
        self.bnt_Lis_reserva.clicked.connect(self.busquedaTabla)
        self.bntt_buscar.clicked.connect(self.buscar_reserva)
        self.bnt_BUSCAR.clicked.connect(self.busquedaTabla)
        self.bntt_sle_MEt_Pago.clicked.connect(self.abrir_ventana_metodo_pago)
        self.bntt_sel_habi.clicked.connect(self.abrir_ventana_habitacion)
        self.txt_busc2.textChanged.connect(self.busquedaTabla)
        self.txt_busc1.returnPressed.connect(self.buscar_reserva)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "GESTIÓN DE RESERVAS "))
        self.bnt_Lis_reserva.setText(_translate("Form", "LISTA DE RESERVAS"))
        self.bnt_mod_reserv.setText(_translate("Form", "MODIFICAR RESERVA"))
        self.bnt_BUSCAR.setText(_translate("Form", "BUSCAR"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "CÓDIGO RESERVA"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "DNI CLIENTE"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "FECHA / HORA ENTRADA"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "FECHA / HORA SALIDA"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "ESTADO"))
        self.label_10.setText(_translate("Form", "CÓDIGO DE RESERVA"))
        self.bntt_buscar.setText(_translate("Form", "BUSCAR"))
        self.label_11.setText(_translate("Form", "USUARIO DE LA RESERVA"))
        self.label_12.setText(_translate("Form", "HABITACIÓN"))
        self.label_13.setText(_translate("Form", "FECHA DE INGRESO"))
        self.label_14.setText(_translate("Form", "FECHA DE SALIDA"))
        self.bntt_sel_habi.setText(_translate("Form", "SELECCIONAR"))
        self.label_16.setText(_translate("Form", "SERVICIO EXTRA"))
        self.label_18.setText(_translate("Form", "METODO DE PAGO"))
        self.label_19.setText(_translate("Form", "MONTO"))
        self.bntt_sle_MEt_Pago.setText(_translate("Form", "SELECCIONAR"))
        self.bntt_actualizar.setText(_translate("Form", "ACTUALIZAR MODIFICACIÓN"))
        self.label_20.setText(_translate("Form", "MONTO TOTAL:  S/"))
        self.labelmontfin.setText(_translate("Form", "100.00"))
        self.label_22.setText(_translate("Form", "ACCIÓN RÁPIDA:      ACTUALIZAR ESTADO"))
        self.bntt_cancel.setText(_translate("Form", "CANCELADO"))
        self.btnPendiente.setText(_translate("Form", "PENDIENTE"))
        self.bntt_regresar.setText(_translate("Form", "REGRESAR"))

    def abrir_ventana_metodo_pago(self):
        if not hasattr(self, 'ventana_pago'):
            self.ventana_pago = PaymentWindow()
            self.ventana_pago.payment_selected.connect(
                self.actualizar_metodo_pago)
        self.ventana_pago.show()

    def actualizar_metodo_pago(self, metodo):
        self.txt_met_PAgo.setText(metodo)

    def abrir_ventana_habitacion(self):
        if not hasattr(self, 'ventana_habitacion'):
            self.ventana_habitacion = HabitacionWindow()
            self.ventana_habitacion.habitacion_seleccionada.connect(self.actualizar_habitacion)
        self.ventana_habitacion.show()

    def actualizar_habitacion(self, valor):
        self.txt_habitacion.setText(str(valor))

    def mostrar_tblreservas(self, filtro_busqueda, cadBuscar):
            try:
                    print("Iniciando función mostrar_tblreservas")
                    # Consulta base
                    sql = "SELECT Reserva_ID, DNI_Cliente, Fech_Entrada, Fech_Salida, Estado FROM reserva"

                    if filtro_busqueda:  # Si hay filtro de búsqueda
                            sql += (
                                    f" WHERE CAST(Reserva_ID AS VARCHAR) LIKE '{cadBuscar}%'"
                                    f" OR CAST(DNI_Cliente AS VARCHAR) LIKE '{cadBuscar}%'"
                                    f" OR FORMAT(Fech_Entrada, 'yyyy-MM-dd HH:mm:ss') LIKE '{cadBuscar}%'"
                                    f" OR FORMAT(Fech_Salida, 'yyyy-MM-dd HH:mm:ss') LIKE '{cadBuscar}%'"
                                    f" OR FORMAT(Fech_Entrada, 'HH:mm:ss') LIKE '{cadBuscar}%'"
                                    f" OR FORMAT(Fech_Salida, 'HH:mm:ss') LIKE '{cadBuscar}%'"
                                    f" OR Estado LIKE '{cadBuscar}%'"
                            )  # Agrega el filtro dinámico

                    datos = conexion.resultadoSQL(sql)  # Obtiene los resultados de la consulta
                    print("Datos obtenidos:", datos)

                    self.tableWidget.setRowCount(0)  # Limpia las filas existentes
                    self.tableWidget.setRowCount(len(datos))  # Establece el número de filas según los datos obtenidos

                    for row_index, row_data in enumerate(datos):  # Recorre los datos obtenidos
                            for col_index, col_data in enumerate(row_data):  # Recorre las columnas de cada fila
                                    # Manejo especial para columnas de tipo datetime
                                    if isinstance(col_data, (datetime,)):
                                            col_data = col_data.strftime(
                                                    '%Y-%m-%d %H:%M:%S')  # Convierte datetime a string
                                    item = QTableWidgetItem(str(col_data))
                                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # Centra los datos
                                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)  # Desactiva la edición
                                    self.tableWidget.setItem(row_index, col_index, item)  # Agrega el item a la tabla

                    print("Fin de la función mostrar_tblreservas")
            except Exception as e:
                    print("Error en mostrar_tblreservas:", str(e))
                    QMessageBox.critical(self, "Error", f"Ocurrió un error al mostrar las reservas: {e}")

    def busquedaTabla(self):
            try:
                    cadBuscar = self.txt_busc2.text().strip()  # Cadena de búsqueda
                    if cadBuscar == "":  # Si está vacío, muestra todos los registros
                            self.mostrar_tblreservas(False, "")  # Llama a la función con el filtro desactivado
                    else:  # Si hay un valor de búsqueda
                            self.mostrar_tblreservas(True, cadBuscar)  # Llama a la función con el filtro activado
            except Exception as e:
                    QMessageBox.warning(None, "Error", str(e))  # Manejo de errores

    def buscar_reserva(self):
            if not self.txt_busc1.text():
                QMessageBox.warning(self, "Advertencia", "El campo no puede estar vacío.")
                self.limpiar_fmr_reserv()
                self.ocultar_botones()
            else:
                #QMessageBox.information(self, "Correcto", "Reservacion encontrada.")
                try:
                        idReserva = self.txt_busc1.text().upper()
                        sql = f"SELECT * FROM reserva WHERE Reserva_ID = '{idReserva}'"
                        self.resultado = conexion.resultadoSQL(sql)
                        sql2 = f"SELECT * FROM Factura WHERE Reserva_ID = '{idReserva}'"
                        self.resultado2 = conexion.resultadoSQL(sql2)
                        sql1 = f"SELECT * FROM ServiciosExtra WHERE Reserva_ID = '{idReserva}'"
                        self.resultado1 = conexion.resultadoSQL(sql1)
                        if len(self.resultado) != 0:
                                self.idMod = self.resultado[0][0]
                                self.txt_usuario_reser.setText(str(self.resultado[0][2]))
                                self.txt_habitacion.setText(str(self.resultado[0][3]))
                                fecha_ingreso = QDateTime.fromString(self.resultado[0][4], "yyyy-MM-dd HH:mm:ss")
                                fecha_salida = QDateTime.fromString(self.resultado[0][5], "yyyy-MM-dd HH:mm:ss")
                                self.dateTimeingreso.setDateTime(fecha_ingreso)
                                self.dateTimeEditSalida.setDateTime(fecha_salida)
                                self.txt_met_PAgo.setText(str(self.resultado2[0][4]))
                                self.labelmontfin.setText(str(self.resultado2[0][1]))
                                self.mostrar_botones()
                                if len(self.resultado1)!=0:
                                    self.txt_descripcion.setText(str(self.resultado1[0][2]))
                                    self.txt_met_PAgo_2.setText(str(self.resultado1[0][3]))
                        else:
                            QMessageBox.information(None, "No existe la reserva", "Ingrese una reserva Valida")
                            self.limpiar_fmr_reserv()
                            self.ocultar_botones()

                except Exception as e:
                        print("Error en la función buscar_reserva:", e)

    def buscar_tabla_reserva(self):
        if not self.txt_busc2.text():
            QMessageBox.warning(self, "Advertencia", "El campo no puede estar vacío.")
        else:
            print("Iniciando función mostrar_tblreservas")
            idReserva = self.txt_busc2.text().upper()
            sql = f"SELECT * FROM reserva WHERE Reserva_ID = {idReserva}"
            datos = conexion.resultadoSQL(sql)
            print("Datos obtenidos:", datos)
            i = len(datos)
            self.tableWidget.setRowCount(i)
            tablerow = 0
            if i!=0:
                for row in datos:
                    print("Cargando fila:", row)
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[2])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[4])))
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[5])))
                    self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[6])))
                    tablerow += 1
                self.txt_busc2.setText("")
            else:
                QMessageBox.information(None, "No existe la reserva", "Ingrese una reserva Valida")
                self.mostrar_tblreservas()
                self.txt_busc2.setText("")
        print("Fin de la función mostrar_tblreservas")

    def mostrar_botones(self):
        self.bntt_cancel.setVisible(True)
        self.bntt_actualizar.setVisible(True)
        self.btnPendiente.setVisible(True)

    def ocultar_botones(self):
        self.bntt_cancel.setVisible(False)
        self.bntt_actualizar.setVisible(False)
        self.btnPendiente.setVisible(False)

    def open_regresar(self):
        self.close()
        self.ventana_prin.show()

    def cancelar_reserva(self):
        id_reserva = self.txt_busc1.text().upper()
        if id_reserva:
            sql = "UPDATE reserva SET estado = 'Cancelado' WHERE Reserva_ID = ?"
            params = (id_reserva,)
            conexion.ejecutarSQL(sql, params)
            QMessageBox.information(self, "Correcto", "Estado de Reserva actualizado correctamente")
            self.limpiar_fmr_reserv()
        else:
            QMessageBox.warning(self, "Advertencia", "El campo de búsqueda no puede estar vacío")

    def reserva_pendiente(self):
        id_reserva = self.txt_busc1.text().upper()
        if id_reserva:
            sql = "UPDATE reserva SET estado = 'Pendiente' WHERE Reserva_ID = ?"
            params = (id_reserva,)
            conexion.ejecutarSQL(sql, params)
            QMessageBox.information(self, "Correcto", "Estado de Reserva actualizado correctamente")
            self.limpiar_fmr_reserv()
        else:
            QMessageBox.warning(self, "Advertencia", "El campo de búsqueda no puede estar vacío")

    def actualizar_reserva(self):
        try:
            id_reserva = self.txt_busc1.text().upper()
            if id_reserva:
                sql = "UPDATE reserva SET Habitacion_ID = ?, Fech_Entrada = ?, Fech_Salida = ?, Estado = 'Pendiente' WHERE Reserva_ID = ?"
                params = (self.txt_habitacion.text(), self.dateTimeingreso.dateTime().toString("yyyy-MM-dd hh:mm:ss"),
                          self.dateTimeEditSalida.dateTime().toString("yyyy-MM-dd hh:mm:ss"), id_reserva)
                conexion.ejecutarSQL(sql, params)
                s = conexion.resultadoSQL("SELECT MAX(Cambio_ID) AS UltimoCambioID FROM HistorialCambiosReserva;")
                a = s[0][0] + 1
                sql2 = "INSERT INTO HistorialCambiosReserva (Cambio_ID, Reserva_ID, FechaCambio, Descripcion) "
                sql2 += " VALUES (?, ?, ?, ?);"
                fecha_cambio = QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss')
                params1 = (a, id_reserva, fecha_cambio, 'Actualización de reserva')
                conexion.ejecutarSQL(sql2, params1)
                QMessageBox.information(self, "Correcto", "Reserva actualizada correctamente")
                self.limpiar_fmr_reserv()
            else:
                QMessageBox.warning(self, "Advertencia", "El campo de búsqueda no puede estar vacío")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al actualizar la reserva: {e}")

    def limpiar_fmr_reserv(self):
        self.txt_habitacion.setText("")
        self.txt_usuario_reser.setText("")
        self.txt_descripcion.setText("")
        self.txt_met_PAgo.setText("")
        self.txt_met_PAgo_2.setText("")
        self.labelmontfin.setText("")

    def keyPressEvent(self, event):
        """Detecta si se presionó la tecla Escape y regresa a la ventana principal."""
        if event.key() == Qt.Key.Key_Escape:
            self.open_regresar()

    def __init__(self, dato, ventana_principal):
            super().__init__()
            self.id_user = dato
            self.ventana_prin = ventana_principal
            self.setupUi(self)
            self.mostrar_tblreservas(False, "")

import sys

if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = Ui_GestReser(1,QtWidgets.QWidget)
        window.show()
        sys.exit(app.exec())
