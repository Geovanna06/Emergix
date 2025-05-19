import sys
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QDialog, QVBoxLayout, QTextEdit, QMessageBox, QPushButton)
from data_management.processamento_lci import selecionar_arquivo_csv
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Emergix")
        appIcon = QIcon(u"Icons/Logo_Emergix - principal.png")
        self.setWindowIcon(appIcon)

        self.btnUpload.clicked.connect(self.importar_csv)
        self.btnAbrirArquivo.clicked.connect(self.abrir_csv_importado)
        self.btnExcluirArquivo.clicked.connect(self.excluir_csv)

    # Importa arquivo csv
    def importar_csv(self):
        dados = selecionar_arquivo_csv(self)
        self.lblUpload.setText("Upload Concluído!")
        if dados is not None:
            print(dados.head())
            self.dados_csv = dados

    # Abre o arquivo csv importado
    def abrir_csv_importado(self):
        if not hasattr(self, 'dados_csv') or self.dados_csv is None:
            QMessageBox.warning(self, "Aviso", "Nenhum arquivo CSV foi importado ainda.")
            return

    # Cria uma nova janela para exibir o conteúdo
        janela = QDialog(self)
        janela.setWindowTitle("Visualização do CSV")
        layout = QVBoxLayout()

        texto = QTextEdit()
        texto.setReadOnly(True)
        texto.setPlainText(self.dados_csv.to_string(index=False))

        layout.addWidget(texto)
        janela.setLayout(layout)
        janela.exec()
    
    # Exclui o arquivo csv importado da memória    
    def excluir_csv(self):
        if hasattr(self, 'dados_csv') and self.dados_csv is not None:
            self.dados_csv = None
            #self.caminho_csv = None
            self.lblUpload.setText("")
            QMessageBox.information(self, "Sucesso", "Arquivo removido.")
        else:
            QMessageBox.warning(self, "Aviso", "Nenhum arquivo foi importado.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setStyle("Fusion") 
    window = MainWindow()
    window.show()
    app.exec()