import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

# Função para baixar dados de ativos
def download_data(tickers, start_date, end_date):
    data = {}
    for ticker in tickers:
        df = yf.download(ticker, start=start_date, end=end_date)
        df.to_csv(f"{ticker}.csv")  # Salvar em arquivos individuais
        data[ticker] = df
    return data

# Função para plotar gráficos
def plot_data(data):
    combined_data = pd.DataFrame()
    for ticker, df in data.items():
        df['Ticker'] = ticker
        df = df[['Ticker', 'Close']].rename(columns={'Close': 'Price'})
        combined_data = pd.concat([combined_data, df])
    fig = px.line(
        combined_data.reset_index(), 
        x='Date', 
        y='Price', 
        color='Ticker', 
        title="Histórico de Preços",
        labels={'Price': 'Preço', 'Date': 'Data'}
    )
    st.plotly_chart(fig)

# Configurações da aplicação
st.title("Baixar Histórico de Ativos")
st.sidebar.header("Configurações")

# Opções de ativos
ativos = {
    "Dólar": "USDBRL=X",
    "Euro": "EURBRL=X",
    "Bitcoin": "BTC-USD",
    "Ouro": "GC=F",
    "Prata": "SI=F",
    "Petróleo": "CL=F",
    "Amazon": "AMZN",
    "Apple": "AAPL",
    "Tesla": "TSLA",
    "Microsoft": "MSFT"
}

# Selecionar ativos
ativos_selecionados = st.sidebar.multiselect("Escolha os ativos para download:", list(ativos.keys()))

# Escolher intervalo de datas
start_date = st.sidebar.date_input("Data de início", value=pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input("Data de fim", value=pd.to_datetime("today"))

# Botão para executar
if st.sidebar.button("Baixar Dados e Gerar Gráfico"):
    if ativos_selecionados:
        st.write(f"Baixando dados para os ativos: {ativos_selecionados}")
        tickers = [ativos[ativo] for ativo in ativos_selecionados]
        data = download_data(tickers, start_date, end_date)
        st.success("Dados baixados com sucesso! Arquivos CSV gerados.")
        plot_data(data)
    else:
        st.error("Por favor, selecione pelo menos um ativo.")
