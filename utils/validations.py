from pandas import DataFrame, Series
from pandas.api import types

def is_str(df: DataFrame, column: str) -> bool:
    return types.is_string_dtype(df[column])

def is_numeric(df: DataFrame, column: str) -> bool:
    return types.is_numeric_dtype(df[column])

def df_missing_columns(df: DataFrame, columns: list[str]) -> list[str]:
    not_exists = [col for col in columns if col not in df.columns]
    return not_exists

def serie_missing_columns(serie: Series, columns: list[str]) -> list[str]:
    not_exists = [col for col in columns if col not in serie.keys()]
    return not_exists
