from idecomp.decomp.modelos.blocos.versaomodelo import VersaoModelo
from idecomp.decomp.modelos.dec_avl_evap import TabelaAvlEvap

from idecomp.decomp.modelos.arquivoscsv.arquivocsv import ArquivoCSV
from typing import Optional
import pandas as pd  # type: ignore


class DecAvlEvap(ArquivoCSV):
    """
    Arquivo com a avaliação da evaporação linear do DECOMP.
    """

    BLOCKS = [VersaoModelo, TabelaAvlEvap]

    @classmethod
    def le_arquivo(
        cls, diretorio: str, arquivo: str = "dec_avl_evap.csv"
    ) -> "DecAvlEvap":
        return cls.read(diretorio, arquivo)

    @property
    def tabela(self) -> Optional[pd.DataFrame]:
        """
        A tabela de dados que está contida no arquivo.

        - periodo (`int`)
        - indice_usina (`int`)
        - nome_usina (`str`)
        - submercado (`int`)
        - ree (`int`)
        - volume_armazenado_hm3 (`float`)
        - evaporacao_calculada_hm3 (`float`)
        - evaporacao_modelo_hm3 (`float`)
        - desvio_absoluto_hm3 (`float`)
        - desvio_percentual (`float`)

        :return: A tabela como um dataframe
        :rtype: pd.DataFrame | None
        """
        return self._tabela()
