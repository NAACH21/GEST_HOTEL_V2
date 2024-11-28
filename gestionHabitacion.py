import re
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, QCoreApplication, QRect
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem, QFileDialog, QPushButton
import conexion
from images import resource_path

class Ui_GestHabi(QtWidgets.QWidget):
    def setupUi(self, gestionHabitacion):
        gestionHabitacion.setObjectName("gestionHabitacion")
        gestionHabitacion.resize(1259, 722)
        gestionHabitacion.setGeometry(
            (gestionHabitacion.screen().geometry().width() - gestionHabitacion.geometry().width()) // 2,
            (gestionHabitacion.screen().geometry().height() - gestionHabitacion.geometry().height()) // 2,
            gestionHabitacion.geometry().width(),
            gestionHabitacion.geometry().height()
        )
        self.widget = QtWidgets.QWidget(parent=gestionHabitacion)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1271, 771))
        self.widget.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.widget.setObjectName("widget")
        self.widget_3 = QtWidgets.QWidget(parent=self.widget)
        self.widget_3.setGeometry(QtCore.QRect(40, 100, 1171, 601))
        self.widget_3.setStyleSheet("border: 1px solid rgb(239, 239, 239);\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "border-radius: 8px;")
        self.widget_3.setObjectName("widget_3")
        self.cmbTipoHabitacion = QtWidgets.QComboBox(parent=self.widget_3)
        self.cmbTipoHabitacion.setGeometry(QtCore.QRect(40, 40, 221, 30))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(False)
        self.cmbTipoHabitacion.setFont(font)
        self.cmbTipoHabitacion.setStyleSheet("background-color: rgb(239, 239, 239);\n"
                                             "border-radius:4px;")
        self.cmbTipoHabitacion.setObjectName("cmbTipoHabitacion")
        self.cmbTipoHabitacion.addItem("")
        self.cmbTipoHabitacion.setItemText(0, "")
        self.cmbTipoHabitacion.addItem("")
        self.cmbTipoHabitacion.addItem("")
        self.cmbTipoHabitacion.addItem("")
        self.cmbTipoHabitacion.addItem("")
        self.cmbTipoHabitacion.addItem("")
        self.label_8 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(670, 20, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_4.setGeometry(QtCore.QRect(400, 20, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.cmbEstado = QtWidgets.QComboBox(parent=self.widget_3)
        self.cmbEstado.setGeometry(QtCore.QRect(660, 100, 191, 30))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(False)
        self.cmbEstado.setFont(font)
        self.cmbEstado.setStyleSheet("background-color: rgb(239, 239, 239);\n"
                                     "border-radius:4px;")
        self.cmbEstado.setObjectName("cmbEstado")
        self.cmbEstado.addItem("")
        self.cmbEstado.setItemText(0, "")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.txtBuscar = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtBuscar.setGeometry(QtCore.QRect(40, 250, 311, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtBuscar.setFont(font)
        self.txtBuscar.setStyleSheet("background-color: rgb(239, 239, 239);\n"
                                     "border-radius:8px;")
        self.txtBuscar.setObjectName("txtBuscar")
        self.label_5 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_5.setGeometry(QtCore.QRect(40, 80, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tblHabitacion = QtWidgets.QTableWidget(parent=self.widget_3)
        self.tblHabitacion.setGeometry(QtCore.QRect(42, 295, 981, 291))
        self.tblHabitacion.setMaximumSize(QtCore.QSize(96100, 16777215))
        self.tblHabitacion.setStyleSheet("background-color: rgb(226, 245, 255);\n"
                                         "border-radius:8px;\n"
                                         "")
        self.tblHabitacion.setObjectName("tblHabitacion")
        self.tblHabitacion.setColumnCount(9)
        self.tblHabitacion.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(8, item)
        self.tblHabitacion.verticalHeader().setMinimumSectionSize(24)
        self.label_2 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtPrecio = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtPrecio.setGeometry(QtCore.QRect(500, 100, 121, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.txtPrecio.setFont(font)
        self.txtPrecio.setStyleSheet("background-color: rgb(239, 239, 239);\n"
                                     "border-radius:4px;")
        self.txtPrecio.setObjectName("txtPrecio")
        self.txtDescripcion = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtDescripcion.setGeometry(QtCore.QRect(40, 100, 411, 30))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        self.txtDescripcion.setFont(font)
        self.txtDescripcion.setStyleSheet("background-color: rgb(239, 239, 239);\n"
                                          "border-radius:4px;")
        self.txtDescripcion.setObjectName("txtDescripcion")
        self.label_10 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_10.setGeometry(QtCore.QRect(660, 80, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.txtTamanio = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtTamanio.setGeometry(QtCore.QRect(400, 40, 121, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.txtTamanio.setFont(font)
        self.txtTamanio.setStyleSheet("background-color: rgb(239, 239, 239);\n"
                                      "border-radius:4px;")
        self.txtTamanio.setObjectName("txtTamanio")
        self.label_6 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(280, 20, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.txtNPiso = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtNPiso.setGeometry(QtCore.QRect(280, 40, 91, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.txtNPiso.setFont(font)
        self.txtNPiso.setStyleSheet("background-color: rgb(239, 239, 239);\n"
                                    "border-radius:4px;")
        self.txtNPiso.setObjectName("txtNPiso")
        self.label_9 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_9.setGeometry(QtCore.QRect(500, 80, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.cmbTipoBanio = QtWidgets.QComboBox(parent=self.widget_3)
        self.cmbTipoBanio.setGeometry(QtCore.QRect(670, 40, 181, 30))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(False)
        self.cmbTipoBanio.setFont(font)
        self.cmbTipoBanio.setStyleSheet("background-color: rgb(239, 239, 239);\n"
                                        "border-radius:4px;")
        self.cmbTipoBanio.setObjectName("cmbTipoBanio")
        self.cmbTipoBanio.addItem("")
        self.cmbTipoBanio.setItemText(0, "")
        self.cmbTipoBanio.addItem("")
        self.cmbTipoBanio.addItem("")
        self.label_7 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(540, 20, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.txtNCamas = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtNCamas.setGeometry(QtCore.QRect(540, 40, 111, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtNCamas.setFont(font)
        self.txtNCamas.setStyleSheet("background-color: rgb(239, 239, 239);\n"
                                     "border-radius:4px;")
        self.txtNCamas.setObjectName("txtNCamas")
        self.btnLimpiar = QtWidgets.QPushButton(parent=self.widget_3)
        self.btnLimpiar.setGeometry(QtCore.QRect(620, 160, 211, 51))
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
        self.btnAgregar = QtWidgets.QPushButton(parent=self.widget_3)
        self.btnAgregar.setGeometry(QtCore.QRect(160, 160, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.btnAgregar.setFont(font)
        self.btnAgregar.setStyleSheet("QPushButton {\n"
                                      "    border-radius: 20px;\n"
                                      "    background-color: rgb(15, 121, 255);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(10, 90, 200);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "}")
        self.btnAgregar.setObjectName("btnAgregar")
        self.btnEliminar = QtWidgets.QPushButton(parent=self.widget_3)
        self.btnEliminar.setGeometry(QtCore.QRect(390, 160, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.btnEliminar.setFont(font)
        self.btnEliminar.setStyleSheet("QPushButton {\n"
                                       "    border-radius: 20px;\n"
                                       "    background-color: rgb(15, 121, 255);\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(10, 90, 200);\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "}")
        self.btnEliminar.setObjectName("btnEliminar")
        self.btnBuscar = QtWidgets.QPushButton(parent=self.widget_3)
        self.btnBuscar.setGeometry(QtCore.QRect(365, 244, 171, 40))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.btnBuscar.setFont(font)
        self.btnBuscar.setStyleSheet("QPushButton {\n"
                                     "    border-radius: 20px;\n"
                                     "    background-color: rgb(15, 121, 255);\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: rgb(10, 90, 200);\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "}")
        self.btnBuscar.setObjectName("btnBuscar")
        self.txtImagenHabitacion = QtWidgets.QLabel(parent=self.widget_3)
        self.txtImagenHabitacion.setGeometry(QtCore.QRect(860, 10, 301, 211))
        self.txtImagenHabitacion.setText("")
        self.txtImagenHabitacion.setPixmap(QtGui.QPixmap(":/habitacion1.jpeg"))
        self.txtImagenHabitacion.setScaledContents(True)
        self.txtImagenHabitacion.setObjectName("txtImagenHabitacion")
        self.txtLogo = QtWidgets.QLabel(parent=self.widget)
        self.txtLogo.setGeometry(QtCore.QRect(1163, 5, 91, 71))
        self.txtLogo.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.txtLogo.setMidLineWidth(-2)
        self.txtLogo.setText("")
        #self.txtLogo.setPixmap(QtGui.QPixmap("logo2.PNG"))
        self.txtLogo.setPixmap(QtGui.QPixmap(resource_path("logo2.PNG")))
        self.txtLogo.setScaledContents(True)
        self.txtLogo.setObjectName("txtLogo")
        self.frame = QtWidgets.QFrame(parent=self.widget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1261, 80))
        self.frame.setStyleSheet("background-color: rgb(24, 71, 113);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(400, 20, 561, 41))
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

        self.retranslateUi(gestionHabitacion)
        QtCore.QMetaObject.connectSlotsByName(gestionHabitacion)

        # Ancho de columnas de tablas
        self.tblHabitacion.setColumnWidth(0, 55) # ID
        self.tblHabitacion.setColumnWidth(1, 130) # tipo
        self.tblHabitacion.setColumnWidth(2, 65) # N piso
        self.tblHabitacion.setColumnWidth(3, 80) # tamaño
        self.tblHabitacion.setColumnWidth(4, 260) # descripcion
        self.tblHabitacion.setColumnWidth(5, 70) # N camas
        self.tblHabitacion.setColumnWidth(7, 70) # tipo de baño
        self.tblHabitacion.setColumnWidth(8, 110) #  precio
        self.tblHabitacion.setColumnWidth(9, 100)  # estado

        self.llenaTblHabitacion(False, "")
        self.tblHabitacion.verticalHeader().setVisible(False)
        self.btnBuscar.clicked.connect(self.busqueda)
        self.filtro_busqueda = False
        self.cadBuscar = ""
        self.txtBuscar.textChanged.connect(self.busqueda)
        self.btnAgregar.clicked.connect(self.registroHabitacion)
        self.tblHabitacion.itemSelectionChanged.connect(self.selRegistroTabla)
        self.id_habitacion_seleccionada = None
        self.fila_seleccionada = None
        self.btnEliminar.clicked.connect(self.eliminaHabitacion)
        self.btnLimpiar.clicked.connect(self.limpia)
        self.cmbTipoHabitacion.currentIndexChanged.connect(self.cambiarImagen)
        self.btnRegresar.clicked.connect(self.open_regresar)

    def retranslateUi(self, gestionHabitacion):
        _translate = QtCore.QCoreApplication.translate
        gestionHabitacion.setWindowTitle(_translate("gestionHabitacion", "Form"))
        self.cmbTipoHabitacion.setItemText(1, _translate("gestionHabitacion", "Sencilla"))
        self.cmbTipoHabitacion.setItemText(2, _translate("gestionHabitacion", "Doble"))
        self.cmbTipoHabitacion.setItemText(3, _translate("gestionHabitacion", "Suite"))
        self.cmbTipoHabitacion.setItemText(4, _translate("gestionHabitacion", "Familiar"))
        self.cmbTipoHabitacion.setItemText(5, _translate("gestionHabitacion", "Matrimonial"))
        self.label_8.setText(_translate("gestionHabitacion", "TIPO DE BAÑO"))
        self.label_4.setText(_translate("gestionHabitacion", "TAMAÑO EN m²"))
        self.cmbEstado.setItemText(1, _translate("gestionHabitacion", "Disponible"))
        self.cmbEstado.setItemText(2, _translate("gestionHabitacion", "Ocupado"))
        self.cmbEstado.setItemText(3, _translate("gestionHabitacion", "Mantenimiento"))
        self.label_5.setText(_translate("gestionHabitacion", "DESCRIPCIÓN"))
        item = self.tblHabitacion.horizontalHeaderItem(0)
        item.setText(_translate("gestionHabitacion", "ID"))
        item = self.tblHabitacion.horizontalHeaderItem(1)
        item.setText(_translate("gestionHabitacion", "Tipo Habitación"))
        item = self.tblHabitacion.horizontalHeaderItem(2)
        item.setText(_translate("gestionHabitacion", "N° piso"))
        item = self.tblHabitacion.horizontalHeaderItem(3)
        item.setText(_translate("gestionHabitacion", "Tamaño"))
        item = self.tblHabitacion.horizontalHeaderItem(4)
        item.setText(_translate("gestionHabitacion", "Descripción"))
        item = self.tblHabitacion.horizontalHeaderItem(5)
        item.setText(_translate("gestionHabitacion", "N° camas"))
        item = self.tblHabitacion.horizontalHeaderItem(6)
        item.setText(_translate("gestionHabitacion", "Tipo Baño"))
        item = self.tblHabitacion.horizontalHeaderItem(7)
        item.setText(_translate("gestionHabitacion", "Precio"))
        item = self.tblHabitacion.horizontalHeaderItem(8)
        item.setText(_translate("gestionHabitacion", "Estado"))
        self.label_2.setText(_translate("gestionHabitacion", "TIPO DE HABITACIÓN"))
        self.txtPrecio.setPlaceholderText(_translate("gestionHabitacion", "  00.00"))
        self.label_10.setText(_translate("gestionHabitacion", "ESTADO"))
        self.txtTamanio.setPlaceholderText(_translate("gestionHabitacion", "00.00"))
        self.label_6.setText(_translate("gestionHabitacion", "N° DE PISO"))
        self.label_9.setText(_translate("gestionHabitacion", "PRECIO EN S/"))
        self.cmbTipoBanio.setItemText(1, _translate("gestionHabitacion", "Privado"))
        self.cmbTipoBanio.setItemText(2, _translate("gestionHabitacion", "Jacuzzi"))
        self.label_7.setText(_translate("gestionHabitacion", "N° DE CAMAS"))
        self.btnLimpiar.setText(_translate("gestionHabitacion", "LIMPIAR"))
        self.btnAgregar.setText(_translate("gestionHabitacion", "AGREGAR"))
        self.btnEliminar.setText(_translate("gestionHabitacion", "ELIMINAR"))
        self.btnBuscar.setText(_translate("gestionHabitacion", "BUSCAR"))
        self.label_3.setText(_translate("gestionHabitacion", "GESTIÓN DE HABITACIONES"))
        self.btnRegresar.setText(_translate("gestionHabitacion", "REGRESAR"))

    def llenaTblHabitacion(self, filtro_busqueda, cadBuscar):
        try:
            sql = "SELECT * FROM Habitacion "  # 1

            if filtro_busqueda:
                sql += (f" WHERE Tipo LIKE '{cadBuscar}%'"
                        f" OR Descripcion LIKE '{cadBuscar}%'"
                        f" OR Tipo_baño LIKE '{cadBuscar}%'"
                        f" OR Estado LIKE '{cadBuscar}%'")  # 1

            list_habitacion = conexion.resultadoSQL(sql)  # n

            # Limpiar la tabla antes de llenarla
            self.tblHabitacion.setRowCount(0)  # 1

            # Obtener y configurar el número de filas en la tabla
            num_rows = len(list_habitacion)  # 1
            self.tblHabitacion.setRowCount(num_rows)  # 1

            # Configurar la fuente para los elementos de la tabla
            font3 = QtGui.QFont()
            font3.setFamily("Segoe UI")
            font3.setPointSize(11)

            # Recorre los datos y llénalos en la tabla
            for row_index, row_data in enumerate(list_habitacion):  # n
                for col_index, col_data in enumerate(row_data):  # m
                    # Crea un item en la tabla para cada celda
                    item = QTableWidgetItem(str(col_data))  # 1
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # 1
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)  # 1
                    item.setFont(font3)  # 1
                    self.tblHabitacion.setItem(row_index, col_index, item)  # 1

        except Exception as e:
            QMessageBox.warning(None, "Error", str(e))  # 1
        # Complejidad total: O(n * m)

    def busqueda(self):
        try:
            cadBuscar = self.txtBuscar.text().strip()
            if cadBuscar=="":
                self.llenaTblHabitacion(False,"")
            else:
                self.llenaTblHabitacion(True, cadBuscar)
        except Exception as e:
            QMessageBox.warning(None, "Error", str(e))

    def id_siguiente(self, nombTbl, nombCamp):
        try:
            # Consulta para contar registros
            sql_count = f"SELECT COUNT({nombCamp}) AS total FROM {nombTbl}"
            result_count = conexion.resultadoSQL(sql_count)  # 1

            if result_count:
                countReg = result_count[0][0]  # 1

                if countReg > 0:
                    # Consulta para obtener el ID máximo
                    sql_max = f"SELECT MAX({nombCamp}) AS idMax FROM {nombTbl}"
                    result_max = conexion.resultadoSQL(sql_max)  # n

                    if result_max:
                        max_id = result_max[0][0]  # 1
                        return max_id + 1  # 1
                else:
                    return 1  # 1
            else:
                return 1  # 1
        except Exception as e:
            QMessageBox.warning(None, "Error", str(e))  # 1
            return None  # 1

    # Complejidad total: O(n)

    def valida(self):
        print("llega")
        sw = False
        mensajes = ""

        try:
            # Validar cmbTipoHabitacion
            if self.cmbTipoHabitacion.currentText().strip() == "":  # 1
                mensajes += "Debe registrar el Tipo de Habitación\n"  # 1

            # Validar txtNPiso
            nPiso = self.txtNPiso.text().strip()  # 1
            if nPiso == "":  # 1
                mensajes += "Debe registrar el Número de Piso\n"  # 1
            elif not nPiso.isdigit():  # 1
                mensajes += "El Número de Piso solo debe contener números enteros\n"  # 1

            # Validar txtTamanio
            tamanio = self.txtTamanio.text().strip()  # 1

            if tamanio == "":  # 1
                mensajes += "Debe registrar el Tamaño\n"  # 1
            else:
                # Validar formato decimal con 2 decimales
                if not re.fullmatch(r'^\d+\.\d{2}$', tamanio):  # 1
                    mensajes += "El Tamaño debe estar en formato decimal con 2 decimales (ej: 15.00)\n"  # 1

            # Validar txtDescripcion
            if self.txtDescripcion.text().strip() == "":  # 1
                mensajes += "Debe registrar la Descripción\n"  # 1

            # Validar txtNCamas
            nCamas = self.txtNCamas.text().strip()  # 1
            if nCamas == "":  # 1
                mensajes += "Debe registrar el Número de Camas\n"  # 1
            elif not nCamas.isdigit():  # 1
                mensajes += "El Número de Camas solo debe contener números enteros\n"  # 1

            # Validar cmbTipoBanio
            if self.cmbTipoBanio.currentText().strip() == "":  # 1
                mensajes += "Debe registrar el Tipo de Baño\n"  # 1

            # Validar txtPrecio
            precio = self.txtPrecio.text().strip()  # 1
            if precio == "":  # 1
                mensajes += "Debe registrar un Precio\n"  # 1
            else:
                # Validar formato decimal con 2 decimales
                if not re.fullmatch(r'^\d+\.\d{2}$', precio):  # 1
                    mensajes += "El Precio debe estar en formato decimal con 2 decimales (ej: 150.00)\n"  # 1

            # Validar cmbEstado
            if self.cmbEstado.currentText().strip() == "":  # 1
                mensajes += "Debe registrar un Estado\n"  # 1

            # Verificar si hubo errores
            if mensajes == "":  # 1
                sw = True
            else:
                QMessageBox.warning(self, "Advertencia", mensajes.strip())  # 1
                print("1 vez")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error: {str(e)}")  # 1
            print("2 vez")
        return sw  # 1

    # Complejidad total: O(1)

    def registroHabitacion(self):
        if self.btnAgregar.text() == "AGREGAR":
            if self.valida():  # 1
                try:
                    id_habitacion = self.id_siguiente("Habitacion", "Habitacion_ID")  # 1
                    tipo_habitacion = self.cmbTipoHabitacion.currentText().strip()  # 1
                    numero_piso = self.txtNPiso.text().strip()  # 1
                    tamanio = self.txtTamanio.text().strip()  # 1
                    descripcion = self.txtDescripcion.text().strip()  # 1
                    numero_camas = self.txtNCamas.text().strip()  # 1
                    tipo_banio = self.cmbTipoBanio.currentText().strip()  # 1
                    precio = self.txtPrecio.text().strip()  # 1
                    estado = self.cmbEstado.currentText().strip()  # 1

                    sql = f"""
                    INSERT INTO Habitacion (Habitacion_ID, Tipo, Piso, Tamaño, Descripcion, N_camas, Tipo_baño, Precio, Estado)
                    VALUES ({id_habitacion}, '{tipo_habitacion}', {numero_piso}, {tamanio}, '{descripcion}', {numero_camas}, '{tipo_banio}', {precio}, '{estado}');
                    """  # 1
                    conexion.ejecutaSQL(sql)  # 1

                    # Guardar la imagen con el nombre basado en el ID de la habitación
                    # self.guardarImagen(id_habitacion)
                    self.llenaTblHabitacion(False, "")  # 1
                    QMessageBox.information(self, "Éxito", "Habitación registrada correctamente.")  # 1
                    self.limpia()  # 1

                except Exception as e:
                    QMessageBox.warning(None, "Error", str(e))  # 1

        if self.btnAgregar.text() == "ACTUALIZAR":
            if self.valida():  # 1
                try:
                    # Obtener el ID de la habitación a actualizar desde la variable global
                    id_habitacion = self.id_habitacion_seleccionada  # 1

                    # Obtener los valores actuales de los campos
                    tipo_habitacion = self.cmbTipoHabitacion.currentText().strip()  # 1
                    numero_piso = self.txtNPiso.text().strip()  # 1
                    tamanio = self.txtTamanio.text().strip()  # 1
                    descripcion = self.txtDescripcion.text().strip()  # 1
                    numero_camas = self.txtNCamas.text().strip()  # 1
                    tipo_banio = self.cmbTipoBanio.currentText().strip()  # 1
                    precio = self.txtPrecio.text().strip()  # 1
                    estado = self.cmbEstado.currentText().strip()  # 1

                    # Crear la sentencia SQL para actualizar los datos
                    sql = f"""
                    UPDATE Habitacion
                    SET Tipo = '{tipo_habitacion}',
                        Piso = {numero_piso},
                        Tamaño = {tamanio},
                        Descripcion = '{descripcion}',
                        N_camas = {numero_camas},
                        Tipo_baño = '{tipo_banio}',
                        Precio = {precio},
                        Estado = '{estado}'
                    WHERE Habitacion_ID = {id_habitacion};
                    """  # 1
                    # Ejecutar la sentencia SQL
                    conexion.ejecutaSQL(sql)  # 1

                    # Actualizar la tabla y limpiar los campos del formulario
                    self.llenaTblHabitacion(False, "")  # 1
                    QMessageBox.information(self, "Éxito", "Habitación actualizada correctamente.")  # 1
                    self.limpia()  # 1

                except Exception as e:
                    QMessageBox.warning(None, "Error", str(e))  # 1
    # Complejidad total: O(1)

    def limpia(self):
        self.txtNPiso.clear()
        self.txtTamanio.clear()
        self.txtDescripcion.clear()
        self.txtNCamas.clear()
        self.txtPrecio.clear()

        self.cmbTipoHabitacion.setCurrentIndex(-1)
        self.cmbTipoBanio.setCurrentIndex(-1)
        self.cmbEstado.setCurrentIndex(-1)
        self.tblHabitacion.clearSelection()
        self.btnAgregar.setText("AGREGAR")

    def selRegistroTabla(self):
        if self.tblHabitacion.selectedItems():
            # Cambiar el texto del botón a "Actualizar"
            self.btnAgregar.setText("ACTUALIZAR")

            # Obtener el registro seleccionado
            selected_row = self.tblHabitacion.currentRow()

            # Extraer los valores de la fila seleccionada
            id_habitacion = self.tblHabitacion.item(selected_row, 0).text()
            tipo_habitacion = self.tblHabitacion.item(selected_row, 1).text()
            numero_piso = self.tblHabitacion.item(selected_row, 2).text()
            tamanio = self.tblHabitacion.item(selected_row, 3).text()
            descripcion = self.tblHabitacion.item(selected_row, 4).text()
            numero_camas = self.tblHabitacion.item(selected_row, 5).text()
            tipo_banio = self.tblHabitacion.item(selected_row, 6).text()
            precio = self.tblHabitacion.item(selected_row, 7).text()
            estado = self.tblHabitacion.item(selected_row, 8).text()

            # Llenar los campos del formulario con los datos seleccionados
            self.cmbTipoHabitacion.setCurrentText(tipo_habitacion)
            self.txtNPiso.setText(numero_piso)
            self.txtTamanio.setText(tamanio)
            self.txtDescripcion.setText(descripcion)
            self.txtNCamas.setText(numero_camas)
            self.cmbTipoBanio.setCurrentText(tipo_banio)
            self.txtPrecio.setText(precio)
            self.cmbEstado.setCurrentText(estado)

            self.id_habitacion_seleccionada = id_habitacion
            #print(self.id_habitacion_seleccionada)
            self.fila_seleccionada= selected_row

    def eliminaHabitacion(self):
        if self.tblHabitacion.selectedItems():
            try:
                respuesta = QMessageBox.question(
                    self,
                    "Confirmar eliminación",
                    "¿Estás seguro de que deseas eliminar esta habitación?",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                    QMessageBox.StandardButton.No  # Default button
                )
            except Exception as e:
                print(f"Error mostrando el diálogo: {e}")
                return

            if respuesta == QMessageBox.StandardButton.Yes:
                try:
                    # Obtener el ID de la habitación seleccionada desde la variable global
                    id_habitacion = self.id_habitacion_seleccionada

                    # Crear la sentencia SQL para eliminar el registro
                    sql = f"DELETE FROM Habitacion WHERE Habitacion_ID = {id_habitacion};"

                    # Ejecutar la sentencia SQL
                    conexion.ejecutaSQL(sql)
                    #print(sql)

                    # Actualizar la tabla para reflejar los cambios
                    self.llenaTblHabitacion(False, "")
                    QMessageBox.information(self, "Éxito", "Habitación eliminada correctamente.")
                    self.limpia()

                except Exception as e:
                    QMessageBox.warning(self, "Error", str(e))
            else:
                QMessageBox.information(self, "Cancelado", "La eliminación ha sido cancelada.")
        else:
            QMessageBox.warning(self, "Advertencia", "No se ha seleccionado ninguna habitación para eliminar.")

    def cambiarImagen(self):
        # Obtener el tipo de habitación seleccionado
        tipo_habitacion = self.cmbTipoHabitacion.currentText()  # 1

        # Mapear el tipo de habitación a la imagen correspondiente
        imagen_map = {
            "Simple": "sencilla.jpeg",  # 1
            "Suite": "suite.jpeg",  # 1
            "Doble": "doble.jpeg",  # 1
            "Familiar": "familiar.jpeg",  # 1
            "Matrimonial": "matrimonial.jpeg"  # 1
        }

        # Obtener el nombre del archivo de la imagen correspondiente
        imagen_archivo = imagen_map.get(tipo_habitacion, "default.jpeg")  # 1

        # Establecer la imagen en el QLabel
        pixmap = QtGui.QPixmap(resource_path(imagen_archivo))  # 1
        self.txtImagenHabitacion.setPixmap(pixmap)  # 1
    # Complejidad total: O(1)

    def __init__(self,dato,ventana_principal):
        super().__init__()
        self.id_user = dato
        self.ventana_prin = ventana_principal
        self.setupUi(self)

    def open_regresar(self):
        self.close()
        self.ventana_prin.show()

    def keyPressEvent(self, event):
        """Detecta si se presionó la tecla Escape y regresa a la ventana principal."""
        if event.key() == Qt.Key.Key_Escape:
            self.open_regresar()

import sys
class MainWindow(QMainWindow, Ui_GestHabi):
        def __init__(self):
                super().__init__()
                self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
