from pandas import Series

from utils.validations import serie_missing_columns

def dict_to_str(dict: dict, end: str = " ") -> str:
    """ Converts a dict to a str 

        Args:
            dict (dict): dictionary
            end (str): string used as a separator (default = ' ')

        Returns:
            str
        
        :raises: Exception: If any exception occurs, the message is printed and the "error" value is returned.
    """
    try:
        s = ""
        
        # concatenates each key-value of a dict into a string
        for n in dict:
            s += f"{n}: {dict[n]}{end}"
        
        return s
    except Exception as e:
        print(f"dict_to_str (exception): {e}")
        return "error"

def serie_to_str(serie: Series, columns:list[str], end=" ") -> str:
    """ Converts a series to a str 
        Args:
            serie (pandas.Series): dataframe
            columns (list[str]): columns chosen to appear in the string
            end (str): string used as a separator (default = ' ')

        Returns:
            str

        :raises: Exception: If any exception occurs, the message is printed and the "error" value is returned.
    """
    try:
        s = ""
        
        #validaions
        type_mission = serie_missing_columns(serie, columns)
        if(len(type_mission) > 0): raise Exception(f"The following categories do not exist in the dataframe: ", type_mission)

        # concatenates each key-value in the series based on the selected columns into a string
        for column in columns:
            s += f"{column.upper()}: {serie[column]}{end}"
        
        return s
    except Exception as e:
        print(f"serie_to_str (exception): {e}")
        return "error"