from typing import Literal
from pandas import DataFrame

def add_by_column(df: DataFrame, column: str, types: list[str]) -> float:
    """ Allows the addition of the values ​​of a column according to the type 
           
        Args:
            df (Dataframe): dataframe
            column (str): column to which the addition will be applied
            categories(list[str]): categories on which the addition will be performed

        Returns:
            float
    """
    sum = 0
    
    for type in types: 
        sum += df[column][type]

    return sum

def sub_by_column(df: DataFrame, column: str, categories: list[str]) -> float:
    """ Allows the subtraction of the values ​​of a column according to the category 
        
        Args:
            df (Dataframe): dataframe
            column (str): column to which the subtraction will be applied
            categories(list[str]): categories on which the subtraction will be performed

        Returns:
            float
    """
    sub = 0
    
    for type in categories:
        if(sub == 0): 
            sub = df[column][type]
            continue

        sub -= df[column][type]

    return sub

def calculate_by_grouped(
    df: DataFrame,
    group_by: str,
    operation: Literal["add", "sub"],
    column: str,
    categories: list[str]
) -> float:
    """ Allows you to group based on one column, 
        then perform mathematical operations based on another column.

        Args:
            df (Dataframe): dataframe
            group_by (str): the categorical column used to group the dataframe
            operation (Literal["add", "sub"]): Mathematical operation applied to a numeric column (add -> addition or sub -> substraccion)
            column (str): numeric column the operation will be applied to
            categories(list[str]): categories on which the operation will be performed

        Returns:
            float
    """
    df_by_type = df.groupby(group_by)

    sum_by_type = df_by_type.sum()

    result = 0

    match operation:
        case "sum": result = add_by_column(sum_by_type, column, categories)
        case "sub": result = sub_by_column(sum_by_type, column, categories)
        case _: result = 0

    return round(result, 2)

def count_by_column(df: DataFrame, column: str) -> dict:
    """ Counts the number of records by the selected column 
        
        Args:
            df (Dataframe): dataframe
            column (str): column by which the count by value will be performed

        Returns:
            dict
    """
    return df[column].value_counts().to_dict()