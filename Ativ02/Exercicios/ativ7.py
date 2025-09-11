# Utilizamos pd.concat() para unir DataFrames.

import pandas as pd

df1 = pd.DataFrame({'nome': ['Maria', 'João'], 'idade': [30, 25]})
df2 = pd.DataFrame({'nome': ['Ana', 'Pedro'], 'idade': [22, 35]})

df_concatenado = pd.concat([df1, df2], ignore_index=True)
print("DataFrame concatenado por linhas:\n", df_concatenado) # Saída esperada: DataFrame com 4 linhas e 2 colunas

df_concatenado_col = pd.concat([df1, df2], axis=1)
print("DataFrame concatenado por colunas:\n", df_concatenado_col) # Saída esperada: DataFrame com 2 linhas e 4 colunas