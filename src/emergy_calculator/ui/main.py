import sys
from PySide6.QtWidgets import QApplication
from .main_window import MainWindow

def run_app():
    """Inicializa e executa a aplicação EmergyCalculator."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_app()