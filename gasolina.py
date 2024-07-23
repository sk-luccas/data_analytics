import pandas as pd
import seaborn as sns
import matplotlib as plt

data = 'gasolina.csv'
df_gasolina = pd.read_csv(data,sep=',')

with sns.axes_style('darkgrid'):
  graph = sns.lineplot(data= df_gasolina, x='dia',y='venda')
  graph.set(title= 'Preço da gasolina diária', xlabel='Dia', ylabel='Preço R$')

  fig = graph.get_figure()
  fig.savefig('gasolina.png')
