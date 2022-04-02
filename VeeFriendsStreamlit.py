#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 10:21:24 2022

@author: averysmith
"""
# Libraries 
import streamlit as st 
import pandas as pd
import plotly.express as px


# Import data
df = pd.read_csv('veefriends.csv')



# how many tokens are in this project?
num_tokens = len(df['asset_id'].unique())

# what is the total volume?
total_volume = df['sale_price_usd'].sum()




# My title
st.title('VeeFriend Dashboard')

st.write('This is my dashboard for streamlit and the nft hackathon')

col1, col2, col3 = st.columns(3)


col1.metric('Total Number of Tokens', num_tokens)

col2.metric('Total Volume (USD', total_volume)


fig_scatter = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
st.plotly_chart(fig_scatter)











