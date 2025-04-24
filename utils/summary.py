import io
import pandas as pd

def dataframe_summary(dataframe):
    """
    Prints a detailed summary of the given pandas DataFrame.

    This includes:
    - Shape (rows x columns)
    - Count of duplicate rows
    - Total memory usage in KB/MB
    - Count and percentage of missing values per column
    - Basic info (data types, non-null counts, etc)
    - Statistical summary of numerical columns

    Parameters:
        dataframe (pd.DataFrame): The DataFrame to summarize.

    Returns:
        None

    Raises:
        TypeError: If input is not a pandas DataFrame.
    """
    try:
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError('Input must be a pandas DataFrame.')

        print('='*70)
        print('DataFrame Summary'.center(70))
        print('='*70)
        
        # Shape
        print(f'Shape: {dataframe.shape[0]} rows × {dataframe.shape[1]} columns')
        print('='*70)
    
        # Duplicates
        dup_count = dataframe.duplicated().sum()
        print(f'Duplicate Rows: {dup_count}')
        print('='*70)

        # Memory usage
        memory_usage = dataframe.memory_usage(deep=True).sum()/1024
        if memory_usage > 1024:
            print(f'Memory Usage: {memory_usage/1024:.2f}MB')
        else:
            print(f'Memory Usage: {memory_usage:.2f}KB')
        print('='*70)

        # Missing values
        print('Missing Values:')
        nulls = dataframe.isnull().sum()
        if nulls.sum() == 0:
            print('No missing values')
        else:
            missing_df = dataframe.isnull().sum().to_frame(name='Missing Values')
            missing_df['%'] = 100 * missing_df['Missing Values'] / len(dataframe)
            print(missing_df[missing_df['Missing Values'] > 0])
        print('='*70)
    
        # DataFrame Info
        print('DataFrame Info:')
        buffer = io.StringIO()
        dataframe.info(buf=buffer)
        info_str = buffer.getvalue()
        print(info_str,end='')
        print('='*70)

        # DataFrame Description
        print('DataFrame Description:')
        numerical_cols = dataframe.select_dtypes(include=['number']).columns
        if len(numerical_cols) == 0:
            print('No numerical columns in the dataframe')
        else:
            with pd.option_context('display.float_format', '{:.2f}'.format,
                       'display.width', 200,
                       'display.max_columns', None):
                summary = dataframe[numerical_cols].describe().round(2)
                print(summary)

    except TypeError as e:
        print(e)