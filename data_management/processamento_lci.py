from PySide6.QtWidgets import QFileDialog, QWidget, QMessageBox
import pandas as pd

def selecionar_arquivo_csv(parent: QWidget = None) -> pd.DataFrame:
    """
    Abre uma janela para o usuário selecionar um arquivo CSV e retorna os dados como DataFrame.
    
    :param parent: Referência à janela principal (opcional)
    :return: DataFrame com os dados do CSV ou None se cancelado
    """
    caminho_arquivo, _ = QFileDialog.getOpenFileName(
        parent,
        "Selecionar arquivo CSV",
        "",
        "Arquivos CSV (*.csv);;Todos os arquivos (*)"
    )

    if not caminho_arquivo:
        #QMessageBox.warning(None, "Seleção de Arquivo", "Nenhum arquivo selecionado.")
        return None  # Usuário cancelou

    try:
        df = pd.read_csv(caminho_arquivo)
        return df
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")
        return None
