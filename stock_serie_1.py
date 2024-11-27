import os
import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

# Criar a pasta "Valor" para salvar os arquivos
def create_folder(folder_name="Valor"):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Função para baixar dados de ativos
def download_data(tickers, start_date, end_date):
    create_folder()  # Certifica-se de que a pasta "Valor" existe
    data = {}
    for name, ticker in tickers.items():
        # Adiciona o código de identificação ao nome do arquivo
        file_name = f"Valor/{name}_{ticker}_{start_date}_{end_date}.csv"
        df = yf.download(ticker, start=start_date, end=end_date)
        df.to_csv(file_name)  # Salvar em arquivos individuais
        data[name] = df
    return data


# Função para plotar gráficos
def plot_data(data):
    st.header("Gráfico Interativo")
    combined_data = pd.DataFrame()
    for name, df in data.items():
        df['Ativo'] = name
        df = df[['Ativo', 'Close']].rename(columns={'Close': 'Preço'})
        combined_data = pd.concat([combined_data, df])
    fig = px.line(
        combined_data.reset_index(), 
        x='Date', 
        y='Preço', 
        color='Ativo', 
        title="Histórico de Preços",
        labels={'Preço': 'Preço (em moeda)', 'Date': 'Data'}
    )
    st.plotly_chart(fig)

# Configurações da aplicação
st.title("Baixar Histórico de Ativos")
st.sidebar.header("Configurações")

# Opções de ativos

ativos_por_categoria = {
    "Moedas": {
        "Dólar_Real": "USDBRL=X",
        "Euro_Real": "EURBRL=X",
        "Euro_Dólar": "EURUSD=X",
        "Bitcoin_Dólar": "BTC-USD",
        "GBP/USD": "GBPUSD=X",
        "USD/JPY": "JPY=X"
    },
    "Bolsas": {
        "S&P 500": "^GSPC",
        "Dow Jones Industrial Average": "^DJI",
        "NASDAQ Composite": "^IXIC",
        "Nasdaq 100": "NQ=F",
        "Russell 2000": "^RUT",
        "FTSE 100 GBP": "^FTSE",
        "Nikkei 225 Osaka": "^N225",
        "IBOVESPA": "^BVSP",
        "IPC MEXICO": "^MXX"
    },
    "Commodities": {
        "Ouro": "GC=F",
        "Prata": "SI=F",
        "Petróleo": "CL=F"
    },
    "Ações": {
        "Amazon": "AMZN",
        "Apple": "AAPL",
        "Tesla": "TSLA",
        "Microsoft": "MSFT",
        "Google": "GOOGL",
        "Meta (Facebook)": "META",
        "Netflix": "NFLX",
        "NVIDIA": "NVDA"
    }
}


# Selecionar ativos
#ativos_selecionados = st.sidebar.multiselect("Escolha os ativos para download:", list(ativos.keys()))

# Selecionar categoria
categoria_selecionada = st.sidebar.selectbox("Escolha a categoria:", list(ativos_por_categoria.keys()))

# Selecionar ativos dentro da categoria
if categoria_selecionada:
    ativos_selecionados = st.sidebar.multiselect(
        "Escolha os ativos:",
        list(ativos_por_categoria[categoria_selecionada].keys())
    )
    ativos_escolhidos = {ativo: ativos_por_categoria[categoria_selecionada][ativo] for ativo in ativos_selecionados}





# Escolher intervalo de datas
start_date = st.sidebar.date_input("Data de início", value=pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input("Data de fim", value=pd.to_datetime("today"))

# Botão para executar
if st.sidebar.button("Baixar Dados e Gerar Gráfico"):
    if ativos_selecionados:
        st.write(f"Baixando dados para os ativos: {ativos_selecionados}")
        ativos_selecionados_dict = {ativo: ativos_escolhidos[ativo] for ativo in ativos_selecionados}
        data = download_data(ativos_selecionados_dict, start_date, end_date)
        st.success("Dados baixados com sucesso! Arquivos CSV gerados na pasta 'Valor'.")
        plot_data(data)
    else:
        st.error("Por favor, selecione pelo menos um ativo.")
