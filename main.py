import yfinance as yf
from pytickersymbols import PyTickerSymbols
import pandas as pd
import os, streamlit as st
import plotly.graph_objects as go
import time


st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"]{
        min-width: 450px;
        max-width: 450px;
    }
    """,
    unsafe_allow_html=True,
)   


stock_data = PyTickerSymbols()
countries = stock_data.get_all_countries()
indices = stock_data.get_all_indices()
industries = stock_data.get_all_industries()

all_stock_data = stock_data.get_all_stocks()

stock_df = pd.DataFrame(all_stock_data)


# Indice select
index_option = st.sidebar.selectbox(
   "Which indice do you want to see?",
   (indices),
   index=None,
   placeholder="Select a stock...",
)


filtered_by_indices = stock_df[stock_df['indices']
                               .apply(lambda x: any([k in x for k in [index_option]]))]

#st.write(filtered_by_indices)

# Ticker select
ticker_option = st.sidebar.selectbox(
   "Which stock do you want to see?",
    (filtered_by_indices.name.to_list()),
    index=None,
   placeholder="Select a stock...",
)

filtered_symbol = filtered_by_indices[filtered_by_indices['name'] == ticker_option].symbol.to_list()



try:

    f"""
    #### {filtered_symbol[0]}
    Company:  {ticker_option} 
    """


    col1, col2 = st.columns(2)

    with(col1):
        period = st.radio(
        "Please select a period",
        ["1d","1mo","3mo","6mo","1y","2y","5y","10y","ytd","max"],
        index=None,
        horizontal=True
)
    with(col2):
        interval = st.radio(
        "Please select an interval",
        ["1m","5m","15m","30m","1h","1d","5d","1wk","1mo","3mo"],
        index=None,
        horizontal=True
)
    

    
    data = yf.download(tickers= filtered_symbol, period=period, interval=interval)

    fig = go.Figure(data=[go.Candlestick(x=data.index,
                                    open=data['Open'],
                                    high=data['High'],
                                    low=data['Low'],
                                    close=data['Close'])])

    st.plotly_chart(fig, use_container_width=True)


    st.dataframe(data)
except:
    st.header("")


