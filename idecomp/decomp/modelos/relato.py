from typing import Dict, List
import numpy as np  # type: ignore


class DadosGeraisRelato:
    """
    Armazena os dados de saída existentes no relato do DECOMP
    referentes aos dados gerais fornecidos ao programa.

    **Parâmetros**

    - numero_semanas_1_mes: `int`

    """
    def __init__(self,
                 numero_semanas_1_mes: int):
        self.numero_semanas_1_mes = numero_semanas_1_mes

    def __eq__(self, o: object) -> bool:
        """
        A igualdade entre DadosGeraisRelato avalia todos os campos.
        """
        if not isinstance(o, DadosGeraisRelato):
            return False
        rel: DadosGeraisRelato = o
        dif = False
        for (k, u), (_, v) in zip(self.__dict__.items(),
                                  rel.__dict__.items()):
            if u != v:
                dif = True
                break
        return not dif


class CMORelato:
    """
    Armazena os dados de saída existentes no relato do DECOMP
    referentes ao Custo Marginal de Operação (CMO).

    Esta classe armazena a tabela de CMO por subsistema em cada
    patamar de carga e os valores médios por submercado.

    **Parâmetros**

    - subsistema: `List[str]`
    - tabela: `np.ndarray`

    """
    def __init__(self,
                 subsistema: List[str],
                 tabela: np.ndarray):
        self.subsistema = subsistema
        self.tabela = tabela

    def __eq__(self, o: object) -> bool:
        """
        A igualdade entre CMORelato avalia todos os campos.
        """
        if not isinstance(o, CMORelato):
            return False
        cmo: CMORelato = o
        eq_subsistema = self.subsistema == cmo.subsistema
        eq_tabela = np.array_equal(self.tabela, cmo.tabela)
        return all([eq_subsistema, eq_tabela])

    @property
    def custo_medio_subsistema(self) -> Dict[str, np.ndarray]:
        """
        Custo Marginal de Operação (CMO) médio por subsistema
        e por semana.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada um
        array onde a posição [i - 1] contém os dados do período
        i do DECOMP.
        """
        dict_cmo: Dict[str, np.ndarray] = {}
        for i, ssis in enumerate(self.subsistema):
            if "Med" in ssis:
                str_subsistema = ssis.split("_")[1]
                dict_cmo[str_subsistema] = self.tabela[i, :]
        return dict_cmo


class GeracaoTermicaSubsistemaRelato:
    """
    Armazena os dados de saída existentes no relato do DECOMP
    referentes à geração de térmicas (MWmed) por subsistema.

    Esta classe armazena a tabela de Geração por subsistema
    e por semana do DECOMP.

    **Parâmetros**

    - subsistema: `List[str]`
    - tabela: `np.ndarray`

    """
    def __init__(self,
                 subsistema: List[str],
                 tabela: np.ndarray):
        self.subsistema = subsistema
        self.tabela = tabela

    def __eq__(self, o: object) -> bool:
        """
        A igualdade entre GeracaoTermicaSubsistemaRelato
        avalia todos os campos.
        """
        if not isinstance(o, GeracaoTermicaSubsistemaRelato):
            return False
        gt: GeracaoTermicaSubsistemaRelato = o
        eq_subsistema = self.subsistema == gt.subsistema
        eq_tabela = np.array_equal(self.tabela, gt.tabela)
        return all([eq_subsistema, eq_tabela])

    @property
    def geracao_subsistema(self) -> Dict[str, np.ndarray]:
        """
        Geração Térmica (MWmed) por subsistema e por semana
        como fornecido no arquivo relato.rvX do DECOMP.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada um
        array onde a posição [i - 1] contém os dados do período
        i do DECOMP.
        """
        dict_gt: Dict[str, np.ndarray] = {}
        for i, ssis in enumerate(self.subsistema):
            dict_gt[ssis] = self.tabela[i, :]
        return dict_gt


class EnergiaArmazenadaSubsistemaRelato:
    """
    Armazena os dados de saída existentes no relato do DECOMP
    referentes à energia armazenada (% EARMax) por subsistema.

    Esta classe armazena a tabela de armazenamento por subsistema
    inicial e por semana do DECOMP.

    **Parâmetros**

    - subsistema: `List[str]`
    - tabela: `np.ndarray`

    """
    def __init__(self,
                 subsistema: List[str],
                 tabela: np.ndarray):
        self.subsistema = subsistema
        self.tabela = tabela

    def __eq__(self, o: object) -> bool:
        """
        A igualdade entre EnergiaArmazenadaSubsistemaRelato
        avalia todos os campos.
        """
        if not isinstance(o, EnergiaArmazenadaSubsistemaRelato):
            return False
        earm: EnergiaArmazenadaSubsistemaRelato = o
        eq_subsistema = self.subsistema == earm.subsistema
        eq_tabela = np.array_equal(self.tabela, earm.tabela)
        return all([eq_subsistema, eq_tabela])

    @property
    def armazenamento_inicial_subsistema(self) -> Dict[str, float]:
        """
        Energia Armazenada inicial (% EARMax) por subsistema
        como fornecido no arquivo relato.rvX do DECOMP.

        **Retorna**

        `Dict[str, float]`

        **Sobre**

        O acesso é feito com `[subsistema]`.
        """
        dict_gt: Dict[str, float] = {}
        for i, ssis in enumerate(self.subsistema):
            dict_gt[ssis] = self.tabela[i, 0]
        return dict_gt

    @property
    def armazenamento_subsistema(self) -> Dict[str, np.ndarray]:
        """
        Energia Armazenada (% EARMax) por subsistema e por
        período de execução como fornecido no arquivo
        relato.rvX do DECOMP.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada uma
        `np.ndarray` onde a entrada [i - 1] possui o valor
        referente ap período i do DECOMP.
        """
        dict_earm: Dict[str, np.ndarray] = {}
        for i, ssis in enumerate(self.subsistema):
            dict_earm[ssis] = self.tabela[i, 1:]
        return dict_earm


class Relato:
    """
    Armazena os dados de saída do DECOMP referentes ao
    acompanhamento do programa.

    Esta classe lida com as informações de entrada fornecidas ao
    DECOMP e reproduzidas no `relato.rvx`, bem como as saídas finais
    da execução: custos de operação, despacho de térmicas, etc.

    Em versões futuras, esta classe pode passar a ler os dados
    de execução intermediárias do programa.

    **Parâmetros**

    - dados_gerais: `DadosGeraisRelato`
    - cmo: `CMORelato`
    - geracao_termica_subsistema: `GeracaoTermicaSubsistemaRelato`

    """
    def __init__(self,
                 dados_gerais: DadosGeraisRelato,
                 cmo: CMORelato,
                 geracao_termica_subsistema: GeracaoTermicaSubsistemaRelato,
                 earm_subsistema: EnergiaArmazenadaSubsistemaRelato):
        self.dados_gerais = dados_gerais
        self._cmo = cmo
        self._geracao_termica_subsistema = geracao_termica_subsistema
        self._earm_subsistema = earm_subsistema

    def __eq__(self, o: object) -> bool:
        """
        A igualdade entre Relato avalia todos os campos.
        """
        if not isinstance(o, Relato):
            return False
        rel: Relato = o
        dif = False
        for (k, u), (_, v) in zip(self.__dict__.items(),
                                  rel.__dict__.items()):
            if u != v:
                dif = True
                break
        return not dif

    @property
    def cmo_medio_subsistema(self) -> Dict[str, np.ndarray]:
        """
        Custo Marginal de Operação (CMO) médio por subsistema
        e por semana.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada um
        array onde a posição [i - 1] contém os dados do período
        i do DECOMP.
        """
        return self._cmo.custo_medio_subsistema

    @property
    def geracao_termica_subsistema(self) -> Dict[str, np.ndarray]:
        """
        Geração Térmica (MWmed) por subsistema e por semana
        como fornecido no arquivo relato.rvX do DECOMP.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada um
        array onde a posição [i - 1] contém os dados do período
        i do DECOMP.
        """
        return self._geracao_termica_subsistema.geracao_subsistema

    @property
    def energia_armazenada_inicial_subsistema(self) -> Dict[str, float]:
        """
        Energia Armazenada inicial (% EARMax) por subsistema
        como fornecido no arquivo relato.rvX do DECOMP.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]`.
        """
        return self._earm_subsistema.armazenamento_inicial_subsistema

    @property
    def energia_armazenada_subsistema(self) -> Dict[str, np.ndarray]:
        """
        Energia Armazenada (% EARMax) por subsistema e por
        período de execução como fornecido no arquivo
        relato.rvX do DECOMP.

        **Retorna**

        `Dict[str, np.ndarray]`

        **Sobre**

        O acesso é feito com `[subsistema]` e é retornada uma
        `np.ndarray` onde a entrada [i - 1] possui o valor
        referente ap período i do DECOMP.
        """
        return self._earm_subsistema.armazenamento_subsistema