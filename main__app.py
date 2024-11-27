import streamlit as st
import pandas as pd
import yfinance as yf
import os
from datetime import datetime


st.set_page_config(layout="wide")
col1, col2, col3 = st.columns([1,9,1])


with col2:
    st.markdown('# App de construção do modelo')

    tab1,tab2,tab3 = st.tabs(["Leitura dos Stocks datasets", 
                            "Update dos Stocks datasets",
                             "Shows dos Stocks datasets"
                            ])
    
    with tab1:
        st.header("Leitura dos Stocks datasets")

        try:
            uploaded_stock1 = st.file_uploader("Upload a CSV dataset",  type=["csv"])
            if uploaded_stock1 is not None:
                Objeto_stock = pd.read_csv(uploaded_stock1, sep =',', parse_dates=True)
                Objeto_stock['Date'] = pd.to_datetime(Objeto_stock['Date'])
                #Objeto_stock = Objeto_stock.set_index('Date')
                st.dataframe(Objeto_stock.head(), use_container_width=True)
                st.dataframe(Objeto_stock.tail(), use_container_width=True)

        except:
            st.stop()

    with tab2:
        st.header("Update dos Stocks datasets")

        pass

    with tab3:
        st.header("Shows dos Stocks datasets")

        pass