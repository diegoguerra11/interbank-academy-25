from typing import Literal

from pandas import DataFrame

def sum_by_column(df: DataFrame, column: str, types: list[str]):
    """ Allows the sum of the values ​​of a column according to the type """
    sum = 0
    
    for type in types: 
        sum += df[column][type]

    return sum

def sub_by_column(df: DataFrame, column: str, types: list[str]):
    """ Allows the subtraction of the values ​​of a column according to the type """
    sub = 0
    
    for type in types:
        if(sub == 0): 
            sub = df[column][type]
            continue

        sub -= df[column][type]

    return sub

def calculate_by_grouped(
    df: DataFrame,
    group_by: str,
    operation: Literal["sum", "sub"],
    column: str,
    types: list[str]
) -> float:
    """ Allows you to group based on one column, 
        then perform mathematical operations based on another column.
    """
    df_by_type = df.groupby(group_by)

    sum_by_type = df_by_type.sum()

    result = 0

    match operation:
        case "sum": result = sum_by_column(sum_by_type, column, types)
        case "sub": result = sub_by_column(sum_by_type, column, types)
        case _: result = 0

    return round(result, 2)

def count_by_column(df: DataFrame, column: str) -> dict:
    """ Counts the number of records by the selected column """
    return df[column].value_counts().to_dict()