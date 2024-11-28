import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QRect, pyqtSignal, Qt, QCoreApplication, QMetaObject
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QWidget, QStatusBar

from images import resource_path

from gestionReserva import Ui_GestReser
from reservarHabitacion import Ui_ReserHabi
from gestionHabitacion import  Ui_GestHabi
from factura import Ui_Factura
from reportes import Ui_Reportes

import conexion

class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)

class Ui_Form(QtWidgets.QWidget):
    def open_reserva(self):
        self.reserva = Ui_ReserHabi(self.id_user,self)
        self.reserva.show()
        self.close()

    def openGestionReserva(self):
        #se pasa el id usuario y la ventana
        self.gesReserva = Ui_GestReser(self.id_user,self)
        self.gesReserva.show()
        self.close()

    def openGestionHabi(self):
        #se pasa el id usuario y la ventana
        self.gesHabi = Ui_GestHabi(self.id_user,self)
        self.gesHabi.show()
        self.close()

    def open_factura(self):
        self.reserva = Ui_Factura(self.id_user, self)
        self.reserva.show()
        self.close()

    def open_reportes(self):
        self.reportes = Ui_Reportes(self)
        self.reportes.show()
        self.close()

        """try:
            self.ventana_reportes = QtWidgets.QWidget()  # Crear un widget contenedor
            self.ui_reportes = Ui_Reportes()  # Instancia de la clase del reporte
            self.ui_reportes.setupUi(self.ventana_reportes)
            self.ventana_reportes.show()  # Muestra la ventana
            self.close()
        except Exception as e:
            QMessageBox.critical(None, "Error", f"No se pudo abrir la ventana de reportes: {e}")"""

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1919, 1035)
        MainWindow.setFixedSize(MainWindow.size())
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, -10, 1981, 1091))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, -2, 399, 1081))
        self.label_2.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, -30, 221, 201))
        self.label_3.setPixmap(QPixmap(resource_path(u"OIP.jpeg")))
        self.label_3.setScaledContents(True)


        self.Btn_Gest_reserv = ClickableLabel(self.centralwidget)
        self.Btn_Gest_reserv.setObjectName(u"Btn_Gest_reserv")
        self.Btn_Gest_reserv.setGeometry(QRect(0, 180, 399, 61))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setPointSize(11)
        self.Btn_Gest_reserv.setFont(font)
        self.Btn_Gest_reserv.setStyleSheet(u"QLabel {\n"
        "    background-color:  rgb(0, 85, 127); /* Color de fondo inicial */\n"
        "    border: none;\n"
        "	color:#e0e0e0;\n"
        "    padding: 5px;\n"
        "}\n"
        "\n"
        "QLabel:hover {\n"
        "    background-color: #e0e0e0; /* Color de fondo al pasar el cursor */\n"
        "	color:rgb(0, 85, 127);\n"
        "}\n"
        "\n"
        "QLabel:pressed {\n"
        "    background-color: #d0d0d0; /* Color de fondo al hacer clic */\n"
        "}\n"
        "")
        self.Btn_Gest_reserv.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.Btn_Mod_Reserv = ClickableLabel(self.centralwidget)
        self.Btn_Mod_Reserv.setObjectName(u"Btn_Mod_Reserv")
        self.Btn_Mod_Reserv.setGeometry(QRect(0, 240, 399, 61))
        self.Btn_Mod_Reserv.setFont(font)
        self.Btn_Mod_Reserv.setStyleSheet(u"QLabel {\n"
        "    background-color:  rgb(0, 85, 127); /* Color de fondo inicial */\n"
        "    border: none;\n"
        "	color:#e0e0e0;\n"
        "    padding: 5px;\n"
        "}\n"
        "\n"
        "QLabel:hover {\n"
        "    background-color: #e0e0e0; /* Color de fondo al pasar el cursor */\n"
        "	color:rgb(0, 85, 127);\n"
        "}\n"
        "\n"
        "QLabel:pressed {\n"
        "    background-color: #d0d0d0; /* Color de fondo al hacer clic */\n"
        "}\n"
        "")
        self.Btn_Mod_Reserv.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.Bnt_Gest_Habi = ClickableLabel(self.centralwidget)
        self.Bnt_Gest_Habi.setObjectName(u"Bnt_Gest_Habi")
        self.Bnt_Gest_Habi.setGeometry(QRect(0, 300, 399, 61))
        self.Bnt_Gest_Habi.setFont(font)
        self.Bnt_Gest_Habi.setStyleSheet(u"QLabel {\n"
        "    background-color:  rgb(0, 85, 127); /* Color de fondo inicial */\n"
        "    border: none;\n"
        "	color:#e0e0e0;\n"
        "    padding: 5px;\n"
        "}\n"
        "\n"
        "QLabel:hover {\n"
        "    background-color: #e0e0e0; /* Color de fondo al pasar el cursor */\n"
        "	color:rgb(0, 85, 127);\n"
        "}\n"
        "\n"
        "QLabel:pressed {\n"
        "    background-color: #d0d0d0; /* Color de fondo al hacer clic */\n"
        "}\n"
        "")
        self.Bnt_Gest_Habi.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Botón "Cerrar Sesión" (Bnt_Fact)
        self.Bnt_Fact = ClickableLabel(self.centralwidget)
        self.Bnt_Fact.setObjectName(u"Bnt_Fact")
        self.Bnt_Fact.setGeometry(QRect(0, 920, 399, 61))
        self.Bnt_Fact.setFont(font)
        self.Bnt_Fact.setStyleSheet("""
                    QLabel {
                        background-color: rgb(0, 85, 127);
                        border: none;
                        color: #e0e0e0;
                        padding: 5px;
                    }
                    QLabel:hover {
                        background-color: rgb(255, 56, 59);
                        color: #e0e0e0;
                    }
                    QLabel:pressed {
                        background-color: #d0d0d0;
                    }
                """)
        self.Bnt_Fact.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Bnt_Fact.setText("CERRAR SESIÓN")




        self.Bnt_Report_estd = ClickableLabel(self.centralwidget)
        self.Bnt_Report_estd.setObjectName(u"Bnt_Report_estd")
        self.Bnt_Report_estd.setGeometry(QRect(0, 360, 399, 61))
        self.Bnt_Report_estd.setFont(font)
        self.Bnt_Report_estd.setStyleSheet(u"QLabel {\n"
        "    background-color:  rgb(0, 85, 127); /* Color de fondo inicial */\n"
        "    border: none;\n"
        "	color:#e0e0e0;\n"
        "    padding: 5px;\n"
        "}\n"
        "\n"
        "QLabel:hover {\n"
        "    background-color: #e0e0e0; /* Color de fondo al pasar el cursor */\n"
        "	color:rgb(0, 85, 127);\n"
        "}\n"
        "\n"
        "QLabel:pressed {\n"
        "    background-color: #d0d0d0; /* Color de fondo al hacer clic */\n"
        "}\n"
        "")
        self.Bnt_Report_estd.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.Bnt_Sunat = ClickableLabel(self.centralwidget)
        self.Bnt_Sunat.setObjectName(u"Bnt_Sunat")
        self.Bnt_Sunat.setGeometry(QRect(0, 420, 399, 61))
        self.Bnt_Sunat.setFont(font)
        self.Bnt_Sunat.setStyleSheet(u"QLabel {\n"
        "    background-color:  rgb(0, 85, 127); /* Color de fondo inicial */\n"
        "    border: none;\n"
        "	color:#e0e0e0;\n"
        "    padding: 5px;\n"
        "}\n"
        "\n"
        "QLabel:hover {\n"
        "    background-color: #e0e0e0; /* Color de fondo al pasar el cursor */\n"
        "	color:rgb(0, 85, 127);\n"
        "}\n"
        "\n"
        "QLabel:pressed {\n"
        "    background-color: #d0d0d0; /* Color de fondo al hacer clic */\n"
        "}\n"
        "")
        self.Bnt_Sunat.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(390, 0, 1531, 81))
        self.label_4.setStyleSheet(u"background-color: rgb(24, 71, 113);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(430, 130, 481, 301))
        self.label_5.setStyleSheet(u"background-color: rgb(254, 254, 254);\n"
        "border: 3px solid #ccc;\n"
        "border-radius: 20px;\n"
        "padding: 20px;")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(930, 130, 481, 301))
        self.label_6.setStyleSheet(u"background-color: rgb(254, 254, 254);\n"
        "border: 3px solid #ccc;\n"
        "border-radius: 20px;\n"
        "padding: 20px;")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(1430, 130, 481, 301))
        self.label_7.setStyleSheet(u"background-color: rgb(254, 254, 254);\n"
        "border: 3px solid #ccc;\n"
        "border-radius: 20px;\n"
        "padding: 20px;")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(490, 220, 111, 111))
        self.label_8.setPixmap(QPixmap(resource_path(u"hotel-reception-bell-svgrepo-com.svg")))
        self.label_8.setScaledContents(True)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(990, 210, 111, 111))
        self.label_9.setPixmap(QPixmap(resource_path(u"bed-svgrepo-com.svg")))
        self.label_9.setScaledContents(True)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(1480, 220, 111, 111))
        self.label_10.setPixmap(QPixmap(resource_path(u"people-svgrepo-com.svg")))
        self.label_10.setScaledContents(True)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(660, 350, 181, 31))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(1130, 340, 221, 31))
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(1650, 330, 221, 31))
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Txt_cant_libre = QLabel(self.centralwidget)
        self.Txt_cant_libre.setObjectName(u"Txt_cant_libre")
        self.Txt_cant_libre.setGeometry(QRect(680, 180, 141, 181))
        font2 = QFont()
        font2.setFamilies([u"Yu Gothic UI Semibold"])
        font2.setPointSize(48)
        font2.setBold(True)
        self.Txt_cant_libre.setFont(font2)
        self.Txt_cant_libre.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Txt_cant_libre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Txt_cant_ocupado = QLabel(self.centralwidget)
        self.Txt_cant_ocupado.setObjectName(u"Txt_cant_ocupado")
        self.Txt_cant_ocupado.setGeometry(QRect(1170, 170, 141, 181))
        self.Txt_cant_ocupado.setFont(font2)
        self.Txt_cant_ocupado.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Txt_cant_ocupado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Txt_ocupants = QLabel(self.centralwidget)
        self.Txt_ocupants.setObjectName(u"Txt_ocupants")
        self.Txt_ocupants.setGeometry(QRect(1690, 160, 141, 181))
        self.Txt_ocupants.setFont(font2)
        self.Txt_ocupants.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Txt_ocupants.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(1840, 0, 71, 71))
        self.label_14.setPixmap(QPixmap(resource_path(u"user-circle-svgrepo-com.svg")))
        self.label_14.setScaledContents(True)
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(1640, 30, 49, 16))
        font3 = QFont()
        font3.setFamilies([u"Microsoft New Tai Lue"])
        font3.setPointSize(14)
        self.label_15.setFont(font3)
        self.labelNombre = QLabel(self.centralwidget)
        self.labelNombre.setObjectName(u"labelNombre")
        self.labelNombre.setGeometry(QRect(1690, 30, 141, 16))
        self.labelNombre.setFont(font3)

        self.label.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.Btn_Gest_reserv.raise_()
        self.Btn_Mod_Reserv.raise_()
        self.Bnt_Gest_Habi.raise_()
        self.Bnt_Fact.raise_()
        self.Bnt_Report_estd.raise_()
        self.Bnt_Sunat.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.Txt_cant_libre.raise_()
        self.Txt_cant_ocupado.raise_()
        self.Txt_ocupants.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.labelNombre.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        # Conectar el clic del botón "Cerrar Sesión" para salir de la aplicación
        self.Bnt_Fact.clicked.connect(self.close_application)
        self.Bnt_Gest_Habi.clicked.connect(self.openGestionHabi)
        self.Btn_Gest_reserv.clicked.connect(self.open_reserva)
        self.Btn_Mod_Reserv.clicked.connect(self.openGestionReserva)
        self.Bnt_Sunat.clicked.connect(self.open_factura)
        self.Bnt_Report_estd.clicked.connect(self.open_reportes)

    def close_application(self):
        QApplication.quit()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))

        # Consulta del usuario por DNI
        sql = "SELECT * FROM Empleado WHERE DNI_Empleado = ?"
        user = conexion.resultadoSQL(sql, (self.id_user,))
        if not user:
            print("Error: No se encontró el usuario.")
            ingreso = "Usuario no encontrado"
        else:
            ingreso = user[0][1] + " " + user[0][2]

        # Consulta de ocupantes
        sql1 = """ 
            SELECT COUNT(*) AS CantidadOcupantes
            FROM Reserva
            WHERE Estado = 'Confirmado';
        """
        ocupantes = conexion.resultadoSQL(sql1)
        ocupantes1 = ocupantes[0][0] if ocupantes else 0

        # Consulta de habitaciones ocupadas
        sql2 = """ 
            SELECT COUNT(*) AS HabitacionesOcupadas
            FROM Habitacion
            WHERE Estado = 'Ocupado';
        """
        ocupadas = conexion.resultadoSQL(sql2)
        ocupadas1 = ocupadas[0][0] if ocupadas else 0

        # Consulta de habitaciones libres
        sql3 = """ 
            SELECT COUNT(*) AS HabitacionesLibres
            FROM Habitacion
            WHERE Estado = 'Disponible';
        """
        libres = conexion.resultadoSQL(sql3)
        libres1 = libres[0][0]
        print(libres1)
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.Btn_Gest_reserv.setText(QCoreApplication.translate("MainWindow", u"GESTI\u00d3N DE RESERVA", None))
        self.Btn_Mod_Reserv.setText(QCoreApplication.translate("MainWindow", u"MODIFICACION DE RESERVA", None))
        self.Bnt_Gest_Habi.setText(QCoreApplication.translate("MainWindow", u"GESTI\u00d3N DE HABITACIONES", None))
        self.Bnt_Fact.setText(QCoreApplication.translate("MainWindow", u"CERRAR SESI\u00d3N", None))
        self.Bnt_Report_estd.setText(QCoreApplication.translate("MainWindow", u"REPORTES ESTAD\u00cdSTICOS", None))
        self.Bnt_Sunat.setText(QCoreApplication.translate("MainWindow", u"SUNAT", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_10.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u" HABITACIONES LIBRES", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u" HABITACIONES OCUPADAS", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"OCUPANTES", None))
        self.Txt_cant_libre.setText(QCoreApplication.translate("MainWindow", f"0{libres1}", None))
        self.Txt_cant_ocupado.setText(QCoreApplication.translate("MainWindow", f"0{ocupadas1}", None))
        self.Txt_ocupants.setText(QCoreApplication.translate("MainWindow", f"0{ocupantes1}", None))
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Hola,", None))
        self.labelNombre.setText(QCoreApplication.translate("MainWindow", ingreso, None))


    def keyPressEvent(self, event):
        """Detecta qué tecla se presionó y ejecuta la acción correspondiente."""
        if event.key() == Qt.Key.Key_1:  # Tecla '1' para la primera opción
            self.open_reserva()
        elif event.key() == Qt.Key.Key_2:  # Tecla '2' para la segunda opción
            self.openGestionReserva()
        elif event.key() == Qt.Key.Key_3:  # Tecla '3' para la tercera opción
            self.openGestionHabi()
        elif event.key() == Qt.Key.Key_4:  # Tecla '4' para la cuarta opción
            self.open_reportes()
        elif event.key() == Qt.Key.Key_5:  # Tecla '5' para la quinta opción
            self.open_factura()
        elif event.key() == Qt.Key.Key_Q:  # Tecla 'Q' para cerrar sesión
            self.close_application()

    import sys
    def __init__(self, dato):
        super().__init__()
        self.id_user = dato
        self.setupUi(self)

if __name__ == "__main__":


    app = QApplication(sys.argv)
    window = Ui_Form()
    window.show()
    sys.exit(app.exec())

