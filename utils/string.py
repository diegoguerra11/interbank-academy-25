from pandas import Series

def dict_to_str(dict: dict, end: str = " ") -> str:
    """ Converts a dict to a str 

        Args:
            dict (dict): dictionary
            end (str): string used as a separator (default = ' ')

        Returns:
            str
    """

    s = ""

    for n in dict:
        s += f"{n}: {dict[n]}{end}"
    
    return s

def serie_to_str(serie: Series, columns:list[str], end=" ") -> str:
    """ Converts a series to a str 
        Args:
            serie (pandas.Series): dataframe
            columns (list[str]): columns chosen to appear in the string
            end (str): string used as a separator (default = ' ')

        Returns:
            str
    """

    s = ""

    for column in columns:
        s += f"{column.upper()}: {serie[column]}{end}"
     
    return s