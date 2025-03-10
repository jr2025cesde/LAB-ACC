import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class VentanaPyQt(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicaciones con PyQt6") 
        self.setGeometry(100, 100, 400, 400)

      
        layout = QVBoxLayout()

        label = QLabel("¡Bienvenido a PyQt6!", self)
        layout.addWidget(label)

      
        button = QPushButton("Aceptar", self)
        button.clicked.connect(self.cerrar_ventana)

    
        line_edit = QLineEdit(self)
        layout.addWidget(line_edit)

        self.setLayout(layout)


    def cerrar_ventana(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    ventana = VentanaPyQt()  
    ventana.show()  
    sys.exit(app.exec())  
    
    