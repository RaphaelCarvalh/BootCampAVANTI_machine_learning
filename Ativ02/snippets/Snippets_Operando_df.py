import pandas as pd

df = pd.DataFrame({

    "Name": [
        "Braund, Mr. Owen Harris",
         "Allen, Mr. William Henry",
         "Bonnell, Miss. Elizabeth",
    ],
    "Age": [22, 35, 58],
    "Sex": ["male", "male", "female"],
})

print(df)
print(df["Age"])
# -------------------------------------------- # -------------------------------- #
df["Age"]

# Saída:
# 0 22
# 1 35
# 2 58
# Name: Age, dtype: int64
# -------------------------------------------- # -------------------------------- #
df["Age"].max()

# Saída:
# 58
# -------------------------------------------- # -------------------------------- #
df.describe()

# Saída:
#       Age
# count 3.000000
# mean  38.333333
# std   18.230012
# min   22.000000
# 25%   28.500000
# 50%   35.000000
# 75%   46.500000
# max   58.000000
# -------------------------------------------- # -------------------------------- #
titanic = pd.read_csv("data/titanic.csv")
titanic.head(8)

# saída:
#    PassengerId Survived Pclass ... Fare    Cabin Embarked
# 0  1           0        3      ... 7.2500  NaN   S
# 1  2           1        1      ... 71.2833 C85   C
# 2  3           1        3      ... 7.9250  NaN   S
# 3  4           1        1      ... 53.1000 C123  S
# 4  5           0        3      ... 8.0500  NaN   S
# 5  6           0        3      ... 8.4583  NaN   Q
# 6  7           0        1      ... 51.8625 E46   S
# 7  8           0        3      ... 21.0750 NaN   S
# [8 rows x 12 columns]
# -------------------------------------------- # -------------------------------- #
titanic.dtypes
# saída:
# PassengerId int64
# Survived int64
# Pclass int64
# Name object
# Sex object
# Age float64
# SibSp int64
# Parch int64
# Ticket object
# Fare float64
# Cabin object
# Embarked object
# dtype: object
# -------------------------------------------- # -------------------------------- #
age_sex = titanic[["Age", "Sex"]]
age_sex.head()
# saída:
#   Age  Sex
# 0 22.0 male
# 1 38.0 female
# 2 26.0 female
# 3 35.0 female
# 4 35.0 male
# -------------------------------------------- # -------------------------------- #
titanic["Age"] > 35
# saída:
# 0 False
# 1 True
# 2 False
# 3 False
# 4 False
# ...
# 886 False
# 887 False
# 888 False
# 889 False
# 890 False
# Name: Age, Length: 891, dtype: bool
# -------------------------------------------- # -------------------------------- #
# Lendo o arquivo CSV
df = pd.read_csv('dados.csv')
# -------------------------------------------- # -------------------------------- #
# Exibindo o DataFrame
print(df)
# -------------------------------------------- # -------------------------------- #
#     nome  idade   profissao
# 0   João     28  Engenheiro
# 1  Maria     32  Professora
# 2 Carlos     25    Designer
# -------------------------------------------- # -------------------------------- #
# Criando um DataFrame
data = {    
     'nome': ['Ana', 'Pedro', 'Luiza'],    
     'idade': [23, 34, 29],    
     'profissao': ['Médica', 'Advogado', 'Arquiteta']
}
df = pd.DataFrame(data)
# -------------------------------------------- # -------------------------------- #
# Gravando o DataFrame em um arquivo CSV
df.to_csv('novo_dados.csv', index=False)
# -------------------------------------------- # -------------------------------- #

# Verifica duplicatas em todo o DataFrame
duplicatas = df.duplicated() 
# -------------------------------------------- # -------------------------------- #

# Verifica duplicatas em uma coluna específica
coluna_duplicatas = df['coluna'].duplicated()
# -------------------------------------------- # -------------------------------- #
# Remove linhas duplicadas
df_sem_duplicatas = df.drop_duplicates()

df_sem_duplicatas = df.drop_duplicates(keep='last')

df_sem_duplicatas = df.drop_duplicates(keep=False)

df_sem_duplicatas = df.drop_duplicates(    
    subset=['coluna1', 'coluna2']
)

df.drop_duplicates(inplace=True)
print(df_sem_duplicatas)
# -------------------------------------------- # -------------------------------- #

# Verifica valores ausentes em todo o DataFrame
valores_ausentes = df.isna()
# -------------------------------------------- # -------------------------------- #
# Verifica valores ausentes em uma coluna específica
coluna_valores_ausentes = df['coluna'].isna()

# -------------------------------------------- # -------------------------------- #

# Preencher valores ausentes em uma coluna com um valor específico
df['coluna'].fillna(valor, inplace=True)
# -------------------------------------------- # -------------------------------- #

# Preencher valores ausentes em todo o DataFrame
df.fillna(valor, inplace=True)
# -------------------------------------------- # -------------------------------- #

# Preenche valores ausentes com a média da coluna
df_preenchido = df.fillna(df.mean())
# -------------------------------------------- # -------------------------------- #

# Preenche valores ausentes com a mediana da coluna
df_preenchido = df.fillna(df.median())
# -------------------------------------------- # -------------------------------- #

# Preenche valores ausentes com a moda da coluna
df_preenchido = df.fillna(df.mode().iloc[0])
# -------------------------------------------- # -------------------------------- #

# Remover linhas com valores ausentes em qualquer coluna
df.dropna(inplace=True)
# -------------------------------------------- # -------------------------------- #

# Remover linhas com valores ausentes em colunas específicas
df.dropna(subset=['coluna1', 'coluna2'], inplace=True)
# -------------------------------------------- # -------------------------------- #

# Opção 1: Remoção de outliers
df_sem_outliers = df[df['idade'] < limite_superior]
# -------------------------------------------- # -------------------------------- #

# Opção 2: Transformação
df['idade_transformada'] = df['idade'].apply(lambda x: x ** 0.5)
# -------------------------------------------- # -------------------------------- #

# Opção 3: Substituição
mediana_idade = df['idade'].median()
df['idade_sem_outliers'] = df['idade'].apply(    
    lambda x: mediana_idade if x > limite_superior else x
)
# -------------------------------------------- # -------------------------------- #

# Convertendo uma coluna para inteiro
df['coluna_int'] = df['coluna_float'].astype(int)

# Convertendo uma coluna para ponto flutuante
df['coluna_float'] = df['coluna_int'].astype(float)

# Convertendo uma coluna para string
df['coluna_str'] = df['coluna_float'].astype(str)
# -------------------------------------------- # -------------------------------- #

# Lendo um CSV com tipos específicos
df = pd.read_csv(
     'dados.csv', 
     dtype={    
         'coluna_int': int, 
         'coluna_float': float    
     })
# -------------------------------------------- # -------------------------------- #

# Renomeando uma coluna
df.rename(    
    columns={'nome_antigo': 'nome_novo'},     
    inplace=True   
    )

# Renomeando várias colunas
df.rename(    
    columns={        
        'coluna1': 'nova_coluna1',         
        'coluna2': 'nova_coluna2'
        },     
    inplace=True   
    )

# -------------------------------------------- # -------------------------------- #

# Exemplo de DataFrame
data = {    
     'idade': [25, 30, 28, 22, 35, 40, 29],    
     'salario': [50000, 60000, 55000, 48000, 75000, 90000, 58000]
}

df = pd.DataFrame(data)

# -------------------------------------------- # -------------------------------- #

# Média
media_idade = df['idade'].mean()
media_salario = df['salario'].mean()

# Mediana
mediana_idade = df['idade'].median()
mediana_salario = df['salario'].median()

# Moda
moda_idade = df['idade'].mode()
moda_salario = df['salario'].mode()

# Mediana
mediana_idade = df['idade'].median()
mediana_salario = df['salario'].median()

# Mínimo
minimo_idade = df['idade'].min()
minimo_salario = df['salario'].min()

# Máximo
maximo_idade = df['idade'].max()
maximo_salario = df['salario'].max()
# -------------------------------------------- # -------------------------------- #
# Contagem de valores únicos em uma coluna
import pandas as pd
# Exemplo de DataFrame
data = {
    'classe': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C', 'B', 'A']
}
df = pd.DataFrame(data)
# Contagem de valores únicos em uma coluna
contagem_valores = df['classe'].value_counts()
print(contagem_valores)

# saída:
# A 4
# B 3
# C 3
# Name: classe, dtype: int64
# -------------------------------------------- # -------------------------------- #
# Filtragem de dados com operadores de comparação
import pandas as pd
# Exemplo de DataFrame
data = {    
    'nome': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],    
    'idade': [25, 30, 28, 22, 35],    
    'salario': [50000, 60000, 55000, 48000, 75000]
}
df = pd.DataFrame(data)

# Filtragem usando operadores de comparação
idade_maior_30 = df[df['idade'] > 30]
salario_acima_55000 = df[df['salario'] > 55000]

print("Pessoas com idade maior que 30:\n", idade_maior_30)
print("Pessoas com salário acima de 55000:\n", salario_acima_55000)
# -------------------------------------------- # -------------------------------- #

# Filtragem e seleção de dados com base em critérios específicos
idade_maior_30 = df.query('idade > 30')
salario_acima_55000 = df.query('salario > 55000')
print("Pessoas com idade maior que 30:\n", idade_maior_30)
# -------------------------------------------- # -------------------------------- #
pessoas_idade_maior_30 = df.loc[    
    df['idade'] > 30, ['nome', 'idade']
]
print("Pessoas com idade maior que 30:\n", pessoas_idade_maior_30)
###
filtro = (df['idade'] > 25) & (df['salario'] > 55000)
pessoas_filtradas = df[filtro]
print("Pessoas com idade maior que 25 e salário acima de 55000:\n", pessoas_filtradas)
###
filtro = (df['idade'] > 25) | (df['salario'] > 55000)
pessoas_filtradas = df[filtro]
print("Pessoas com idade maior que 25 ou salário acima de 55000:\n", pessoas_filtradas)
###
# -------------------------------------------- # -------------------------------- #
# Operações de junção e fusão de DataFrames
# O método join() permite combinar dataframes usando os índices em vez de colunas-chave.
# Fusão usando join
data = {    
    'nome': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'idade': [25, 30, 28, 22, 35],    

}
numbers = {    
    'chave': [1, 2, 3, 4, 5],    
    'idade': [25, 30, 28, 22, 35]
}

df2 = pd.DataFrame(data)
df1 = pd.DataFrame(data)

df1 = df1.set_index('chave')
df2 = df2.set_index('chave')
resultado_join = df1.join(df2, lsuffix='_left', rsuffix='_right')
print(resultado_join)
# -------------------------------------------- # -------------------------------- #
# Fusão usando merge
resultado_merge = pd.merge(df1, df2, on='chave')
print(resultado_merge)
# -------------------------------------------- # -------------------------------- #

import pandas as pd
#from sklearn.model_selection
import train_test_split

# Exemplo de DataFrame
data = {    
'features': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],    
'target': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}
df = pd.DataFrame(data)
# -------------------------------------------- # -------------------------------- #
# Exemplo de DataFrames
df1 = pd.DataFrame({'coluna1': [1, 2, 3]})
df2 = pd.DataFrame({'coluna1': [4, 5, 6]})
# -------------------------------------------- # -------------------------------- #

# Concatenação vertical
result_vert = pd.concat([df1, df2])
print(result_vert)
#    coluna1
# 0        1
# 1        2
# 2        3
# 0        4
# 1        5
# 2        6
# -------------------------------------------- # -------------------------------- #

# Concatenação horizontal
result_hor = pd.concat([df1, df2], axis=1)
print(result_hor)
#    coluna1
# 0        1
# 1        2
# 2        3
# 0        4
# 1        5
# 2        6
# -------------------------------------------- # -------------------------------- #

# Divisão dos dados em conjuntos de treinamento e teste
X = df['features']
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
print("Conjunto de treinamento (X):\n", X_train)
print("Conjunto de teste (X):\n", X_test)
print("Conjunto de treinamento (y):\n", y_train)
print("Conjunto de teste (y):\n", y_test)
# -------------------------------------------- # -------------------------------- #
# Exemplo de DataFrame
data = {    
'features': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],    
'target': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}
df = pd.DataFrame(data)

# Divisão dos dados em conjuntos de treinamento e teste
X = df['features']
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
print("Conjunto de treinamento (X):\n", X_train)
print("Conjunto de teste (X):\n", X_test)
print("Conjunto de treinamento (y):\n", y_train)
print("Conjunto de teste (y):\n", y_test)

# -------------------------------------------- # -------------------------------- #
import pandas as pd
import matplotlib.pyplot as plt
data = {    
    'categoria': ['A', 'B', 'C', 'D'],    
    'valor': [10, 25, 15, 30]
}
df = pd.DataFrame(data)

# Gráfico de barras usando Matplotlib
plt.bar(df['categoria'], df['valor'])
plt.xlabel('Categoria')
plt.ylabel('Valor')
plt.title('Gráfico de Barras')
plt.show()

# -------------------------------------------- # -------------------------------- #
import pandas as pd
import matplotlib.pyplot as plt
data = {
     'ano': [2010, 2011, 2012, 2013, 2014],
     'vendas': [100, 120, 150, 130, 180]
}
df = pd.DataFrame(data)
# Gráfico de linhas usando Matplotlib
plt.plot(df['ano'], df['vendas'], marker='o')
plt.xlabel('Ano')
plt.ylabel('Vendas')
plt.title('Gráfico de Linhas')
plt.show()

# -------------------------------------------- # -------------------------------- #
import pandas as pd
import matplotlib.pyplot as plt
data = {
     'ano': [2010, 2011, 2012, 2013, 2014],
     'vendas': [100, 120, 150, 130, 180]
}
df = pd.DataFrame(data)
# Gráfico de linhas usando Matplotlib
plt.plot(df['ano'], df['vendas'], marker='o')
plt.xlabel('Ano')
plt.ylabel('Vendas')
plt.title('Gráfico de Linhas')
plt.show()

# -------------------------------------------- # -------------------------------- #
import pandas as pd
import matplotlib.pyplot as plt
data = {
    'idade': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
}
df = pd.DataFrame(data)

# Histograma usando Matplotlib
plt.hist(df['idade'], bins=5, edgecolor='k')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.title('Histograma')
plt.show()

# -------------------------------------------- # -------------------------------- #
