#Podemos selecionar colunas usando a notação de colchetes e filtrar linhas com base em condições lógicas.

import pandas as pd

dados = {'nome': ['Ana', 'Pedro', 'Maria'], 'idade': [25, 30, 22]}
df = pd.DataFrame(dados)

# Filtrando a coluna 'idade'
coluna_idade = df['idade']
print("Coluna 'idade' selecionada:\n", coluna_idade) # Saída esperada: [25, 30, 22]

# Filtrando linhas onde a idade é maior que 25
df_filtrado = df[df['idade'] > 25]
print("\nDataFrame filtrado (idade > 25):\n", df_filtrado) # Saída esperada: DataFrame com Pedro (30)