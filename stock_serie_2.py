import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import ccf

# Função para carregar dados da pasta "Valor"
def carregar_dados(pasta="Valor"):
    arquivos = [f for f in os.listdir(pasta) if f.endswith(".csv")]
    return {arq: pd.read_csv(os.path.join(pasta, arq), parse_dates=["Date"], index_col="Date") for arq in arquivos}

# Função para analisar periodicidade
def analisar_periodicidade(df, freq):
    df_resample = df['Close'].resample(freq).mean()  # Média por periodicidade
    return df_resample

# Função para decomposição sazonal
def decompor_serie(df):
    result = seasonal_decompose(df['Close'], model='additive', period=30)  # Exemplo de 30 dias
    return result

# Streamlit
st.title("Análise de Séries Temporais")

# Carregar arquivos da pasta "Valor"
dados = carregar_dados()
opcoes = list(dados.keys())

# Selecionar ativo para análise
arquivo_selecionado = st.selectbox("Selecione o ativo para análise:", opcoes)
if arquivo_selecionado:
    df = dados[arquivo_selecionado]
    st.write(f"### Dados de: {arquivo_selecionado}")
    st.line_chart(df['Close'], use_container_width=True)

    # Selecionar periodicidade
    periodicidade = st.radio("Escolha a periodicidade:", ["Semanal", "Mensal", "Anual"])
    freq_map = {"Semanal": "W", "Mensal": "M", "Anual": "Y"}
    df_periodico = analisar_periodicidade(df, freq_map[periodicidade])

    # Mostrar resultados
    st.write(f"### Média por {periodicidade.lower()}:")
    st.line_chart(df_periodico, use_container_width=True)

    # Decomposição sazonal
    st.write("### Decomposição Sazonal:")
    decomposicao = decompor_serie(df)
    fig, axes = plt.subplots(4, 1, figsize=(10, 8), sharex=True)
    decomposicao.observed.plot(ax=axes[0], title="Observado")
    decomposicao.trend.plot(ax=axes[1], title="Tendência")
    decomposicao.seasonal.plot(ax=axes[2], title="Sazonalidade")
    decomposicao.resid.plot(ax=axes[3], title="Resíduo")
    st.pyplot(fig)


# Seleção de duas séries para calcular correlação
st.write("### Correlação entre Séries")
series_para_correlacao = st.multiselect("Escolha duas séries para análise de correlação:", list(dados.keys()), max_selections=2)

if len(series_para_correlacao) == 2:
    df1 = dados[series_para_correlacao[0]]['Close']
    df2 = dados[series_para_correlacao[1]]['Close']
    # Alinhamento das séries no tempo
    df1, df2 = df1.align(df2, join='inner')

    # Calcular e exibir correlação de Pearson
    correlacao = df1.corr(df2)
    st.write(f"Correlação de Pearson: {correlacao:.2f}")


# Função de cross-correlation
if len(series_para_correlacao) == 2:
    cross_corr = ccf(df1, df2, adjusted=False)
    st.write("### Cross-Correlation")
    st.line_chart(cross_corr)

    # Mostrar defasagens máximas
    max_corr_lag = (cross_corr.argmax(), cross_corr.max())
    st.write(f"Máxima correlação ocorre com defasagem de {max_corr_lag[0]}: {max_corr_lag[1]:.2f}")
