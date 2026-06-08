import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit App")   


st.write("This is a simple Streamlit app to demonstrate its capabilities.")

df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': ['A', 'B', 'C', 'D']
})

st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Column 1', 'Column 2', 'Column 3']
)
st.line_chart(chart_data)