# A função pd.read_csv() é usada para ler arquivos no formato CSV.
import pandas as pd

# Lendo o arquivo e exibindo as primeiras 5 linhas
df = pd.read_csv("dados.csv")
print("As primeiras 5 linhas do DataFrame:\n", df.head())