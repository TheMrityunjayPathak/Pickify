import ast
import pandas as pd

def extract_genre(obj):
    """
    Converts a string representation of a Python object into Original Python object and extract the value of 'name' key.

    Parameters:
        obj (str): A string representation of a list of dictionaries, where each dictionary must contain a 'name' key.

    Returns:
        pd.Series: A Series containing list of genres corresponding to the 'name' key of each dictionary.

    Raises:
        TypeError: If input is not a string.
        ValueError: If input string does not represents a list of dictionaries.
    
    Example:
        >>> extract_genre('[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}]')
        ['Action', 'Adventure']
    """
    try:
        if not isinstance(obj, str):
            raise TypeError('Input must be a string.')
        original_obj = ast.literal_eval(obj)
        if not isinstance(original_obj, list) or not all(isinstance(i, dict) for i in original_obj):
            raise ValueError('Input must be a list of dictionaries.')
        return [dct['name'] for dct in original_obj]
    except (TypeError, ValueError) as e:
        print(e)
        return pd.Series()