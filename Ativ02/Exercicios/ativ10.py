# O pandas oferece várias funções para tratar valores NaN (Not a Number).

import pandas as pd
import numpy as np

# Criando um DataFrame com valores ausentes
df = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [5, np.nan, 7, 8]})
print("DataFrame original com NaN:\n", df)

# 1. Remover linhas com valores NaN
df_sem_nan = df.dropna()
print("\nDataFrame após remover linhas com NaN:\n", df_sem_nan)

# 2. Preencher valores NaN com um valor específico (ex: 0)
df_preenchido = df.fillna(0)
print("\nDataFrame após preencher NaN com 0:\n", df_preenchido)

# 3. Preencher NaN com a média da coluna
media_coluna_A = df['A'].mean()
df_preenchido_media = df.fillna({'A': media_coluna_A})
print("\nDataFrame após preencher NaN de 'A' com a média:\n", df_preenchido_media)