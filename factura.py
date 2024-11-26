import webbrowser

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMessageBox
import http.client
import json
import re
from datetime import datetime
import conexion

class Ui_Factura(QtWidgets.QWidget):
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
        self.txtCodReserva = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtCodReserva.setGeometry(QtCore.QRect(230, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtCodReserva.setFont(font)
        self.txtCodReserva.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.txtCodReserva.setObjectName("txtCodReserva")
        self.label_11 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_11.setGeometry(QtCore.QRect(30, 90, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.txtIdTipoHabitacion = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtIdTipoHabitacion.setGeometry(QtCore.QRect(230, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtIdTipoHabitacion.setFont(font)
        self.txtIdTipoHabitacion.setStyleSheet("background-color: rgb(239, 239, 239);\n"
                                               "")
        self.txtIdTipoHabitacion.setObjectName("txtIdTipoHabitacion")
        self.label_12 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_12.setGeometry(QtCore.QRect(30, 130, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.txtCliente = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtCliente.setGeometry(QtCore.QRect(230, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtCliente.setFont(font)
        self.txtCliente.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.txtCliente.setObjectName("txtCliente")
        self.btnGenerarFactura = QtWidgets.QPushButton(parent=self.widget_3)
        self.btnGenerarFactura.setGeometry(QtCore.QRect(280, 200, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.btnGenerarFactura.setFont(font)
        self.btnGenerarFactura.setStyleSheet("QPushButton {\n"
                                             "    border-radius: 20px;\n"
                                             "    background-color: rgb(15, 121, 255);\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover {\n"
                                             "    background-color: rgb(10, 90, 200);\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "}")
        self.btnGenerarFactura.setObjectName("btnGenerarFactura")
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
        self.label_3.setGeometry(QtCore.QRect(530, 20, 191, 41))
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
        self.btnBuscar.clicked.connect(self.buscar_reserva)
        self.btnGenerarFactura.clicked.connect(self.generar_factura)


    def buscar_reserva(self):
        if not self.txtCodReserva.text():
            QMessageBox.warning(self,"Advertencia", "El campo no puede estar vacío.")
        else:
            QMessageBox.information(self, "Correcto", "Reservacion encontrada.")
            try:
                id_reserva = self.txtCodReserva.text().upper()
                sql = f"SELECT * FROM Reserva WHERE Reserva_ID = {id_reserva}"
                print(sql)
                self.result = conexion.resultadoSQL(sql)
                if len(self.result) != 0:
                    idUsuario = self.result[0][2]
                    idHab = self.result[0][3]
                    sql1 = f"SELECT * FROM Cliente WHERE DNI_Cliente = {idUsuario}"
                    print(sql1)
                    sql2 = f"SELECT * FROM Habitacion WHERE Habitacion_ID = {idHab}"
                    self.result1 = conexion.resultadoSQL(sql1)
                    self.result2 = conexion.resultadoSQL(sql2)
                    self.txtIdTipoHabitacion.setText(str(self.result2[0][1]))
                    self.txtCliente.setText(str(self.result1[0][1]))
                else:
                    QMessageBox.information(None, "No existe la reserva", "Ingrese una reserva Valida")

            except Exception as e:
                print("Error en la función buscar_reserva:", e)

    def generar_factura(self):
        id_reserva = self.txtCodReserva.text().strip().upper()
        if not id_reserva:
            QMessageBox.warning(self, "Advertencia", "El campo de código de reserva no puede estar vacío.")
            return

        try:
            # Consulta la reserva
            sql_reserva = f"SELECT * FROM Reserva WHERE Reserva_ID = {id_reserva}"
            self.reserva_result = conexion.resultadoSQL(sql_reserva)

            if not self.reserva_result or len(self.reserva_result) == 0:
                QMessageBox.warning(self, "Error", "Reserva no encontrada.")
                return

            idUsuario = self.reserva_result[0][2]
            idHab = self.reserva_result[0][3]

            # Consulta al cliente y habitación
            sql_cliente = f"SELECT * FROM Cliente WHERE DNI_Cliente = {idUsuario}"
            sql_habitacion = f"SELECT * FROM Habitacion WHERE Habitacion_ID = {idHab}"

            cliente_result = conexion.resultadoSQL(sql_cliente)
            habitacion_result = conexion.resultadoSQL(sql_habitacion)

            if not cliente_result or len(cliente_result) == 0 or not habitacion_result or len(habitacion_result) == 0:
                QMessageBox.warning(self, "Error", "Datos del cliente o habitación no encontrados.")
                return

            # Preparar los datos del cliente
            vec_Clie = [
                cliente_result[0][1],  # Nombre del cliente
                '104'+str(cliente_result[0][0]),  # DNI del cliente
                cliente_result[0][5]  # Dirección del cliente
            ]
            print(vec_Clie)


            # Preparar los datos de la factura
            precio_habitacion = float(habitacion_result[0][7])  # Campo Precio en la tabla Habitacion
            vec_factura = ["FF03", "53953", precio_habitacion]

            total_gravada = vec_factura[2]
            total_igv = total_gravada * 0.18

            # Preparar los productos
            vec_prod = [{
                "producto": habitacion_result[0][1],  # Tipo de habitación
                "cantidad": 1,
                "precio_base": precio_habitacion,
                "codigo_sunat": "-",  # Código SUNAT si aplica
                "codigo_producto": habitacion_result[0][0],  # ID de la habitación
                "codigo_unidad": "NIU"
            }]

            # Preparar el JSON del payload
            payload = json.dumps({
                "empresa": {
                    "ruc": "20604051984",  # RUC de la empresa
                    "razon_social": "FACTURACION ELECTRONICA MONSTRUO E.I.R.L.",
                    "nombre_comercial": "FACTURACION INTEGRAL",
                    "domicilio_fiscal": "AV. LA MOLINA NRO. 570",
                    "ubigeo": "150114",
                    "urbanizacion": "RESIDENCIAL MONTERRICO",
                    "distrito": "LA MOLINA",
                    "provincia": "LIMA",
                    "departamento": "LIMA",
                    "modo": "0",
                    "usu_secundario_produccion_user": "MODDATOS",
                    "usu_secundario_produccion_password": "MODDATOS"
                },
                "cliente": {
                    "razon_social_nombres": vec_Clie[0],
                    "numero_documento": vec_Clie[1],
                    "codigo_tipo_entidad": "6",
                    "cliente_direccion": vec_Clie[2]
                },
                "venta": {
                    "serie": vec_factura[0],
                    "numero": vec_factura[1],
                    "fecha_emision": datetime.now().strftime("%Y-%m-%d"),
                    "hora_emision": datetime.now().strftime("%H:%M:%S"),
                    "fecha_vencimiento": "",
                    "moneda_id": "1",
                    "forma_pago_id": "1",
                    "total_gravada": str(total_gravada),
                    "total_igv": str(total_igv),
                    "total_exonerada": "",
                    "total_inafecta": "",
                    "tipo_documento_codigo": "01",
                    "nota": "notas o comentarios"
                },
                "items": [
                    {
                        "producto": prod["producto"],
                        "cantidad": str(prod["cantidad"]),
                        "precio_base": str(prod["precio_base"]),
                        "codigo_sunat": prod["codigo_sunat"],
                        "codigo_producto": prod["codigo_producto"],
                        "codigo_unidad": prod["codigo_unidad"],
                        "tipo_igv_codigo": "10"
                    } for prod in vec_prod
                ]
            })

            # Enviar la solicitud a la API
            headers = {'Content-Type': 'application/json'}
            conn = http.client.HTTPSConnection("facturaciondirecta.com")
            conn.request("POST", "/API_SUNAT/post.php", payload, headers)
            res = conn.getresponse()
            data = res.read().decode('utf-8')

            print("Respuesta de la API completa:", data)  # Depuración

            # Extraer el JSON inicial
            json_match = re.search(r'(\{.*\})', data)
            if json_match:
                valid_json_string = json_match.group(1)
                data_final = json.loads(valid_json_string)

                # Procesar la respuesta
                ruta_pdf = data_final["data"].get("ruta_pdf")
                if ruta_pdf:
                    webbrowser.open(ruta_pdf)
                else:
                    QMessageBox.warning(self, "Error", "No se generó el PDF de la factura.")
            else:
                QMessageBox.critical(self, "Error", "No se encontró un JSON válido en la respuesta.")
        except json.JSONDecodeError as e:
            QMessageBox.critical(self, "Error", f"Error al procesar el JSON: {str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error inesperado: {str(e)}")

        self.txtIdTipoHabitacion.setText("")
        self.txtCliente.setText("")

        try:
            # Datos a insertar en la tabla Factura
            monto = total_gravada + total_igv
            reserva_id = id_reserva
            fecha_emision = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            metodo_pago = "Efectivo"  ## Ajusta según el método de pago correspondiente
            observacion = "Factura automática."[:30]  # Truncar observación a 30 caracteres para evitar errores

            # Consulta SQL con marcadores de parámetros
            sql_insert_factura = """
                INSERT INTO Factura (Monto, Reserva_ID, Fecha, Metodo_Pago, Observacion)
                VALUES (?, ?, ?, ?, ?);
            """
            print(sql_insert_factura)
            # Ejecutar la consulta con parámetros
            conexion.ejecutarSQL(sql_insert_factura, (monto, reserva_id, fecha_emision, metodo_pago, observacion))
            print("Factura registrada exitosamente en la base de datos.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al registrar la factura en la base de datos: {str(e)}")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnBuscar.setText(_translate("Form", "BUSCAR"))
        self.label_10.setText(_translate("Form", "CÓDIGO DE RESERVA"))
        self.label_11.setText(_translate("Form", "TIPO DE HABITACIÓN"))
        self.label_12.setText(_translate("Form", "CLIENTE"))
        self.btnGenerarFactura.setText(_translate("Form", "GENERAR FACTURA"))
        self.label_3.setText(_translate("Form", "FACTURAS"))
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
    window = Ui_Factura()
    window.show()
    sys.exit(app.exec())