import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px


st.header('Playoffs!')
st.markdown("""---""")
st.header('This Week\'s Games')
# Example 1


wc1 = pd.DataFrame({
     'Team': ["Maize 'N Blue", "Moneyballers"],
     'Win Probability': [56.37, 43.63]
     })
fig = px.pie(wc1, values='Win Probability', names='Team', title='Wild Card 1')
st.plotly_chart(fig, use_container_width=True)
# Example 2


wc2 = pd.DataFrame({
     'Team': ["The Gurley Tates", "The Van Buren Boys"],
     'Win Probability': [37.09, 62.91]
     })
fig = px.pie(wc2, values='Win Probability', names='Team', title='Wild Card 1')
st.plotly_chart(fig, use_container_width=True)

st.markdown("""---""")
st.header('Title Chances')
df_ch = pd.DataFrame({
     'Team': ["Maize 'N Blue", "Moneyballers", "The Gurley Tates", "The Van Buren Boys",  "Brooklyn Big Blue", "The Uncaught Exceptions"],
     'Win Probability': [8.91, 3.81, 2.62, 8.8, 48.06, 27.80]
     })
st.bar_chart(df_ch, x='Team', y='Win Probability')

st.markdown("""---""")
st.header('Expected Playoff Winnings')
df_money = pd.DataFrame({
     'Team': ["Maize 'N Blue", "Moneyballers", "The Gurley Tates", "The Van Buren Boys",  "Brooklyn Big Blue", "The Uncaught Exceptions"],
     '$$': [58, 31, 25, 66, 213, 162]
     })
st.bar_chart(df_money, x='Team', y='$$')


st.markdown("""---""")
st.header('Extra Pick!')
dfl = pd.DataFrame({
     'Team': ["Muthah Tucker", "You Carr'd Be Kidding", "Hidden Talents", "Hurricane",  "Cromarties Bastards", "Shoot em Into the Sun"],
     'Probability': [0.82, 14.96, 5.31, 6.13, 27.81, 44.97]
     })
st.bar_chart(dfl, x='Team', y='Probability')
