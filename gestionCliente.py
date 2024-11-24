from datetime import datetime, timedelta
import re
from PyQt6.QtCore import QDate, Qt, QRect, QCoreApplication
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem, QPushButton
from PyQt6 import QtCore, QtGui, QtWidgets
import conexion

class Ui_GestClie(QtWidgets.QWidget):
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
        self.widget.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.widget.setObjectName("widget")
        self.widget_3 = QtWidgets.QWidget(parent=self.widget)
        self.widget_3.setGeometry(QtCore.QRect(40, 100, 1171, 601))
        self.widget_3.setStyleSheet("border: 1px solid rgb(239, 239, 239);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.widget_3.setObjectName("widget_3")
        self.txtBuscar = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtBuscar.setGeometry(QtCore.QRect(40, 250, 311, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtBuscar.setFont(font)
        self.txtBuscar.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:8px;")
        self.txtBuscar.setObjectName("txtBuscar")
        self.label_2 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
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
        self.cmbSexo = QtWidgets.QComboBox(parent=self.widget_3)
        self.cmbSexo.setGeometry(QtCore.QRect(590, 100, 121, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cmbSexo.setFont(font)
        self.cmbSexo.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.cmbSexo.setObjectName("cmbSexo")
        self.cmbSexo.addItem("")
        self.cmbSexo.setItemText(0, "")
        self.cmbSexo.addItem("")
        self.cmbSexo.addItem("")
        self.txtApellidos = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtApellidos.setGeometry(QtCore.QRect(500, 40, 251, 30))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        self.txtApellidos.setFont(font)
        self.txtApellidos.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.txtApellidos.setText("")
        self.txtApellidos.setObjectName("txtApellidos")
        self.label_4 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_4.setGeometry(QtCore.QRect(230, 20, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_5.setGeometry(QtCore.QRect(500, 20, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txtCelular = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtCelular.setGeometry(QtCore.QRect(40, 100, 171, 30))
        font2 = QtGui.QFont()
        font2.setFamily("Segoe UI")
        font2.setPointSize(12)
        self.txtCelular.setFont(font2)
        self.txtCelular.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.txtCelular.setText("")
        self.txtCelular.setObjectName("txtCelular")
        self.label_11 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_11.setGeometry(QtCore.QRect(740, 80, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_8 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(230, 80, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.txtDireccion = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtDireccion.setGeometry(QtCore.QRect(230, 100, 331, 30))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        self.txtDireccion.setFont(font2)
        self.txtDireccion.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.txtDireccion.setText("")
        self.txtDireccion.setObjectName("txtDireccion")
        self.label_10 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_10.setGeometry(QtCore.QRect(590, 80, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_6 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(40, 80, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.txtNombres = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtNombres.setGeometry(QtCore.QRect(230, 40, 251, 30))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        self.txtNombres.setFont(font)
        self.txtNombres.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.txtNombres.setText("")
        self.txtNombres.setObjectName("txtNombres")
        self.txtCorreo = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtCorreo.setGeometry(QtCore.QRect(780, 40, 301, 30))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        self.txtCorreo.setFont(font)
        self.txtCorreo.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.txtCorreo.setText("")
        self.txtCorreo.setObjectName("txtCorreo")
        self.dtFechaNacimiento = QtWidgets.QDateEdit(parent=self.widget_3)
        self.dtFechaNacimiento.setGeometry(QtCore.QRect(740, 100, 191, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dtFechaNacimiento.setFont(font)
        self.dtFechaNacimiento.setObjectName("dtFechaNacimiento")
        self.txtDNI = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtDNI.setGeometry(QtCore.QRect(40, 40, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        self.txtDNI.setFont(font2)
        self.txtDNI.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.txtDNI.setText("")
        self.txtDNI.setObjectName("txtDNI")
        self.label_7 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(780, 20, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tblCliente = QtWidgets.QTableWidget(parent=self.widget_3)
        self.tblCliente.setGeometry(QtCore.QRect(40, 290, 1091, 291))
        self.tblCliente.setMaximumSize(QtCore.QSize(96100, 16777215))
        font3 = QtGui.QFont()
        font3.setFamily("Segoe UI")
        font3.setPointSize(11)
        self.tblCliente.setFont(font3)
        self.tblCliente.setStyleSheet("background-color: rgb(226, 245, 255);\n"
"border-radius:8px;\n"
"")
        self.tblCliente.setObjectName("tblCliente")
        self.tblCliente.setColumnCount(8)
        self.tblCliente.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblCliente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblCliente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblCliente.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblCliente.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblCliente.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblCliente.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblCliente.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblCliente.setHorizontalHeaderItem(7, item)
        self.tblCliente.verticalHeader().setMinimumSectionSize(24)
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Ancho de columnas de tablas
        self.tblCliente.setColumnWidth(0, 80) # DNI
        self.tblCliente.setColumnWidth(1, 160) # nombres
        self.tblCliente.setColumnWidth(2, 170) # apellidos
        self.tblCliente.setColumnWidth(3, 90) # celular
        self.tblCliente.setColumnWidth(4, 160) # correo
        self.tblCliente.setColumnWidth(5, 210) # direccion
        self.tblCliente.setColumnWidth(6, 80)  # sexo
        self.tblCliente.setColumnWidth(7, 110) # fecha nacimeinto

        self.llenaTblCliente(False, "")
        self.tblCliente.verticalHeader().setVisible(False)
        # self.btnBuscar.clicked.connect(self.busqueda)
        self.filtro_busqueda = False
        self.cadBuscar = ""
        self.txtBuscar.textChanged.connect(self.busqueda)
        fecha_especifica = QDate(2000, 1, 1)
        self.dtFechaNacimiento.setDate(fecha_especifica)
        self.dtFechaNacimiento.setCalendarPopup(True)

        self.btnAgregar.clicked.connect(self.registrarCliente)
        self.tblCliente.itemSelectionChanged.connect(self.selRegistroTabla)
        self.dni_seleccionado = None
        self.fila_seleccionada = None
        self.btnEliminar.clicked.connect(self.eliminaCliente)
        self.btnLimpiar.clicked.connect(self.limpia)
        self.btnRegresar.clicked.connect(self.open_regresar)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "DNI"))
        self.btnLimpiar.setText(_translate("Form", "LIMPIAR"))
        self.btnAgregar.setText(_translate("Form", "AGREGAR"))
        self.btnEliminar.setText(_translate("Form", "ELIMINAR"))
        self.btnBuscar.setText(_translate("Form", "BUSCAR"))
        self.cmbSexo.setItemText(1, _translate("Form", "Masculino"))
        self.cmbSexo.setItemText(2, _translate("Form", "Femenino"))
        self.label_4.setText(_translate("Form", "NOMBRES"))
        self.label_5.setText(_translate("Form", "APELLIDOS"))
        self.label_11.setText(_translate("Form", "FECHA DE NACIMIENTO"))
        self.label_8.setText(_translate("Form", "DIRECCIÓN"))
        self.label_10.setText(_translate("Form", "SEXO"))
        self.label_6.setText(_translate("Form", "CELULAR / TELÉFONO"))
        self.label_7.setText(_translate("Form", "CORREO ELECTRÓNICO"))
        item = self.tblCliente.horizontalHeaderItem(0)
        item.setText(_translate("Form", "DNI"))
        item = self.tblCliente.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nombres"))
        item = self.tblCliente.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Apellidos"))
        item = self.tblCliente.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Celular"))
        item = self.tblCliente.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Correo"))
        item = self.tblCliente.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Dirección"))
        item = self.tblCliente.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Sexo"))
        item = self.tblCliente.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Fecha nacimiento"))
        self.label_3.setText(_translate("Form", "GESTIÓN DE CLIENTES"))
        self.btnRegresar.setText(_translate("Form", "REGRESAR"))

    def llenaTblCliente(self, filtro_busqueda, cadBuscar):
        try:
            # Construcción de la consulta SQL inicial (Operación constante)
            sql = "SELECT DNI_Cliente, Nombres, Apellidos, Celular, Correo, Direccion, Sexo,"
            sql += " CONVERT(DATE, FechaNacimiento) FROM Cliente  "  # O(1)

            if filtro_busqueda:  # O(1)
                # Modificación de la consulta según el filtro (Operación constante)
                sql += (f" WHERE Nombres LIKE '{cadBuscar}%'"
                        f" OR Apellidos LIKE '{cadBuscar}%'"
                        f" OR CONVERT(VARCHAR, DNI_Cliente) LIKE '{cadBuscar}%'")  # O(1)

            # Ejecución de la consulta y obtención de resultados (Dependiente del tamaño de la base de datos)
            list_cliente = conexion.resultadoSQL(sql)  # O(n)

            self.tblCliente.setRowCount(0)  # O(1) - Resetea las filas de la tabla

            # Número de filas en la tabla
            num_rows = len(list_cliente)  # O(1)
            self.tblCliente.setRowCount(num_rows)  # O(1) - Establece la cantidad de filas en la tabla

            # Llenado de la tabla
            for row_index, row_data in enumerate(list_cliente):  # Repite n veces
                for col_index, col_data in enumerate(row_data):  # Repite m veces
                    item = QTableWidgetItem(str(col_data))  # O(1)
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # O(1)
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)  # O(1)
                    self.tblCliente.setItem(row_index, col_index, item)  # O(1)

        except Exception as e:  # Manejo de excepciones
            QMessageBox.warning(None, "Error", str(e))  # O(1)

    def busqueda(self):
        try:
            cadBuscar = self.txtBuscar.text().strip()  # 1 operación constante O(1)
            if cadBuscar == "":  # 1 operación constante O(1)
                self.llenaTblCliente(False,
                                     "")  # Llamada a otra función, su complejidad depende de la implementación de llenaTblCliente
            else:
                self.llenaTblCliente(True,
                                     cadBuscar)  # Llamada a otra función, su complejidad depende de la implementación de llenaTblCliente
        except Exception as e:
            QMessageBox.warning(None, "Error", str(e))  # 1 operación constante O(1)

    def valida(self):
        mensajes = ""  # 1

        # Validar txtNombres
        nombres = self.txtNombres.text().strip()  # 1
        if nombres == "":  # 1
            mensajes += "Debe registrar el Nombre\n"  # 1

        # Validar txtApellidos
        apellidos = self.txtApellidos.text().strip()  # 1
        if apellidos == "":  # 1
            mensajes += "Debe registrar el Apellido\n"  # 1

        # Validar txtCelular
        celular = self.txtCelular.text().strip()  # 1
        if celular == "":  # 1
            mensajes += "Debe registrar el Celular\n"  # 1
        elif not celular.isdigit():  # 1
            mensajes += "El Celular solo debe contener números\n"  # 1
        elif len(celular) < 9:  # 1
            mensajes += "El Celular debe tener al menos 9 dígitos\n"  # 1

        # Validar cmbSexo
        if self.cmbSexo.currentText().strip() == "":  # 1
            mensajes += "Debe seleccionar el Sexo\n"  # 1

        # Validar txtDNI
        dni = self.txtDNI.text().strip()  # 1
        if dni == "":  # 1
            mensajes += "Debe registrar el DNI\n"  # 1
        elif not dni.isdigit():  # 1
            mensajes += "El DNI solo debe contener números\n"  # 1
        elif len(dni) != 8:  # 1
            mensajes += "El DNI debe tener exactamente 8 dígitos\n"  # 1

        # Validar txtCorreo
        correo = self.txtCorreo.text().strip()  # 1
        if correo == "":  # 1
            mensajes += "Debe registrar el Correo\n"  # 1
        elif not re.fullmatch(r'[^@]+@[^@]+\.[^@]+', correo):  # 1
            mensajes += "El Correo debe tener un formato válido (ej: ejemplo@dominio.com)\n"  # 1

        # Validar txtDireccion
        direccion = self.txtDireccion.text().strip()  # 1
        if direccion == "":  # 1
            mensajes += "Debe registrar la Dirección\n"  # 1

        # Validar txtFechaNacimiento
        fecha_nacimiento = self.dtFechaNacimiento.text().strip()  # 1
        if fecha_nacimiento == "":  # 1
            mensajes += "Debe registrar la Fecha de Nacimiento\n"  # 1
        else:
            try:
                # Intentar parsear la fecha con el formato esperado
                fecha = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")  # 1

                # Verificar que la fecha no esté en el futuro
                if fecha > datetime.now():  # 1
                    mensajes += "La Fecha de Nacimiento no puede ser en el futuro\n"  # 1

                # Verificar que la fecha no sea mayor a 100 años desde la actualidad
                fecha_maxima = datetime.now() - timedelta(days=365 * 100)  # 1
                if fecha < fecha_maxima:  # 1
                    mensajes += "La Fecha de Nacimiento no puede ser mayor a 100 años desde la actualidad\n"  # 1

            except ValueError:  # 1
                mensajes += "La Fecha de Nacimiento debe tener el formato DD/MM/YYYY\n"  # 1

        if mensajes:  # 1
            QMessageBox.warning(self, "Validación de Datos", mensajes.strip())  # 1
            return False  # 1

        return True  # 1
        # Complejidad total: O(1)

    def registrarCliente(self):  # 1
        if self.btnAgregar.text() == "AGREGAR":  # 1
            if self.valida():  # 1
                try:  # 1
                    dni_cliente = self.txtDNI.text().strip()  # 1
                    nombres = self.txtNombres.text().strip()  # 1
                    apellidos = self.txtApellidos.text().strip()  # 1
                    celular = self.txtCelular.text().strip()  # 1
                    direccion = self.txtDireccion.text().strip()  # 1
                    correo = self.txtCorreo.text().strip()  # 1
                    sexo = self.cmbSexo.currentText().strip()  # 1
                    fecha_nacimiento = self.dtFechaNacimiento.date().toString("yyyy-MM-dd")  # 1
                    fecha_nacimiento += "T00:00:00"  # 1
                    sql = f"""                               # 1
                    INSERT INTO Cliente (DNI_Cliente, Nombres, Apellidos, Celular, Correo, Direccion, Sexo, FechaNacimiento)  # 1
                    VALUES ({dni_cliente}, '{nombres}', '{apellidos}', '{celular}', '{correo}', '{direccion}', '{sexo}', '{fecha_nacimiento}');  # 1
                    """  # 1
                    conexion.ejecutaSQL(sql)  # 1
                    self.llenaTblCliente(False, "")  # 1
                    QMessageBox.information(self, "Éxito", "Cliente registrado correctamente.")  # 1
                    self.limpia()  # 1
                except Exception as e:  # 1
                    QMessageBox.warning(self, "Error", str(e))  # 1

        elif self.btnAgregar.text() == "ACTUALIZAR":  # 1
            if self.valida():  # 1
                try:  # 1
                    dni_cliente = self.dni_seleccionado  # 1
                    nombres = self.txtNombres.text().strip()  # 1
                    apellidos = self.txtApellidos.text().strip()  # 1
                    celular = self.txtCelular.text().strip()  # 1
                    direccion = self.txtDireccion.text().strip()  # 1
                    correo = self.txtCorreo.text().strip()  # 1
                    sexo = self.cmbSexo.currentText().strip()  # 1
                    fecha_nacimiento = self.dtFechaNacimiento.date().toString("yyyy-MM-dd")  # 1

                    sql = f"""                               # 1
                    UPDATE Cliente                         # 1
                    SET Nombres = '{nombres}',              # 1
                        Apellidos = '{apellidos}',          # 1
                        Celular = '{celular}',              # 1
                        Correo = '{correo}',                # 1
                        Direccion = '{direccion}',          # 1
                        Sexo = '{sexo}',                    # 1
                        FechaNacimiento = '{fecha_nacimiento}'  # 1
                    WHERE DNI_Cliente = {dni_cliente};      # 1
                    """  # 1
                    conexion.ejecutaSQL(sql)  # 1
                    self.llenaTblCliente(False, "")  # 1
                    QMessageBox.information(self, "Éxito", "Cliente actualizado correctamente.")  # 1
                    self.limpia()  # 1
                except Exception as e:  # 1
                    QMessageBox.warning(self, "Error", str(e))  # 1

    # Complejidad total: O(1)

    def selRegistroTabla(self):  # 1
        if self.tblCliente.selectedItems():  # 1
            self.btnAgregar.setText("ACTUALIZAR")  # 1

            # Obtener la fila seleccionada
            selected_row = self.tblCliente.currentRow()  # 1

            dni = self.tblCliente.item(selected_row, 0).text()  # 1
            nombres = self.tblCliente.item(selected_row, 1).text()  # 1
            apellidos = self.tblCliente.item(selected_row, 2).text()  # 1
            celular = self.tblCliente.item(selected_row, 3).text()  # 1
            correo = self.tblCliente.item(selected_row, 4).text()  # 1
            direccion = self.tblCliente.item(selected_row, 5).text()  # 1
            sexo = self.tblCliente.item(selected_row, 6).text()  # 1
            fecha_nacimiento_str = self.tblCliente.item(selected_row, 7).text()  # 1

            # Convertir la fecha de nacimiento de string a QDate
            fecha_nacimiento = QDate.fromString(fecha_nacimiento_str, "yyyy-MM-dd")  # 1

            if fecha_nacimiento.isValid():  # 1
                self.txtDNI.setText(dni)  # 1
                self.txtNombres.setText(nombres)  # 1
                self.txtApellidos.setText(apellidos)  # 1
                self.txtCelular.setText(celular)  # 1
                self.txtDireccion.setText(direccion)  # 1
                self.txtCorreo.setText(correo)  # 1
                self.cmbSexo.setCurrentText(sexo)  # 1
                self.dtFechaNacimiento.setDate(fecha_nacimiento)  # 1

                self.dni_seleccionado = dni  # 1
                self.fila_seleccionada = selected_row  # 1
            else:  # 1
                print("Formato de fecha inválido:", fecha_nacimiento_str)  # 1
    # Complejidad total: O(1)

    def eliminaCliente(self):  # 1
        if self.tblCliente.selectedItems():  # 1
            try:  # 1
                respuesta = QMessageBox.question(  # 1
                    self,  # 1
                    "Confirmar eliminación",  # 1
                    "¿Estás seguro de que deseas eliminar este cliente?",  # 1
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,  # 1
                    QMessageBox.StandardButton.No  # 1
                )  # 1
            except Exception as e:  # 1
                print(f"Error mostrando el diálogo: {e}")  # 1
                return  # 1

            if respuesta == QMessageBox.StandardButton.Yes:  # 1
                try:  # 1
                    dni_cliente = self.dni_seleccionado  # 1
                    sql = f"DELETE FROM Cliente WHERE DNI_Cliente = {dni_cliente};"  # 1
                    conexion.ejecutaSQL(sql)  # 1
                    self.llenaTblCliente(False, "")  # 1
                    QMessageBox.information(self, "Éxito", "Cliente eliminado correctamente.")  # 1
                    self.limpia()  # 1

                except Exception as e:  # 1
                    QMessageBox.warning(self, "Error", str(e))  # 1
            else:  # 1
                QMessageBox.information(self, "Cancelado", "La eliminación ha sido cancelada.")  # 1
        else:  # 1
            QMessageBox.warning(self, "Advertencia", "No se ha seleccionado ningún cliente para eliminar.")  # 1
    # Complejidad total: O(1)

    def limpia(self):
        self.txtDNI.clear()  # 1
        self.txtNombres.clear()  # 1
        self.txtApellidos.clear()  # 1
        self.txtCelular.clear()  # 1
        self.txtDireccion.clear()  # 1
        self.txtCorreo.clear()  # 1

        self.cmbSexo.setCurrentIndex(-1)  # 1
        self.dtFechaNacimiento.setDate(QDate(2000, 1, 1))  # 1
        self.tblCliente.clearSelection()  # 1

        self.btnAgregar.setText("AGREGAR")  # 1
        self.dni_seleccionado = None  # 1
    # Complejidad total: O(1)

    def __init__(self,dato,ventana_principal):
        super().__init__()
        self.id_user = dato
        self.ventana_prin = ventana_principal
        self.setupUi(self)
        from reservarHabitacion import Ui_ReserHabi
        self.ui_reser_habi = Ui_ReserHabi(self.id_user, self)
        self.ui_reser_habi.llenaCmbClientes(False,"")

    def open_regresar(self):
        self.close()
        self.ventana_prin.show()
        self.ui_reser_habi.llenaCmbClientes(False,"")

    def keyPressEvent(self, event):
        """Detecta si se presionó la tecla Escape y regresa a la ventana principal."""
        if event.key() == Qt.Key.Key_Escape:
            self.open_regresar()


import sys
class MainWindow(QMainWindow, Ui_GestClie):
        def __init__(self):
                super().__init__()
                self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())