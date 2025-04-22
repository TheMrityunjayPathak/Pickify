import pandas as pd

def merge_dataframe(first_dataframe, second_dataframe, column):
    """
    Merges two pandas DataFrame on a common column.

    Parameters:
        first_dataframe (pd.DataFrame): The first DataFrame to merge.
        second_dataframe (pd.DataFrame): The second DataFrame to merge.
        column (str): Name of the column to merge the DataFrames on. Column must exist in both the DataFrames.

    Returns:
        pd.DataFrame: A DataFrame after merging first_dataframe and second_dataframe on a common column.

    Raises:
        TypeError: If any of the input is not a pandas DataFrame.
        KeyError: If the specified column does not exist in both the DataFrames.
    """
    try:
        if not isinstance(first_dataframe, pd.DataFrame) or not isinstance(second_dataframe, pd.DataFrame):
            raise TypeError("Both inputs must be a pandas DataFrame.")
        if column not in first_dataframe.columns or column not in second_dataframe.columns:
            raise KeyError(f"Column '{column}' must exist in both the DataFrames.")
        
        df = first_dataframe.merge(second_dataframe, on=column)
        return df
    
    except TypeError as e:
        print(e)
        return pd.DataFrame()
    except KeyError as e:
        print(e.args[0])
        return pd.DataFrame()