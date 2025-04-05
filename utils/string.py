from pandas import Series

def dict_to_str(dict: dict, end: str = " ") -> str:
    """ Converts a dict to a str """
    s = ""

    for n in dict:
        s += f"{n}: {dict[n]}{end}"
    
    return s

def serie_to_str(serie: Series, columns:list[str], end=" ") -> str:
    """ Converts a series to a str """
    s = ""

    for column in columns:
        s += f"{column.upper()}: {serie[column]}{end}"
     
    return s