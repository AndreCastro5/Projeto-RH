# Libs Necessárias 

# Libs para Modelagem e Matrizes 
import numpy as np 
import pandas as pd 

#libs para a análise gráfica 
import matplotlib.pyplot as plt 
import seaborn as sns 

# lib para ignorar avisos 
import warnings 

# Desabilitando avisos 
warnings.filterwarnings ('ignore')

# lib de importação de DF 
import os 

# importando df 
os.chdir('C:\\Users\\andre\\OneDrive\\Área de Trabalho\\python\\Projeto RH')

#Lendo os dados 
Base_Dados = pd.read_csv('Salary_Data.csv')

# verificando 
print (Base_Dados.head())

# renomeando as colunas 
Base_Dados.rename(columns ={
    'YearsExperience' : 'Xp',
    'Salary' : 'Renda'
}, inplace=True
                  )
# dimensão 
print(Base_Dados.shape)

#Campos nulos 
print(Base_Dados.isnull().sum())

#Grafico dos Nulos 
sns.heatmap(Base_Dados.isnull(), cbar=False)
plt.show()

print(Base_Dados.describe())

# Análise de Renda 
plt.figure(figsize=(10,6))
plt.title('Análise de Renda')
sns.kdeplot(Base_Dados['Renda'], color='green')
plt.show()

# Análise de Experiência
plt.figure(figsize=(10,6))
plt.title('Análise de Xp')
sns.kdeplot(Base_Dados['Xp'], color='blue')
plt.show()

# Distribuição da renda 
plt.figure(figsize=(10,5))
sns.boxplot(Base_Dados['Renda'])
plt.show()

# Distribuição da Experiência 
plt.figure(figsize=(10,5))
sns.boxplot(Base_Dados['Xp'])
plt.show()

# Distribuição de renda por experiência, gráfico plotado 
plt.figure(figsize=(10,5))
sns.scatterplot(data=Base_Dados, x='Renda', y='Xp')
plt.show()

# Distribuição de renda por experiência, gráfico plotado com linha indicadora
plt.figure(figsize=(10,5))
sns.regplot(data=Base_Dados, x='Renda', y='Xp')
plt.show()

# Correlação de pearson
correlacao = Base_Dados.corr('pearson')
plt.figure( figsize=(10,5))
sns.heatmap(correlacao, annot=True, cbar= True)
plt.show()

# Correlação de spearman 
correlacao = Base_Dados.corr('spearman')
plt.figure( figsize=(10,5))
sns.heatmap(correlacao, annot=True, cbar= True)
plt.show()