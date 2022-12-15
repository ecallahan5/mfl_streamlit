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


