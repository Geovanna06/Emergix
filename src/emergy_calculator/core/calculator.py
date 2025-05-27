import pandas as pd

class EmergyCalculator:

    def load_and_calculate_emergy(self, caminho_csv):
        """Carrega os dados e calcula a emergia"""
        df = pd.read_csv(caminho_csv)
        df['emergia'] = df['quantidade'] * df['transformidade']
        return df
    
    def organize_emergy_data_by_process(self, df):
        """Organiza a emergia dos dados por processo"""
        processos = df['processo'].unique()
        estrutura = {}

        for processo in processos:
            entradas = df[(df['processo'] == processo) & (df['tipo_fluxo'] == 'entrada')]
            saidas = df[(df['processo'] == processo) & (df['tipo_fluxo'] == 'saida')]
            estrutura[processo] = {
                'entradas': entradas,
                'saidas': saidas
            }
        
        return estrutura
    
    def apply_emergy_methodology_rules(self, estrutura, df):
        """Aplica as regras de emergia e retorna o relatório do cálculo"""
        resultados = []

        for processo, dados in estrutura.items():
            entradas = dados['entradas']
            saidas = dados['saidas'].copy()
            
            # Regra 4 – Feedback: zerar emergia se a origem for o mesmo processo
            saidas.loc[saidas['origem'] == saidas['destino'], 'emergia'] = 0

            # Regra 2 – Coprodutos: só considerar o de maior emergia por origem
            coprodutos = saidas[saidas['origem'] == saidas['destino']]

            if not coprodutos.empty:
                maior_emergia = coprodutos.loc[coprodutos['emergia'].idxmax()]
                coprodutos_filtrados = pd.DataFrame([maior_emergia])
                outros = saidas[saidas['origem'] != saidas['destino']]
                saidas = pd.concat([coprodutos_filtrados, outros])
            
            # Regra 1 – Conservação
            emergia_entrada = entradas['emergia'].sum()
            emergia_saida = saidas['emergia'].sum()

            if emergia_saida > emergia_entrada:
                status = "VIOLAÇÃO"
            else:
                status = "OK"

            resultados.append({
                'processo': processo,
                'entrada': emergia_entrada,
                'saida': emergia_saida,
                'status': status
            })

        return pd.DataFrame(resultados)
    
    def run_full_emergy_analysis(self, caminho_csv):
        """Executa todo o processo do cálculo de emergia"""
        df = self.load_and_calculate_emergy(caminho_csv)
        estrutura = self.organize_emergy_data_by_process(df)
        relatorio = self.apply_emergy_methodology_rules(estrutura, df)
        return relatorio
    
