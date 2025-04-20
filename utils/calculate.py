from typing import Literal
from pandas import DataFrame

from utils.validations import is_str, is_numeric, df_missing_columns, serie_missing_columns

def add_by_column(df: DataFrame, column: str, categories: list[str]) -> float:
    """ Allows the addition of the values ​​of a column according to the type 
           
        Args:
            df (pandas.Dataframe): dataframe
            column (str): column to which the addition will be applied
            categories(list[str]): categories on which the addition will be performed

        Returns:
            float
        
        :raises: Exception: If any exception occurs, the message is returned and the -9999999 value is returned.            
    """
    try:
        missing = df_missing_columns(df, [column])
        if(len(missing) > 0): raise Exception(f"The following columns do not exist in the dataframe: ", missing)
    
        type_mission = serie_missing_columns(df[column], categories)
        if(len(type_mission) > 0): raise Exception(f"The following categories do not exist in the dataframe: ", type_mission)

        sum = 0
        
        for category in categories: 
            sum += df[column][category]

        return sum
    except Exception as e:
        print(f"add_by_column: {e}")
        return -9999999

def sub_by_column(df: DataFrame, column: str, categories: list[str]) -> float:
    """ Allows the subtraction of the values ​​of a column according to the category 
        
        Args:
            df (pandas.Dataframe): dataframe
            column (str): column to which the subtraction will be applied
            categories(list[str]): categories on which the subtraction will be performed

        Returns:
            float
        
        :raises: Exception: If any exception occurs, the message is returned and the -9999999 value is returned.  
    """
    try:
        sub = 0

        missing = df_missing_columns(df, [column])
        if(len(missing) > 0): raise Exception(f"The following columns do not exist in the dataframe: ", missing)

        type_mission = serie_missing_columns(df[column], categories)
        if(len(type_mission) > 0): raise Exception(f"The following categories do not exist in the dataframe: ", type_mission)
        
        for category in categories:
            if(sub == 0): 
                sub = df[column][category]
                continue

            sub -= df[column][category]

        return sub
    except Exception as e:
        print(f"sub_by_column (exception): {e}")
        return -9999999

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
            df (pandas.Dataframe): dataframe
            group_by (str): the categorical column used to group the dataframe
            operation (Literal["add", "sub"]): Mathematical operation applied to a numeric column (add -> addition or sub -> substraccion)
            column (str): numeric column the operation will be applied to
            categories(list[str]): categories on which the operation will be performed

        Returns:
            float

        :raises: Exception: If any exception occurs, the message is returned and the -9999999 value is returned.              
    """
    try:
        missing = df_missing_columns(df, [group_by, column])

        if(len(missing) > 0): raise Exception(f"The following columns do not exist in the dataframe: ", missing)
        if(not is_str(df, group_by)): raise Exception("Group by categorical column only")
        if(not is_numeric(df, column)):  raise Exception("Only operation by column numeric")

        df_by_type = df.groupby(group_by).sum()

        result = 0

        match operation:
            case "sum": result = add_by_column(df_by_type, column, categories)
            case "sub": result = sub_by_column(df_by_type, column, categories)
            case _: raise Exception("Only add or sub operations can be performed")

        return round(result, 2)
    except Exception as e:
        print(f"calculate_by_grouped (exception): {e}")
        return -9999999

def count_by_column(df: DataFrame, column: str) -> dict:
    """ Counts the number of records by the selected column 
        
        Args:
            df (pandas.Dataframe): dataframe
            column (str): column by which the count by value will be performed

        Returns:
            dict

        :raises: Exception: If any exception occurs, the message is returned and an empty dict is returned.
    """
    try:
        missing = df_missing_columns(df, [column])
        
        if(len(missing) > 0): raise Exception(f"The following columns do not exist in the dataframe: ", missing)

        return df[column].value_counts().to_dict()
    except Exception as e:
        print(f"count_by_column (exception): {e}")
        return {}