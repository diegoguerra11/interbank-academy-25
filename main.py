import pandas as pd

from utils.string import dict_to_str, serie_to_str
from utils.calculate import calculate_by_grouped_type, count_by_column

df = pd.read_csv('data.csv')

print("Reporte de Transacciones")
print("---------------------------------------------")

final_balance = calculate_by_grouped_type(df, 'sub', 'monto', ['Crédito', 'Débito'])
print(f"Balance Final: {final_balance}")

mayor_monto = df.max()
print(f"Transacción de Mayor Monto: {serie_to_str(mayor_monto, ['id', 'monto'])}")

count_by_type = count_by_column(df, 'tipo')
print(f"Conteo de Transacciones: {dict_to_str(count_by_type)}")