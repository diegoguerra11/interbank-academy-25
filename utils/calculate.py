from typing import Literal
from pandas import DataFrame

from utils.validations import is_str, is_numeric, df_missing_columns, serie_missing_columns

def add_by_categories(df: DataFrame, categorical_column: str, categories: list[str]) -> float:
    """ Allows the addition of the values ​​of a column according to the type 
           
        Args:
            df (pandas.Dataframe): dataframe
            categorical_column (str): column to which the addition will be applied
            categories(list[str]): categories on which the addition will be performed

        Returns:
            float
        
        :raises: Exception: If any exception occurs, the message is printed and the -9999999 value is returned.            
    """
    try:
        #validations
        columns_missings = df_missing_columns(df=df, columns=[categorical_column])
        if(len(columns_missings) > 0): raise Exception(f"The following columns do not exist in the dataframe: ", columns_missings)

        if(not is_numeric(df, categorical_column)): raise Exception("only numeric column")

        categories_missings = serie_missing_columns(serie=df[categorical_column], keys=categories)
        if(len(categories_missings) > 0): raise Exception(f"The following categories do not exist in the dataframe: ", categories_missings)

        sum = 0

        # sum the amounts of the categories (category 1 + category 2 + category n)
        for category in categories: 
            sum += df[categorical_column][category]

        return sum
    except Exception as e:
        print(f"add_by_column: {e}")
        return -9999999

def sub_by_categories(df: DataFrame, categorical_column: str, categories: list[str]) -> float:
    """ Allows the subtraction of the values ​​of a column according to the category 
        
        Args:
            df (pandas.Dataframe): dataframe
            categorical_column (str): column to which the subtraction will be applied
            categories(list[str]): categories on which the subtraction will be performed

        Returns:
            float
        
        :raises: Exception: If any exception occurs, the message is printed and the -9999999 value is returned.  
    """
    try:
        sub = 0

        #validations
        columns_missings = df_missing_columns(df=df, columns=[categorical_column])
        if(len(columns_missings) > 0): raise Exception(f"The following columns do not exist in the dataframe: ", columns_missings)

        if(not is_numeric(df, categorical_column)): raise Exception("only numeric column")

        categories_missings = serie_missing_columns(serie=df[categorical_column], keys=categories)
        if(len(categories_missings) > 0): raise Exception(f"The following categories do not exist in the dataframe: ", categories_missings)
        
        # subtract the amounts of the categories (category 1 - category 2 - category n
        for category in categories:
            if(sub == 0): 
                sub = df[categorical_column][category]
                continue

            sub -= df[categorical_column][category]

        return sub
    except Exception as e:
        print(f"sub_by_column (exception): {e}")
        return -9999999

def calculate_by_grouped(
    df: DataFrame,
    grouping_column: str,
    operation: Literal["add", "sub"],
    categorical_column: str,
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

        :raises: Exception: If any exception occurs, the message is printed and the -9999999 value is returned.              
    """
    try:
        #validations
        columns_missings = df_missing_columns(df=df, columns=[grouping_column, categorical_column])

        if(len(columns_missings) > 0): raise Exception(f"The following columns do not exist in the dataframe: ", columns_missings)
        if(not is_str(df=df, column=grouping_column)): raise Exception("Group by categorical column only")
        if(not is_numeric(df=df, column=categorical_column)):  raise Exception("Only operation by column numeric")

        # group by the desired column and sum by column
        sum_by_type = df.groupby(grouping_column).sum()

        result = 0

        # select the type of operation according to the operation variable
        match operation:
            case "sum": 
                result = add_by_categories(
                    df=sum_by_type,
                    categorical_column=categorical_column,
                    categories=categories
                )
            case "sub": 
                result = sub_by_categories(
                    df=sum_by_type,
                    categorical_column=categorical_column,
                    categories=categories
                )
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

        :raises: Exception: If any exception occurs, the message is printed and an empty dict is returned.
    """
    try:
        #validations
        columns_missings = df_missing_columns(df=df, columns=[column])
        
        if(len(columns_missings) > 0): raise Exception(f"The following columns do not exist in the dataframe: ", columns_missings)

        # counts for each value in the column and returns a dict
        return df[column].value_counts().to_dict()
    except Exception as e:
        print(f"count_by_column (exception): {e}")
        return {}