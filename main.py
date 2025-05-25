import sys
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QDialog, QVBoxLayout, QTextEdit, QMessageBox, QPushButton, QTableWidget, QTableWidgetItem)
from data_management.processamento_lci import selecionar_arquivo_csv
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
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
        self.btnGrafico1.clicked.connect(self.criar_tabela)
        self.btnGrafico2.clicked.connect(self.criar_grafico)

    # Importa arquivo csv
    def importar_csv(self):
        dados = selecionar_arquivo_csv(self)
        if dados is not None:
            print(dados.head())
            self.dados_csv = dados
            self.lblUpload.setText("Upload Concluído!")

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

    def criar_tabela(self):
        
        layout = QVBoxLayout()
        self.pgGrafico1.setLayout(layout)

# 1. Cria a tabela
        self.tableEmergia = QTableWidget()
        self.tableEmergia.setColumnCount(2)
        self.tableEmergia.setHorizontalHeaderLabels(["Processo", "Emergia (seJ)"])

# Dados de exemplo
        processos = [
            ("Processo A", "1.5E+12"),
            ("Processo B", "2.3E+13"),
            ("Processo C", "4.9E+11"),
        ]

        self.tableEmergia.setRowCount(len(processos))
        for i, (nome, emergia) in enumerate(processos):
            self.tableEmergia.setItem(i, 0, QTableWidgetItem(nome))
            self.tableEmergia.setItem(i, 1, QTableWidgetItem(emergia))

        # Adicionar a tabela ao layout
        layout.addWidget(self.tableEmergia)

        # Adicionar a página ao QStackedWidget
        self.swGraficos.addWidget(self.pgGrafico1)
        self.swGraficos.setCurrentWidget(self.pgGrafico1)
        
    def criar_grafico(self):
        # Exemplo de dados (substitua com os seus dados reais)
        processos = ["Processo A", "Processo B", "Processo C", "Processo D"]
        emergias = [500, 300, 800, 200]

    # Criar a figura e o gráfico
        figura = Figure(figsize=(5, 3))
        eixo = figura.add_subplot(111)
        eixo.barh(processos, emergias, color="#4FA3A5")  # azul esverdeado médio
        eixo.set_xlabel("Emergia (seJ)")
        eixo.set_title("Ranking de Consumo de Emergia")

    # Canvas do gráfico embutido no Qt
        canvas = FigureCanvas(figura)

    # Layout da página pgGrafico2
        layout = QVBoxLayout()
        self.pgGrafico2.setLayout(layout)
        #layout = QVBoxLayout(self.pgGrafico2)
        layout.addWidget(canvas)
        self.swGraficos.setCurrentWidget(self.pgGrafico2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setStyle("Fusion") 
    window = MainWindow()
    window.show()
    app.exec()