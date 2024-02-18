import streamlit as st
import pandas as pd

def main():
    st.title("Voter Data Analysis App")

    # File upload section
    st.sidebar.title("Upload File")
    uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        # Load the data
        df = pd.read_csv(uploaded_file)

        # Display the uploaded data
        st.subheader("Uploaded Data")
        st.write(df)

        # Perform analysis or display specific columns
        # You can add more functionality here based on your requirements

if __name__ == "__main__":
    main()
