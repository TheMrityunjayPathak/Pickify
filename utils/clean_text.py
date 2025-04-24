import pandas as pd

def remove_spaces(dataframe, column):
    """
    Removes spaces between words from each row in a column of the DataFrame, where each row must be a list of strings.

    Parameters:
        dataframe (pd.DataFrame): The DataFrame containing the column.
        column (str): Name of the column from which spaces will be removed, must contain list of strings.

    Returns:
        pd.Series: A Series where spaces between words from each row of a column has been removed.

    Raises:
        TypeError: If input is not a pandas DataFrame.
        KeyError: If column does not exist in the DataFrame.
        ValueError: If each row in the column does not contain a list of strings.
    """
    try:
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError('Input must be a pandas DataFrame.')
        if column not in dataframe.columns:
            raise KeyError(f"Column '{column}' not exist in DataFrame.")
        for rows in dataframe[column]:
            if not isinstance(rows, list) or not all(isinstance(val, str) for val in rows):
                raise ValueError(f"Each row in column '{column}' must be a list of strings.")
        return dataframe[column].apply(lambda x: [item.replace(' ','') for item in x])
    except TypeError as e:
        print(e)
        return pd.Series()
    except KeyError as e:
        print(e.args[0])
        return pd.Series()
    except ValueError as e:
        print(e)
        return pd.Series()