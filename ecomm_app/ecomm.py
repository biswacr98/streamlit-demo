import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

def main():
    st.title("This is app for ecomm I am creating")
    st.sidebar.title("you can upload your file here")

    upload_file = st.sidebar.file_uploader("Upload your file here", type=['csv', 'xlsx'])

    if upload_file is not None:
        try:
            if upload_file.name.endswith('.csv'):
                data = pd.read_csv(upload_file)
            else: 
                data = pd.read_excel(upload_file)
            st.sidebar.success("File uploaded successfully")

            st.subheader("I am going to show you data details")
            st.dataframe(data.head())

            st.subheader("Let's see some more details about the data")
            st.write("shape of data", data.shape)
            st.write("the column name inside data is", data.columns)
            st.write("missing values into column", data.isnull().sum())

            st.subheader("I will show you bit of stats")
            st.write(data.describe())

        except Exception as e:
            st.sidebar.error("Something went wrong")

if __name__ == "__main__":
    main()
