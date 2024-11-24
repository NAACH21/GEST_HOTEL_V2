from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QApplication
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QFont

class PaymentWindow(QDialog):
    payment_selected = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Selecciona un método de pago")
        self.setGeometry(150, 150, 300, 200)

        # Centrar la ventana
        self.center_window()

        # Estilo minimalista para la ventana
        self.setStyleSheet("""
            QDialog {
                background-color: #f2f2f2;  /* Fondo gris claro */
                border-radius: 10px;
            }
            QPushButton {
                background-color: #4CAF50;  /* Verde suave */
                color: white;
                font-size: 16px;
                font-family: Arial;
                border: none;
                padding: 10px;
                border-radius: 15px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;  /* Verde más oscuro al pasar el ratón */
            }
        """)

        layout = QVBoxLayout()

        # Crear botones con estilo minimalista
        self.bank_transfer_button = QPushButton("Trans. Bancaria", self)
        self.bank_transfer_button.clicked.connect(lambda: self.select_payment_method("Trans. Bancaria"))
        layout.addWidget(self.bank_transfer_button)

        self.yape_plin_button = QPushButton("Yape/Plin", self)
        self.yape_plin_button.clicked.connect(lambda: self.select_payment_method("Yape/Plin"))
        layout.addWidget(self.yape_plin_button)

        self.cash_button = QPushButton("Efectivo", self)
        self.cash_button.clicked.connect(lambda: self.select_payment_method("Efectivo"))
        layout.addWidget(self.cash_button)

        # Ajuste de los márgenes y disposición
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        self.setLayout(layout)

    def select_payment_method(self, method):
        self.payment_selected.emit(method)  # Emitir la señal con el método seleccionado
        self.accept()  # Cerrar la ventana

    def center_window(self):
        # Obtener el tamaño de la pantalla
        screen_geometry = self.screen().geometry()
        # Calcular las coordenadas para centrar la ventana con un desplazamiento a la derecha
        x = (screen_geometry.width() - self.width()) // 2 + 500  # Ajusta 150 a un valor mayor o menor según necesites
        y = (screen_geometry.height() - self.height()) // 2 - 65
        # Establecer la posición de la ventana
        self.move(x, y)

