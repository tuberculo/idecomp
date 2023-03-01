"""
========================================
relato.rv0
========================================
"""

#%%
# O primeiro passo para realizar o processamento do arquivo, assim como os
# demais arquivos de saída, é a leitura. A função de leitura recebe dois argumentos,
# sendo que o segundo é opcional.
from idecomp.decomp import Relato

arq = Relato.le_arquivo(".", nome_arquivo="relato.rv0")


#%%
# Existem diversas propriedades, uma para cada tipo de dados do Relato, e que estão disponíveis
# em datalhes na seção de Referência. Uma destas é o balanco da operação energética. Assim como
# a maioria das propriedades que são tabulares, esta é processada na forma de um dataframe para o usuário.
df = arq.balanco_energetico
print(df.columns)


#%%
# A partir deste dataframe é possível realizar análises e produzir visualizações. Por exemplo,
# utilizando o módulo plotly. Deste ponto em diante, não é mais necessário o conhecimento
# específico do arquivo ou da idecomp.
import plotly.express as px

# sphinx_gallery_thumbnail_number = 1
fig = px.line(df, x="Estágio", y="Earm Final Percentual", color="Subsistema")
fig
