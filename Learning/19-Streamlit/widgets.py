import streamlit as st
import pandas as pd
st.title("Streamlit Widgets")

name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 0, 100, 25)
status = st.selectbox("Select your status:", ["Single", "Married", "Divorced"])
if name:
    st.write(f"Hello, {name}! You are {age} years old and {status}.")

df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': ['A', 'B', 'C', 'D']
})
st.write("Here is a DataFrame:")
df.to_csv("sample_data.csv", index=False)  # Save DataFrame to CSV
st.write(df)
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:")
    st.write(data)