import pandas as pd

# Define the function to count vowels
def count_vowels(string):
    '''
    This function counts the number of vowels in a string
    Parameters:
        string (str): The string to count the vowels from
    
    Returns:
        int: The number of vowels in the string
    '''
    vowels = 'aeiouAEIOU'
    return sum(1 for char in string if char in vowels)


# Load imdb dataset from the data directory 
df = pd.read_csv('data/imdb.csv')

# Apply the function to the 'Title' column to create the 'Vowels' column
df['Vowels'] = df['review'].apply(count_vowels)

# Display the dataframe
print(df)