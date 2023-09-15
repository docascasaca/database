# Importação das bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leitura da base de dados
url = "https://github.com/docascasaca/database/raw/main/data.xls" 
df = pd.read_excel(url)

# Tratamento de dados faltantes
df.fillna(value=0, inplace=True)

# Estatística Descritiva
print("Estatísticas descritivas:")
print(df.describe())


# ««««« Uso de Group By »»»»»

# Utilização do GroupBy para agrupar dados por Região e obter média dos rendimentos
grouped = df.groupby("Região").mean()
print("\nMédia dos rendimentos por região:")
print(grouped)

# Soma os valores dos rendimentos por cada região
grouped_sum = df.groupby('Região').sum()
print("\nSoma dos rendimentos por região:")
print(grouped_sum)

# Encontra a renda per capita máxima e mínima por região
grouped_extremes = df.groupby('Região')['Rendimento domiciliar per capita'].agg(['min', 'max'])
print("\nRenda per capita mínima e máxima por região:")
print(grouped_extremes)


# ««««« Uso de Join »»»»»

# DataFrame de exemplo com dados de população por região
data = {'Região': ['Rio de Janeiro', 'Penha', 'Bangu', 'Santa Teresa'],
        'População': [100000, 150000, 200000, 250000]}
df2 = pd.DataFrame(data)

# Realizando um JOIN entre df e df2 baseado na coluna "Região"
joined_df = pd.merge(df, df2, on="Região")
print("\nDataFrame após o JOIN com df2:")
print(joined_df)


# «««««  Uso de gráficos  »»»»»

# Histograma do Rendimento domiciliar per capita
plt.figure(figsize=(10, 6))
plt.hist(df['Rendimento domiciliar per capita'], bins=20, edgecolor='black')
plt.title('Histograma de Rendimento domiciliar per capita')
plt.xlabel('Rendimento domiciliar per capita')
plt.ylabel('Frequência')
plt.show()

# Boxplot do Rendimento mensal domiciliar por Região
plt.figure(figsize=(11, 8))
sns.boxplot(y='Região', x='Rendimento mensal domiciliar', data=df)
plt.title('Grafico de Rendimento mensal domiciliar por Região')
plt.show()
