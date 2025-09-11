### Questão 6: Identificar e Tratar Outliers


# O método do IQR é baseado na mediana e nos quartis

# ```python
import pandas as pd
import numpy as np

dados = pd.Series([20, 22, 21, 23, 25, 99, 24])

Q1 = dados.quantile(0.25) # Primeiro quartil (25%)
Q3 = dados.quantile(0.75) # Terceiro quartil (75%)

IQR = Q3 - Q1 # Intervalo interquartil

# 1,5 valor fixo usado para definir o intervalo onde os dados são considerados "normais" no método do Intervalo Interquartil (IQR)
limite_inferior = Q1 - 1.5 * IQR # Limite inferior
limite_superior = Q3 + 1.5 * IQR # Limite superior

# Encontrar os outliers
outliers = dados[(dados < limite_inferior) | (dados > limite_superior)]
print(f"Outliers encontrados: \n{outliers}\n")  # Saída esperada: 5 99

# Para tratar, podemos substituir por NaN ou pela média/mediana
dados_tratados = dados.mask((dados < limite_inferior) | (dados > limite_superior), np.nan)
print("Dados com outliers substituídos por NaN:\n", dados_tratados) # Saída esperada: [20.0, 22.0, 21.0, 23.0, 25.0, NaN, 24.0]

