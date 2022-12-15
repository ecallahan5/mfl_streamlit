import numpy as np
import pandas as pd
import streamlit as st

st.header('Playoffs!')

# Example 1

st.write('Wild Card 1')
wc1 = pd.DataFrame({
     'Team': ["Maize 'N Blue", "Moneyballers"],
     'Win Probability': [56.37, 43.63]
     })
st.write(wc1)
# Example 2

st.write('Wild Card 2')
wc2 = pd.DataFrame({
     'Team': ["The Gurley Tates", "The Van Buren Boys"],
     'Win Probability': [37.09, 62.91]
     })
st.write(wc2)

st.header('Extra Pick!')
dfl = pd.DataFrame({
     'Team': ["Muthah Tucker", "You Carr'd Be Kidding", "Hidden Talents", "Hurricane",  "Cromarties Bastards", "Shoot em Into the Sun"],
     'Win Probability': [0.82, 14.96, 5.31, 6.13, 27.81, 44.97]
     })
st.bar_chart(dfl, x='Team', y='Win Probability')