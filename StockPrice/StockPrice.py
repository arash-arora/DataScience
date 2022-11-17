#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
import streamlit as st
import pandas as dp


# In[ ]:

st.write("""
# Simple Stock Price App""")

option = st.selectbox(
     'Choose',
     ('GOOGLE', 'APPLE', 'NVIDEA', "CSCO", "AMZN", "AMD", "TSLA", "F", "INTC", "MSFT", "UBER"))

st.write("""
Shown are the stock closing price and volume of 
""",option)

if option=="GOOGLE":
    option="GOOGL"
elif option=="APPLE":
    option="AAPL"
elif option=="NVIDEA":
    option="NVDA"
elif option=="CISCO":
    option="CSCO"
elif option=="AMAZON":
    option="AMZN"
elif option=="AMD":
    option="AMD"
elif option=="TESLA":
    option="TSLA"
elif option=="FORD":
    option="F"
elif option=="INTEL":
    option="INTC"
elif option=="MICROSOFT":
    option="MSFT"
elif option=="UBER":
    option="UBER"

tickerSymbol = option

tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')


st.write(
    """
    ### Closing Price
    """
)
st.line_chart(tickerDF.Close)
st.write(
    """
    ### Volume Price
    """
)
st.line_chart(tickerDF.Volume)

