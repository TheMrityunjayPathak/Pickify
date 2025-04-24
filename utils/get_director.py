import ast
import pandas as pd

def extract_director(obj):
    """
    Converts a string representation of a Python object into Original Python object and extract 'name' key only where 'job' key is equal to 'Director'.

    Parameters:
        obj (str): A string representation of a list of dictionaries, where each dictionary must contain a 'name' key.

    Returns:
        pd.Series: A Series containing list of directors corresponding to the 'name' key of each dictionary, where 'job' key is equal to 'Director'.

    Raises:
        TypeError: If input is not a string.
        ValueError: If input string does not represents a list of dictionaries.
      
    Example:
        >>> extract_director('[{"name": "James Cameron", "job": "Director"}, {"name": "Johnny Depp", "job": "Actor"}]')
        ['James Cameron']

    """
    try:
        if not isinstance(obj, str):
            raise TypeError('Input must be a string.')
        original_obj = ast.literal_eval(obj)
        if not isinstance(original_obj, list) or not all(isinstance(i, dict) for i in original_obj):
            raise ValueError('Input must be a list of dictionaries.')
        director_list = []
        for i in original_obj:
            if i['job'] == 'Director':
                director_list.append(i['name'])
                break
        return director_list
    except (TypeError, ValueError) as e:
        print(e)
        return pd.Series()