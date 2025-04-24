from pandas import DataFrame, Series
from pandas.api import types

def is_str(df: DataFrame, column: str) -> bool:
    """ validates if a column in the dataframe is of type str 

        Args:
            df (Dataframe): dataframe
            column (str): column to be validated

        Returns:
            bool
    """
    return types.is_string_dtype(df[column])

def is_numeric(df: DataFrame, column: str) -> bool:
    """ validates if a column in the dataframe is numeric 

        Args:
            df (Dataframe): dataframe
            column (str): column to be validated

        Returns:
            bool
    """
    return types.is_numeric_dtype(df[column])

def df_missing_columns(df: DataFrame, columns: list[str]) -> list[str]:
    """ Validates whether a list of columns is part of the dataframe and returns those that do not exist

        Args:
            df (Dataframe): dataframe
            columns (list[str]): columns to validate

        Returns:
            list[str]
    """
    # Search for columns that do not exist in the data frame and store them in an array, which will then be returned.
    not_exists = [col for col in columns if col not in df.columns]
    return not_exists

def serie_missing_columns(serie: Series, keys: list[str]) -> list[str]:
    """ Validates whether a list of keys is part of the serie and returns those that do not exist

        Args:
            df (Dataframe): dataframe
            keys (list[str]): keys to validate

        Returns:
            list[str]
    """
    # Searches for keys that do not exist in the series and stores them in an array, which will then be returned.
    not_exists = [col for col in keys if col not in serie.keys()]
    return not_exists
