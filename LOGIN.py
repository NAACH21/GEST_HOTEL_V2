from PyQt6.QtCore import Qt, QRect, QCoreApplication, QMetaObject
from PyQt6.QtGui import QPalette, QBrush, QColor, QFont, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QLineEdit, QPushButton, QMessageBox, QCheckBox, \
        QRadioButton, QTextBrowser
from PyQt6.uic.Compiler.qtproxies import QtCore
from Main import Ui_Form
import os
from images import resource_path
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors



import conexion
class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                if not MainWindow.objectName():
                    MainWindow.setObjectName(u"DockWidget")
                MainWindow.resize(440, 478)
                MainWindow.setMinimumSize(440, 478)
                MainWindow.setMaximumSize(440, 478)
                self.dockWidgetContents = QWidget()
                self.dockWidgetContents.setObjectName(u"dockWidgetContents")
                self.widget = QWidget(self.dockWidgetContents)
                self.widget.setObjectName(u"widget")
                self.widget.setGeometry(QRect(0, 190, 461, 321))
                self.widget.setStyleSheet(u"background-color:  rgb(14,138, 229);\n"
                "")
                self.label_3 = QLabel(self.widget)
                self.label_3.setObjectName(u"label_3")
                self.label_3.setGeometry(QRect(170, 110, 131, 41))
                font = QFont()
                font.setFamilies([u"Gill Sans MT Condensed"])
                font.setPointSize(20)
                font.setBold(True)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
                self.widget_3 = QWidget(self.widget)
                self.widget_3.setObjectName(u"widget_3")
                self.widget_3.setGeometry(QRect(120, 80, 221, 16))
                self.widget_3.setStyleSheet(u"background-color: rgb(55, 111, 166);")
                self.widget_4 = QWidget(self.widget_3)
                self.widget_4.setObjectName(u"widget_4")
                self.widget_4.setGeometry(QRect(0, 90, 221, 16))
                self.widget_4.setStyleSheet(u"background-color: rgb(55, 111, 166);")
                self.lineEdit_3 = QLineEdit(self.widget_3)
                self.lineEdit_3.setObjectName(u"lineEdit_3")
                self.lineEdit_3.setGeometry(QRect(0, 70, 221, 31))
                font1 = QFont()
                font1.setPointSize(12)
                self.lineEdit_3.setFont(font1)
                self.lineEdit_3.setStyleSheet(u"border: none;\n"
                "")
                self.widget_5 = QWidget(self.widget)
                self.widget_5.setObjectName(u"widget_5")
                self.widget_5.setGeometry(QRect(120, 160, 221, 16))
                self.widget_5.setStyleSheet(u"background-color: rgb(55, 111, 166);")
                self.widget_6 = QWidget(self.widget_5)
                self.widget_6.setObjectName(u"widget_6")
                self.widget_6.setGeometry(QRect(0, 90, 221, 16))
                self.widget_6.setStyleSheet(u"background-color: rgb(55, 111, 166);")
                self.lineEdit_4 = QLineEdit(self.widget_5)
                self.lineEdit_4.setObjectName(u"lineEdit_4")
                self.lineEdit_4.setGeometry(QRect(0, 70, 221, 31))
                self.lineEdit_4.setFont(font1)
                self.lineEdit_4.setStyleSheet(u"border: none;\n"
                "")
                self.lineEdit = QLineEdit(self.widget)
                self.lineEdit.setObjectName(u"lineEdit")
                self.lineEdit.setGeometry(QRect(120, 141, 221, 31))
                self.lineEdit.setFont(font1)
                self.lineEdit.setStyleSheet(u"border: none;\n"
                "color: rgb(255, 255, 255);\n")
                self.lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
                self.lineEdit_2 = QLineEdit(self.widget)
                self.lineEdit_2.setObjectName(u"lineEdit_2")
                self.lineEdit_2.setGeometry(QRect(120, 60, 221, 31))
                self.lineEdit_2.setFont(font1)
                self.lineEdit_2.setStyleSheet(u"border: none;\n"
                "color: rgb(255, 255, 255);\n"
                "")
                self.label_2 = QLabel(self.widget)
                self.label_2.setObjectName(u"label_2")
                self.label_2.setGeometry(QRect(190, 30, 131, 41))
                palette = QPalette()
                brush = QBrush(QColor(255, 255, 255, 255))
                brush.setStyle(Qt.BrushStyle.SolidPattern)
                palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
                brush1 = QBrush(QColor(14, 138, 229, 255))
                brush1.setStyle(Qt.BrushStyle.SolidPattern)
                palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
                palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
                palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
                palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
                palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
                brush2 = QBrush(QColor(255, 255, 255, 128))
                brush2.setStyle(Qt.BrushStyle.SolidPattern)
        #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
                palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush2)
        #endif
                palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
                palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
                palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
                palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
                palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
                palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
                palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush2)
        #endif
                palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
                palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
                palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
                palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
                palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
                palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        #if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
                palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush2)
        #endif
                self.label_2.setPalette(palette)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
                self.most_contra = QRadioButton(self.widget)
                self.most_contra.setObjectName(u"most_contra")
                self.most_contra.setGeometry(QRect(150, 190, 151, 20))
                self.most_contra.toggled.connect(self.show_password)
                self.pushButton = QPushButton(self.widget)
                self.pushButton.setObjectName(u"pushButton")
                self.pushButton.setGeometry(QRect(140, 220, 161, 41))
                self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                "color:rgb(21, 72, 113);")

                self.widget_2 = QWidget(self.dockWidgetContents)
                self.widget_2.setObjectName(u"widget_2")
                self.widget_2.setGeometry(QRect(-10, 0, 471, 201))
                self.widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
                self.textBrowser = QTextBrowser(self.widget_2)
                self.textBrowser.setObjectName(u"textBrowser")
                self.textBrowser.setGeometry(QRect(60, 160, 256, 192))
                self.label_4 = QLabel(self.widget_2)
                self.label_4.setObjectName(u"label_4")
                self.label_4.setGeometry(QRect(120, 0, 221, 231))
                self.label_4.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
                self.label_4.setPixmap(QPixmap(resource_path(u"OIP.jpeg")))
                self.label_4.setScaledContents(True)
                self.label = QLabel(self.widget_2)
                self.label.setObjectName(u"label")
                self.label.setGeometry(QRect(150, 30, 161, 41))
                font2 = QFont()
                font2.setFamilies([u"Corbel Light"])
                font2.setPointSize(36)
                font2.setBold(False)
                self.label.setFont(font2)
                self.label.setAutoFillBackground(False)
                self.label.setStyleSheet(u"color:rgb(24, 71, 113);\n"
                "background-color: transparent;")
                MainWindow.setCentralWidget(self.dockWidgetContents)

                self.retranslateUi(MainWindow)
                QMetaObject.connectSlotsByName(MainWindow)

                # configuraciones
                self.pushButton.clicked.connect(self.validate_login)
                self.lineEdit_2.returnPressed.connect(self.validate_login) # Conectar Enter desde usuario
                self.lineEdit.returnPressed.connect(self.validate_login)  # Conectar Enter desde contraseña

        def retranslateUi(self, DockWidget):
                DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"DockWidget", None))
                self.label_3.setText(QCoreApplication.translate("DockWidget", u"CONTRASE\u00d1A", None))
                self.label_2.setText(QCoreApplication.translate("DockWidget", u"USUARIO", None))
                self.most_contra.setText(QCoreApplication.translate("DockWidget", u"Mostrar Contrase\u00f1a", None))
                self.pushButton.setText(QCoreApplication.translate("DockWidget", u"INGRESAR", None))
                self.label_4.setText("")
                #self.label.setText(QCoreApplication.translate("DockWidget", u"MARK'S", None))
            # retranslateUi

        def show_password(self):
                if self.most_contra.isChecked():
                        self.lineEdit.setEchoMode(QLineEdit.EchoMode.Normal)
                else:
                        self.lineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        def setLabelPalette(self, label, family, size, bold, r, g, b):
                palette = QPalette()
                brush = QBrush(QColor(r, g, b, 255))
                brush.setStyle(Qt.BrushStyle.SolidPattern)
                palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
                label.setPalette(palette)
                font = QFont()
                font.setFamilies([family])
                font.setPointSize(size)
                font.setBold(bold)
                label.setFont(font)
                label.setStyleSheet(f"color: rgb({r}, {g}, {b});")

        def setLineEditStyle(self, lineEdit, size, is_password=False):
                font = QFont()
                font.setPointSize(size)
                lineEdit.setFont(font)
                lineEdit.setStyleSheet("border: none;\ncolor: rgb(255, 255, 255);\n")
                if is_password:
                        lineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        def validate_login(self):
                try:
                        username = self.lineEdit_2.text()
                        password = self.lineEdit.text()
                        sql = "SELECT * FROM Empleado "
                        vec_user = conexion.resultadoSQL(sql)
                        login_successful = False
                        for i in vec_user:
                                if i[6] == username and i[7] == password:
                                        login_user = i[0]
                                        login_successful = True
                                        break

                        if login_successful:
                                QMessageBox.information(None, "Login Exitoso", "Usuario y contraseña correctos.")
                                self.principal = Ui_Form(login_user)
                                self.principal.show()
                                self.close()
                        else:
                                QMessageBox.warning(None, "Login Fallido", "Usuario o contraseña incorrectos.")
                except Exception as e:
                        QMessageBox.warning(None, "Error", str(e))

def resource_path(relative_path):
        """Obtiene la ruta absoluta de los recursos para el ejecutable o script."""
        base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
        return os.path.join(base_path, relative_path)

import sys
class MainWindow(QMainWindow, Ui_MainWindow):
        def __init__(self):
                super().__init__()
                self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
