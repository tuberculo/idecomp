"""
========================================
dec_oper_sist.csv
========================================
"""

# %%
# O primeiro passo para realizar o processamento do arquivo, assim como os
# demais arquivos .csv, é a leitura. A função de leitura recebe dois argumentos,
# sendo que o segundo é opcional. Tendo lido o arquivo, é possível recuperar
# a versão em que o modelo foi executado.
from idecomp.decomp import DecOperSist

arq = DecOperSist.le_arquivo(".")
print(arq.versao)


# %%
# A tabela de informações é fornecida como um dataframe, onde os nomes das colunas geralmente
# remetem aos nomes originais das colunas do arquivo .csv, porém em camelCase.
df = arq.tabela
print(df.columns)


# %%
# A partir deste dataframe é possível realizar análises e produzir visualizações. Por exemplo,
# utilizando o módulo plotly. Deste ponto em diante, não é mais necessário o conhecimento
# específico do arquivo ou da idecomp.
import plotly.express as px

estagio_mensal = df["periodo"].max()
# sphinx_gallery_thumbnail_number = 1
fig = px.box(
    df.loc[df["periodo"] == estagio_mensal],
    x="nome_submercado",
    y="geracao_termica_MW",
)
fig
