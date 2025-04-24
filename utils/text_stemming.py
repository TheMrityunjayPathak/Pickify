import pandas as pd
from nltk.stem import PorterStemmer
ps = PorterStemmer()

def stem(text):
    """
    Perform stemming on a given text using PorterStemmer.

    Parameters:
        text (str): A string of text to be stemmed.

    Returns:
        pd.Series: A Series with each word in each row stemmed and joined by spaces.

    Raises:
        TypeError: If input is not string.

    Example:
        >>> stem("running jumped flying")
        'run jump fli'
    """
    try: 
        if not isinstance(text, str):
            raise TypeError('Input must be a string.')
        return ' '.join([ps.stem(word) for word in text.split()])
    except TypeError as e:
        print(e)
        return pd.Series()