import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Function to create and plot histogram
def create_histogram(dataframe, column_name):
    '''
    Function to create and plot histogram
        Args:
            dataframe: Pandas dataframe
            column_name: Name of the column to plot
        Returns:
            None
    '''
    plt.figure(figsize=(10, 4))
    plt.hist(dataframe[column_name].dropna(), bins=20, alpha=0.7, color='blue')
    plt.title('Histogram of Ages')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    st.pyplot(plt)


def main():
    '''
    Main Streamlit app
    '''
    st.title('CSV File Upload & Histogram Plotting')

    # File uploader widget
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file)

        # Check if 'Age' column is in the dataframe
        if 'Age' in dataframe.columns:
            create_histogram(dataframe, 'Age')
        else:
            st.error("The uploaded file does not contain an 'Age' column.")

# Run the main function
if __name__ == '__main__':
    main()