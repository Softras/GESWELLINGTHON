import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("TABELA DE IDENTIFICAÇÃO DE PERIGOS POR GES") 

st.markdown("***GES-Grupo de Exposição Similares*** \n**GHE: 01 - ADMINISTRATIVO**  \n**SETOR: ADMINISTRATIVO**")

# Lê o CSS externo
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Colunas da tabela
colunas = [
    "Agente / Tipo", "Perigo / Fonte de Riscos", "Dano", "Padrões Legais / Limite de Exposição",
    "Fonte Geradora", "POAD/EPC", "Eficaz POAD/EPC (S/N)", "EPI", "CA", "Atenuação / Fator de Proteção",
    "Eficaz EPI (S/N)", "Intensidade / Concentração", "Técnica Utilizada", "Frequência", "Severidade",
    "Avaliação do Risco", "IR", "Definições de ações necessárias e prioridades", "Critério para monitorar a exposição"
]

dados = [
    ["Ergonômico", "Postura incorreta, esforço repetitivo", "Dores lombares e LER/DORT", "NR17",
     "Atividades administrativas.", "Ordem de serviços, Análise Ergonômica do Trabalho (AET).", "NA",
     "NA", "NA", "NA", "NA", "NA", "QUALITATIVO", "Habitual", "Médio", "RISCO PURO", 0,
     "Manter controle existente. (P2)", "Manter controle existente"],
     
    ["Ergonômico", "Pegar a mercadoria de forma inadequada.", "Lesão muscular", "NR17",
     "Recebimento de materiais diversos", "Integração com TST Treinamento de ergonomia.", "NA",
     "NA", "NA", "NA", "NA", "NA", "QUALITATIVO", "Intermitente", "Médio", "BAIXO", 0,
     "Nenhum controle adicional é necessário. Manter controle existente (P2)", "Nenhum controle adicional é necessário"],
    
    ["Ergonômico", "Condições ambientais inadequadas (Temperatura e iluminação)", "Stress, fadiga.", "NR17",
     "Atividade administrativa da empresa.", "Análise Ergonômica do Trabalho (AET).", "NA",
     "NA", "NA", "NA", "NA", "401 LUX", "NHO 011 FUNDACENTRO e NR-17", "Habitual", "Médio", "Moderado", 0,
     "Manter controle existente. (P2)", "Manter controle existente"],
    
    ["Acidente", "Queda do mesmo nível", "Fratura, lesões", "NA",
     "Percorrer local", "Integração de portaria, Integração com TST Treinamento de escorregão, tropeço e queda.", "NA",
     "Calçado de segurança", "NA", "NA", "Sim", "NA", "QUALITATIVO", "Habitual", "Médio", "Moderado", 0,
     "Manter controle existente. (P2)", "Manter controle existente"],
    
    ["Acidente", "Piso escorregadio / irregular", "Lesões múltiplas, escoriações", "NA",
     "Percorrer local", "Integração de portaria, Integração com TST Treinamento de escorregão, tropeço e queda.", "NA",
     "Calçado de segurança", "NA", "NA", "Sim", "NA", "QUALITATIVO", "Habitual", "Médio", "Moderado", 0,
     "Manter controle existente. (P2)", "Manter controle existente"]
]

df = pd.DataFrame(dados, columns=colunas)

# Função para colorir a coluna "Avaliação do Risco"
def colorir_risco(val):
    cor = ''
    if val == 'RISCO PURO':
        cor = 'background-color: red; color: white;'
    elif val == 'Moderado':
        cor = 'background-color: yellow; color: black;'
    elif val == 'BAIXO':
        cor = 'background-color: lightgreen; color: black;'
    return cor

styler = df.style.applymap(colorir_risco, subset=["Avaliação do Risco"])
styler = styler.hide(axis="index")  

st.markdown(styler.to_html(), unsafe_allow_html=True)
