import pandas as pd
import matplotlib.pyplot as plt

file_path = 'dados.csv'
dados = pd.read_csv(file_path, delimiter=';')

dados.columns = dados.columns.str.strip()


dados['Valor da Receita Tributária'] = dados['Valor da Receita Tributária'].str.replace('.', '').str.replace(',', '.').astype(float)
dados['Percentual do PIB'] = dados['Percentual do PIB'].str.replace(',', '.').astype(float)


print(dados.info())
print(dados.describe())


principais_receitas = dados.groupby('Descrição')['Valor da Receita Tributária'].sum().sort_values(ascending=False)
top_10_receitas = principais_receitas.head(10)


estatisticas_descritivas = dados[dados['Descrição'].isin(top_10_receitas.index)].groupby('Descrição')['Valor da Receita Tributária'].describe()


print(estatisticas_descritivas)


plt.figure(figsize=(10, 6))
top_10_receitas.plot(kind='bar')
plt.title('Gastos Consolidados das Principais Linhas de Investimento')
plt.ylabel('Valor da Receita Tributária')
plt.xlabel('Descrição')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()


plt.savefig('gastos_consolidados.png')


plt.show()


ultimo_ano = dados['Ano-calendário'].max()
dados_ultimo_ano = dados[dados['Ano-calendário'] == ultimo_ano]

maior_gasto = dados_ultimo_ano.loc[dados_ultimo_ano['Valor da Receita Tributária'].idxmax()]
menor_gasto = dados_ultimo_ano.loc[dados_ultimo_ano['Valor da Receita Tributária'].idxmin()]


plt.figure(figsize=(10, 6))
dados[dados['Descrição'] == maior_gasto['Descrição']].groupby('Ano-calendário')['Valor da Receita Tributária'].sum().plot(kind='bar')
plt.title(f'Evolução Anual do Maior Gasto: {maior_gasto["Descrição"]}')
plt.ylabel('Valor da Receita Tributária')
plt.xlabel('Ano-calendário')
plt.tight_layout()


plt.savefig('maior_gasto.png')


plt.show()


plt.figure(figsize=(10, 6))
dados[dados['Descrição'] == menor_gasto['Descrição']].groupby('Ano-calendário')['Valor da Receita Tributária'].sum().plot(kind='bar')
plt.title(f'Evolução Anual do Menor Gasto: {menor_gasto["Descrição"]}')
plt.ylabel('Valor da Receita Tributária')
plt.xlabel('Ano-calendário')
plt.tight_layout()


plt.savefig('menor_gasto.png')


plt.show()





dados_classe_1000 = dados[dados['Código da Receita Tributária'] >= 1000]
dados_classe_1000 = dados_classe_1000[dados_classe_1000['Código da Receita Tributária'] < 2000]


estatisticas_classe_1000 = dados_classe_1000.groupby('Descrição')['Valor da Receita Tributária'].describe()


print(estatisticas_classe_1000)


plt.figure(figsize=(10, 6))
dados_classe_1000.groupby('Ano-calendário')['Valor da Receita Tributária'].sum().plot(kind='bar')
plt.title('Evolução Anual da Classe 1000 - Tributos sobre a Renda')
plt.ylabel('Valor da Receita Tributária')
plt.xlabel('Ano-calendário')
plt.tight_layout()


plt.savefig('evolucao_classe_1000.png')


plt.show()
