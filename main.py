import pandas as pd

from utils.string import dict_to_str, serie_to_str
from utils.calculate import calculate_by_grouped, count_by_column

# The pandas library reads the .csv file and converts it to a dataframe.
df = pd.read_csv('data/data.csv')

print("""
Reporte de Transacciones
---------------------------------------------------------------------------------
""")

# Subtracts the amounts from the dataframe based on the type (Credit - Debit)
final_balance = calculate_by_grouped(
    df=df,
    grouping_column='tipo',
    operation='sub',
    categorical_column='monto',
    categories=['Crédito', 'Débito']
)
print(f"Balance Final: {final_balance}")

# Find the record with the highest amount
mayor_monto = df.max()
print(f"Transacción de Mayor Monto: {serie_to_str(serie=mayor_monto, columns=['id', 'monto'])}")

# Counts the number of records according to the type column
count_by_type = count_by_column(df=df, column='tipo')
print(f"Conteo de Transacciones: {dict_to_str(dict=count_by_type)}")