from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QApplication
from PyQt6.QtCore import pyqtSignal

class HabitacionWindow(QDialog):
    habitacion_seleccionada = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Selecciona una habitación")
        self.setGeometry(150, 150, 250, 200)
        # Centrar la ventana
        self.center_window()
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

        # Crear botones para las opciones de habitaciones
        self.simple_button = QPushButton("Simple", self)
        self.simple_button.clicked.connect(lambda: self.seleccionar_habitacion(1))
        layout.addWidget(self.simple_button)

        self.doble_button = QPushButton("Doble", self)
        self.doble_button.clicked.connect(lambda: self.seleccionar_habitacion(2))
        layout.addWidget(self.doble_button)

        self.suite_button = QPushButton("Suite", self)
        self.suite_button.clicked.connect(lambda: self.seleccionar_habitacion(3))
        layout.addWidget(self.suite_button)

        self.familiar_button = QPushButton("Familiar", self)
        self.familiar_button.clicked.connect(lambda: self.seleccionar_habitacion(4))
        layout.addWidget(self.familiar_button)

        self.setLayout(layout)

    def seleccionar_habitacion(self, valor):
        self.habitacion_seleccionada.emit(valor)  # Emitir la señal con el valor seleccionado
        self.accept()  # Cerrar la ventana

    def center_window(self):
        # Obtener el tamaño de la pantalla desde QApplication
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        # Calcular las coordenadas para centrar la ventana
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        # Establecer la posición de la ventana
        self.move(x, y)
