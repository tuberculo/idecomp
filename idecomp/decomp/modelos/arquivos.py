from cfinterface.components.section import Section
from cfinterface.components.line import Line
from cfinterface.components.literalfield import LiteralField
from typing import IO, List
import pandas as pd  # type: ignore


class BlocoNomesArquivos(Section):
    """
    Bloco de informações do arquivo que contém os
    arquivos de entrada do DECOMP.
    """

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line([LiteralField(80, 0)])

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BlocoNomesArquivos):
            return False
        bloco: BlocoNomesArquivos = o
        if not all(
            [
                isinstance(self.data, pd.DataFrame),
                isinstance(o.data, pd.DataFrame),
            ]
        ):
            return False
        else:
            return self.data.equals(bloco.data)

    # Override
    def read(self, file: IO):
        def converte_tabela_em_df():
            df = pd.DataFrame(data={"Nome": nomes})
            return df

        nomes: List[str] = []
        while True:
            linha = file.readline()
            if len(linha) == 0:
                self.data = converte_tabela_em_df()
                break
            dados = self.__linha.read(linha)
            nomes.append(dados[0])

    # Override
    def write(self, file: IO):
        if not isinstance(self.data, pd.DataFrame):
            raise ValueError("Dados do arquivos não foram lidos")
        for _, linha in self.data.iterrows():
            file.write(self.__linha.write(linha.tolist()))
