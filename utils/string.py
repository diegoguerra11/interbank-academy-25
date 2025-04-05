from pandas import Series

def dict_to_str(dict: dict, end: str = " ") -> str:
    s = ""

    for n in dict:
        s += f"{n}: {dict[n]} "
    
    return s

def serie_to_str(serie: Series, columns:list[str]) -> str:
    s = ""

    for column in columns:
        s += f"{column.upper()}: {serie[column]} "
     
    return s