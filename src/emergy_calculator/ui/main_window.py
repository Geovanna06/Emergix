from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QMainWindow, QDialog, QVBoxLayout, QTextEdit, QMessageBox,
    QTableWidget, QTableWidgetItem, QHeaderView, QFileDialog
)

import tempfile
import os
import matplotlib.pyplot as plt
from openpyxl import load_workbook
from openpyxl.drawing.image import Image as ExcelImage
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# Importações dos módulos
from .ui_main import Ui_MainWindow
from ..data_management.file_importer import select_csv_file
from ..core.calculator import EmergyCalculator

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Janela principal da aplicação Emergix, gerenciando a interface do usuário
    e orquestrando a interação com os módulos de dados e cálculo.
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Emergix")
        appIcon = QIcon("src/emergy_calculator/ui/resources/Logo_Emergix - principal.png")
        self.setWindowIcon(appIcon)
        self.emergy_calculator = EmergyCalculator()
        self._connect_signals()
        self._initialize_ui_state()

    def _connect_signals(self):
        """Conecta os sinais (eventos da UI) aos slots (métodos de manipulação)."""
        self.btnUpload.clicked.connect(self.import_csv_file)
        self.btnAbrirArquivo.clicked.connect(self.view_imported_csv)
        self.btnExcluirArquivo.clicked.connect(self.clear_imported_csv)
        self.btnGrafico1.clicked.connect(self.create_emergy_table)
        self.btnGrafico2.clicked.connect(self.create_emergy_graph)
        self.btnCalcular.clicked.connect(self.run_emergy_analysis_clicked)
        self.btnExtrairRelatorio.clicked.connect(self.export_to_excel)

    def _initialize_ui_state(self):
        """Define o estado inicial dos elementos da UI."""
        self.lblUpload.setText("Nenhum arquivo selecionado")
        #self.btnAbrirArquivo.setEnabled(False)
        #self.btnExcluirArquivo.setEnabled(False)
        self.btnExtrairRelatorio.setEnabled(False)
        self.btnGrafico1.setEnabled(False)
        self.btnGrafico2.setEnabled(False)
        self.btnCalcular.setEnabled(False)
        self.swGraficos.setCurrentIndex(0)

    # --- Métodos de Manipulação de Dados (Chamadas para o módulo de dados) ---

    def import_csv_file(self):
        """Importa o arquivo csv e salva o DataFrame e caminho do arquivo"""
        resultado = select_csv_file(self)
        if resultado is not None:
            df, caminho = resultado
            self.caminho = caminho
            self.dados_csv = df
            self.lblUpload.setText("Upload Concluído!")
            self.btnAbrirArquivo.setEnabled(True)
            self.btnExcluirArquivo.setEnabled(True)
            self.btnCalcular.setEnabled(True)

    def view_imported_csv(self):
        """Abre uma nova janela para exibir o conteúdo completo do DataFrame importado."""
        if not hasattr(self, 'dados_csv') or self.dados_csv is None:
            QMessageBox.warning(self, "Aviso", "Nenhum arquivo CSV foi importado ainda.")
            return
        
        dialog = QDialog(self)
        dialog.setWindowTitle("Visualização do CSV")
        layout = QVBoxLayout()

        text_display = QTextEdit()
        text_display.setReadOnly(True)
        text_display.setPlainText(self.dados_csv.to_string(index=False))

        layout.addWidget(text_display)
        dialog.setLayout(layout)
        dialog.exec()

    def clear_imported_csv(self):
        """Exclui o DataFrame importado da memória e reseta o estado da UI."""
        if hasattr(self, 'dados_csv') and self.dados_csv is not None:
            self.dados_csv = None
            self.caminho = None
            self.lblUpload.setText("Nenhum arquivo selecionado")
            self.btnAbrirArquivo.setEnabled(False)
            self.btnExcluirArquivo.setEnabled(False)
            self.btnCalcular.setEnabled(False)
            QMessageBox.information(self, "Sucesso", "Dados do arquivo removidos da memória.")
        else:
            QMessageBox.warning(self, "Aviso", "Nenhum arquivo foi importado.")

    # --- Métodos de Visualização de Dados (Usando dados dos modelos) ---

    def create_emergy_table(self):
        """Cria uma tabela a partir dos resultados do cálculo"""
        layout = QVBoxLayout()
        self.pgGrafico1.setLayout(layout)

        self.tableEmergia = QTableWidget()
        self.tableEmergia.setColumnCount(3)
        self.tableEmergia.setHorizontalHeaderLabels(["Processo", "Emergia Entrada (seJ)", "Emergia Saída (seJ)"])

        relatorio = self.relatorio

        self.tableEmergia.setRowCount(len(relatorio))
        for i, row in relatorio.iterrows():
            self.tableEmergia.setItem(i, 0, QTableWidgetItem(str(row['processo'])))
            self.tableEmergia.setItem(i, 1, QTableWidgetItem(f"{row['entrada']:.2e}"))
            self.tableEmergia.setItem(i, 2, QTableWidgetItem(f"{row['saida']:.2e}"))

        self.tableEmergia.setStyleSheet("""
            QTableWidget {
                background-color: white;
                color: black;
                gridline-color: black;
                border: 1px solid black;
            }
            QHeaderView::section {
                background-color: #dfefff;
                color: black;
                font-weight: bold;
                border: 1px solid black;
            }
            QTableWidget::item:selected {
                background-color: rgb(70, 120, 130);
                color: white;
            }
        """)
        self.tableEmergia.setMinimumSize(400, 200)
        self.tableEmergia.horizontalHeader().setStretchLastSection(True)
        self.tableEmergia.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        layout.addWidget(self.tableEmergia)

        self.swGraficos.addWidget(self.pgGrafico1)
        self.swGraficos.setCurrentWidget(self.pgGrafico1)

    def create_emergy_graph(self):
        """Cria um gráfico de barras a partir dos resultados do cálculo"""
        df_ordenado = self.relatorio.sort_values(by='saida', ascending=False)

        processos = df_ordenado['processo'].tolist()
        emergias = df_ordenado['saida'].tolist()

        figura = Figure(figsize=(6, 4))
        eixo = figura.add_subplot(111)
        eixo.bar(processos, emergias, color="#4FA3A5")

        eixo.set_xlabel("Emergia (seJ)")
        eixo.set_title("Ranking de Consumo de Emergia")

        canvas = FigureCanvas(figura)

        layout = QVBoxLayout()
        self.pgGrafico2.setLayout(layout)
        layout.addWidget(canvas)
        self.swGraficos.setCurrentWidget(self.pgGrafico2)

    def run_emergy_analysis_clicked(self):
        """Inicia todo o processo do cálculo de emergia"""
        caminho = self.caminho
        if caminho:
            self.relatorio = self.emergy_calculator.run_full_emergy_analysis(caminho)
            self.create_emergy_table()
            self.create_emergy_graph
            self.btnExtrairRelatorio.setEnabled(True)
            self.btnGrafico1.setEnabled(True)
            self.btnGrafico2.setEnabled(True)
            self.tabConteudo.setCurrentWidget(self.tabResultado)

    def export_to_excel(self):
        """Exporta o relatório do cálculo e o gráfico apresentado na interface para uma planilha Excel"""
        caminho, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar Relatório com Gráfico",
            filter="Planilha Excel (*.xlsx)"
        )

        if not caminho:
            return

        if not caminho.endswith(".xlsx"):
            caminho += ".xlsx"

        try:
            self.relatorio.to_excel(caminho, index=False, sheet_name="Relatório")

            rel = self.relatorio.sort_values(by="saida", ascending=False)

            fig, ax = plt.subplots(figsize=(6, 4))
            ax.bar(rel["processo"], rel["saida"], color="#4FA3A5")
            ax.set_title("Ranking de Consumo de Emergia")
            ax.set_ylabel("Emergia (seJ)")
            ax.set_xlabel("Processos")
            plt.xticks(rotation=30, ha='right')
            plt.tight_layout()

            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_image:
                plt.savefig(temp_image.name)
                temp_image_path = temp_image.name
            plt.close()

            wb = load_workbook(caminho)
            ws = wb["Relatório"]

            img = ExcelImage(temp_image_path)
            img.anchor = "G2" 

            ws.add_image(img)
            wb.save(caminho)

            os.remove(temp_image_path)

            QMessageBox.information(self, "Sucesso", "Relatório com gráfico exportado com sucesso!")

        except Exception as e:
            QMessageBox.critical(self, "Erro ao Exportar", str(e))

    def closeEvent(self, event):
        """Limpa as variáveis ao fechar o programa"""
        resposta = QMessageBox.question(
            self,
            "Confirmar saída",
            "Tem certeza de que deseja sair?",
            QMessageBox.Yes | QMessageBox.No
        )

        if resposta == QMessageBox.Yes:
            self.relatorio = None
            self.caminho = None
            self.df = None

            event.accept()
        else:
            event.ignore()