from idecomp.decomp.modelos.dadger import (
    TE,
    SB,
    UH,
    CT,
    UE,
    DP,
    PQ,
    CD,
    FP,
    RI,
    IA,
    TX,
    GP,
    NI,
    DT,
    MP,
    MT,
    FD,
    VE,
    RE,
    LU,
    FU,
    FT,
    FI,
    VI,
    IR,
    CI,
    CE,
    FC,
    EA,
    ES,
    QI,
    TI,
    RQ,
    EZ,
    RT,
    HV,
    LV,
    CV,
    HQ,
    LQ,
    CQ,
    AR,
    EV,
    FJ,
    HE,
    CM,
    PD,
    PU,
    RC,
    PE,
    TS,
    PV,
    CX,
    FA,
    VT,
    CS,
    ACNUMPOS,
    ACNUMJUS,
    ACDESVIO,
    ACVOLMIN,
    ACVOLMAX,
    ACCOTVOL,
    ACCOTARE,
    ACPROESP,
    ACPERHID,
    ACNCHAVE,
    ACCOTVAZ,
    ACCOFEVA,
    ACNUMCON,
    ACNUMMAQ,
    ACPOTEFE,
    ACALTEFE,
    ACVAZEFE,
    ACJUSMED,
    ACVERTJU,
    ACVAZMIN,
    ACTIPERH,
    ACJUSENA,
    ACVSVERT,
    ACVMDESV,
    ACNPOSNW,
)

import pandas as pd  # type: ignore
from cfinterface.files.registerfile import RegisterFile
from cfinterface.components.register import Register
from typing import Type, List, Optional, TypeVar, Any, Union


class Dadger(RegisterFile):
    """
    Armazena os dados de entrada gerais do DECOMP.

    Esta classe lida com as informações de entrada fornecidas ao
    DECOMP no `dadger.rvx`. Possui métodos para acessar individualmente
    cada registro, editá-lo e também cria alguns novos registros.

    É possível ler as informações existentes em arquivos a partir do
    método `le_arquivo()` e escreve um novo arquivo a partir do método
    `escreve_arquivo()`.

    """

    T = TypeVar("T")

    AC = Union[
        ACNUMPOS,
        ACNUMJUS,
        ACDESVIO,
        ACVOLMIN,
        ACVOLMAX,
        ACCOTVOL,
        ACCOTARE,
        ACPROESP,
        ACPERHID,
        ACNCHAVE,
        ACCOTVAZ,
        ACCOFEVA,
        ACNUMCON,
        ACNUMMAQ,
        ACPOTEFE,
        ACALTEFE,
        ACVAZEFE,
        ACJUSMED,
        ACVERTJU,
        ACVAZMIN,
        ACTIPERH,
        ACJUSENA,
        ACVSVERT,
        ACVMDESV,
        ACNPOSNW,
    ]

    REGISTERS = [
        TE,
        SB,
        UH,
        CT,
        UE,
        DP,
        PQ,
        CD,
        FP,
        RI,
        IA,
        TX,
        GP,
        NI,
        DT,
        MP,
        MT,
        FD,
        VE,
        RE,
        LU,
        FU,
        FT,
        FI,
        VI,
        IR,
        CI,
        CE,
        FC,
        EA,
        ES,
        QI,
        TI,
        RQ,
        EZ,
        RT,
        HV,
        LV,
        CV,
        HQ,
        LQ,
        CQ,
        AR,
        EV,
        FJ,
        HE,
        CM,
        ACNUMPOS,
        ACNUMJUS,
        ACDESVIO,
        ACVOLMIN,
        ACVOLMAX,
        ACCOTVOL,
        ACCOTARE,
        ACPROESP,
        ACPERHID,
        ACNCHAVE,
        ACCOTVAZ,
        ACCOFEVA,
        ACNUMCON,
        ACNUMMAQ,
        ACPOTEFE,
        ACALTEFE,
        ACVAZEFE,
        ACJUSMED,
        ACVERTJU,
        ACVAZMIN,
        ACTIPERH,
        ACJUSENA,
        ACVSVERT,
        ACVMDESV,
        ACNPOSNW,
    ]

    def __init__(self, data=...) -> None:
        super().__init__(data)

    @classmethod
    def le_arquivo(cls, diretorio: str, nome_arquivo="dadger.rv0") -> "Dadger":
        return cls.read(diretorio, nome_arquivo)

    def escreve_arquivo(self, diretorio: str, nome_arquivo="dadger.rv0"):
        self.write(diretorio, nome_arquivo)

    def __registros_por_tipo(self, registro: Type[T]) -> List[T]:
        """
        Obtém um gerador de blocos de um tipo, se houver algum no arquivo.
        :param bloco: Um tipo de bloco para ser lido
        :type bloco: T
        :param indice: O índice do bloco a ser acessado, dentre os do tipo
        :type indice: int
        """
        return [b for b in self.data.of_type(registro)]

    def __obtem_registro(self, tipo: Type[T]) -> Optional[T]:
        """ """
        r = self.__obtem_registros(tipo)
        return r[0] if len(r) > 0 else None

    def __obtem_registros(self, tipo: Type[T]) -> List[T]:
        return self.__registros_por_tipo(tipo)

    def __obtem_registros_com_filtros(
        self, tipo_registro: Type[T], **kwargs
    ) -> Optional[Union[T, List[T]]]:
        def __atende(r) -> bool:
            condicoes: List[bool] = []
            for k, v in kwargs.items():
                if v is not None:
                    condicoes.append(getattr(r, k) == v)
            return all(condicoes)

        regs_filtro = [
            r for r in self.__obtem_registros(tipo_registro) if __atende(r)
        ]
        if len(regs_filtro) == 0:
            return None
        elif len(regs_filtro) == 1:
            return regs_filtro[0]
        else:
            return regs_filtro

    def cria_registro(self, anterior: Register, registro: Register):
        """
        Adiciona um registro ao arquivo após um outro registro previamente
        existente.

        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        self.data.add_after(anterior, registro)

    def deleta_registro(self, registro: Register):
        """
        Remove um registro existente no arquivo.

        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        self.data.remove(registro)

    def lista_registros(self, tipo: Type[T]) -> List[T]:
        """
        Lista todos os registros presentes no arquivo que tenham o tipo `T`.

        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        return [r for r in self.data.of_type(tipo)]

    def append_registro(self, registro: Register):
        """
        Adiciona um registro ao arquivo na última posição.


        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        self.data.append(registro)

    def preppend_registro(self, registro: Register):
        """
        Adiciona um registro ao arquivo na primeira posição.

        Este método existe para retrocompatibilidade e deve ser substituído
        quando for suportado na classe :class:`RegisterFile`.
        """
        self.data.preppend(registro)

    @property
    def te(self) -> Optional[TE]:
        """
        Obtém o (único) registro que define o nome do estudo no
        :class:`Dadger`

        :return: Um registro, se existir.
        :rtype: :class:`TE` | None.
        """
        return self.__obtem_registro(TE)

    def sb(
        self,
        codigo: Optional[int] = None,
        nome: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[SB, List[SB], pd.DataFrame]]:
        """
        Obtém um registro que define os subsistemas existentes
        no estudo descrito pelo :class:`Dadger`.

        :param codigo: código que especifica o registro do subsistema
        :type codigo: int | None
        :param nome: nome do subsistema
        :type nome: str | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`SB` | list[:class:`SB`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(SB)
        else:
            return self.__obtem_registros_com_filtros(
                SB, codigo=codigo, nome=nome
            )

    def uh(
        self,
        codigo: Optional[int] = None,
        ree: Optional[int] = None,
        volume_inicial: Optional[float] = None,
        evaporacao: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[UH, List[UH], pd.DataFrame]]:
        """
        Obtém um registro que define uma usina hidrelétrica existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo: índice do código que especifica o registro da UHE
        :type codigo: int | None
        :param ree: índice do ree da UHE
        :type ree: int | None
        :param volume_inicial: volume inicial da UHE
        :type volume_inicial: float | None
        :param evaporacao: consideração da evaporação na UHE
        :type evaporacao: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`UH` | list[:class:`UH`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(UH)
        else:
            return self.__obtem_registros_com_filtros(
                UH,
                codigo=codigo,
                ree=ree,
                volume_inicial=volume_inicial,
                evaporacao=evaporacao,
            )

    def ct(
        self,
        codigo: Optional[int] = None,
        estagio: Optional[int] = None,
        subsistema: Optional[int] = None,
        nome: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[CT, List[CT], pd.DataFrame]]:
        """
        Obtém um registro que define uma usina termelétrica existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo: código que especifica o registro da UTE
        :type codigo: int | None
        :param estagio: estágio associado ao registro
        :type estagio: int | None
        :param subsistema: subsistema da UTE
        :type subsistema: str | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`CT` | list[:class:`CT`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(CT)
        else:
            return self.__obtem_registros_com_filtros(
                CT,
                codigo=codigo,
                estagio=estagio,
                subsistema=subsistema,
                nome=nome,
            )

    def dp(
        self,
        estagio: Optional[int] = None,
        subsistema: Optional[int] = None,
        num_patamares: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[DP, List[DP], pd.DataFrame]]:
        """
        Obtém um registro que define as durações dos patamares
        no estudo descrito pelo :class:`Dadger`.

        :param estagio: estágio sobre o qual serão
            definidas as durações dos patamares
        :type estagio: int | None
        :param subsistema: subsistema para o qual
            valerão os patamares.
        :type subsistema: int | None
        :param num_patamares: número de patamares
        :type num_patamares: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`DP` | list[:class:`DP`] |
            :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(DP)
        else:
            return self.__obtem_registros_com_filtros(
                DP,
                estagio=estagio,
                subsistema=subsistema,
                num_patamares=num_patamares,
            )

    def pq(
        self,
        nome: Optional[str] = None,
        subsistema: Optional[int] = None,
        estagio: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[PQ, List[PQ], pd.DataFrame]]:
        """
        Obtém um registro que define as gerações das pequenas usinas
        no estudo descrito pelo :class:`Dadger`.

        :param nome: o nome das gerações
        :param subsistema: subsistema para o qual
            valerão as gerações
        :param estagio: estágio sobre o qual serão
            definidas as gerações
        :type estagio: int | None
        :type subsistema: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`PQ` | list[:class:`PQ`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(PQ)
        else:
            return self.__obtem_registros_com_filtros(
                PQ,
                nome=nome,
                estagio=estagio,
                subsistema=subsistema,
            )

    def ac(
        self,
        uhe: int,
        modificacao: Any,
        df: bool = False,
        **kwargs,
    ) -> Optional[Union[AC, List[AC], pd.DataFrame]]:
        """
        Obtém um registro que define modificações nos parâmetros
        das UHE em um :class:`Dadger`.

        :param uhe: código da UHE modificada
        :type uhe: int
        :param modificacao: classe da modificação realizada
        :type modificacao: subtipos do tipo `AC`
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: `AC` | list[`AC`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(modificacao)
        else:
            return self.__obtem_registros_com_filtros(
                modificacao, **{"uhe": uhe, **kwargs}
            )

    def cd(
        self,
        numero_curva: Optional[int] = None,
        subsistema: Optional[int] = None,
        nome_curva: Optional[str] = None,
        estagio: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[CD, List[CD], pd.DataFrame]]:
        """
        Obtém um registro que define as curvas de déficit
        no estudo descrito pelo :class:`Dadger`.

        :param numero_curva: Índice da curva de déficit descrita
        :type numero_curva: int | None
        :param subsistema: subsistema para o qual valerá a curva.
        :type subsistema: int | None
        :param nome_curva: nome da curva.
        :type nome_curva: str | None
        :param estagio: estagio para o qual valerá a curva.
        :type estagio: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`LU` | list[:class:`LU`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(CD)
        else:
            return self.__obtem_registros_com_filtros(
                CD,
                numero_curva=numero_curva,
                subsistema=subsistema,
                nome_curva=nome_curva,
                estagio=estagio,
            )

    @property
    def tx(self) -> Optional[TX]:
        """
        Obtém o (único) registro que define a taxa de desconto
        aplicada no estudo definido no :class:`Dadger`

        :return: Um registro, se existir.
        :rtype: :class:`TX` | None.
        """
        return self.__obtem_registro(TX)

    @property
    def gp(self) -> Optional[GP]:
        """
        Obtém o (único) registro que define o gap para convergência
        considerado no estudo definido no :class:`Dadger`

        :return: Um registro, se existir.
        :rtype: :class:`GP` | None.
        """
        return self.__obtem_registro(GP)

    @property
    def ni(self) -> Optional[NI]:
        """
        Obtém o (único) registro que define o número máximo de iterações
        do DECOMP no estudo definido no :class:`Dadger`

        :return: Um registro, se existir.
        :rtype: :class:`NI` | None.
        """
        return self.__obtem_registro(NI)

    @property
    def dt(self) -> Optional[DT]:
        """
        Obtém o (único) registro que define a data de referência do
        estudo definido no :class:`Dadger`

        :return: Um registro, se existir.
        :rtype: :class:`DT` | None.
        """
        return self.__obtem_registro(DT)

    def re(
        self,
        codigo: Optional[int] = None,
        estagio_inicial: Optional[int] = None,
        estagio_final: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[RE, List[RE], pd.DataFrame]]:
        """
        Obtém um registro que cadastra uma restrição elétrica existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo: código que especifica o registro
            da restrição elétrica
        :type codigo: int | None
        :param estagio_inicial: estágio inicial da restrição elétrica
        :type estagio_inicial: int | None
        :param estagio_final: estágio final da restrição elétrica
        :type estagio_final: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RE` | list[:class:`RE`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(RE)
        else:
            return self.__obtem_registros_com_filtros(
                RE,
                codigo=codigo,
                estagio_inicial=estagio_inicial,
                estagio_final=estagio_final,
            )

    def lu(  # noqa
        self,
        codigo: Optional[int] = None,
        estagio: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[LU, List[LU], pd.DataFrame]]:
        """
        Obtém um registro que especifica os limites inferiores e
        superiores por patamar de uma restrição elétrica existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo: Índice do código que especifica o registro
            da restrição elétrica
        :type codigo: int | None
        :param estagio: Estágio sobre o qual valerão os limites da
            restrição elétricas
        :type estagio: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`LU` | list[:class:`LU`] | :class:`pd.DataFrame` | None

        **Exemplos**

        Para um objeto :class:`Dadger` que possua uma restrição RE
        de código 1, definida para os estágios de 1 a 5, com limites
        LU definidos apenas para o estágio 1, estes podem ser acessados com:

        >>> lu = dadger.lu(1, 1)
        >>> lu
            <idecomp.decomp.modelos.dadger.LU object at 0x0000026E5C269550>

        Se for acessado o registro LU de um estágio fora dos limites da
        restrição RE, isso resultará em um erro:

        >>> dadger.lu(1, 7)
            Traceback (most recent call last):
            ...
            ValueError: Estágio 7 fora dos limites do registro RE

        Por outro lado, se for acessado o registro LU em um estágio dentro
        dos limites do registro RE, porém sem limites próprios definidos,
        será criado um registro idêntico ao do último estágio existente,
        e este será retornado:

        >>> lu2 = dadger.lu(1, 5)
        >>> lu.limites_inferiores == lu2.limites_inferiores
            True

        """

        def cria_registro() -> Optional[LU]:
            re = self.re(codigo=codigo)
            if isinstance(re, list) or re is None:
                return None
            ei = re.estagio_inicial
            ef = re.estagio_final
            if any([estagio is None, ei is None, ef is None]):
                return None
            ultimo_registro = None
            if ei is not None and estagio <= ef:  # type: ignore
                for e in range(ei, estagio + 1):  # type: ignore
                    registro_estagio = self.__obtem_registros_com_filtros(
                        LU, codigo=codigo, estagio=e
                    )
                    if registro_estagio is not None:
                        ultimo_registro = registro_estagio
            if isinstance(ultimo_registro, LU):
                novo_registro = LU(
                    data=[None] * len(ultimo_registro.data),
                )
                novo_registro.codigo = ultimo_registro.codigo
                novo_registro.limites_inferiores = (
                    ultimo_registro.limites_inferiores
                )
                novo_registro.limites_superiores = (
                    ultimo_registro.limites_superiores
                )
                novo_registro.estagio = estagio
                self.data.add_after(ultimo_registro, novo_registro)
                return novo_registro
            return None

        if df:
            return self._as_df(LU)
        else:
            lu = self.__obtem_registros_com_filtros(
                LU, codigo=codigo, estagio=estagio
            )
            if isinstance(lu, list):
                return lu
            if lu is None:
                lu = cria_registro()
            return lu

    def fu(
        self,
        restricao: Optional[int] = None,
        estagio: Optional[int] = None,
        uhe: Optional[int] = None,
        coeficiente: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[FU, List[FU], pd.DataFrame]]:
        """
        Obtém um registro que cadastra os coeficientes das restrições
        elétricas.

        :param restricao: código que especifica o registro
        :type restricao: int | None
        :param estagio: o estágio do coeficiente
        :type estagio: int | None
        :param uhe: o código da UHE para a restrição
        :type uhe: int | None
        :param coeficiente: valor do coeficiente para a usina
            na restrição
        :type coeficiente: float | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se houverem.
        :rtype: :class:`FU` | list[:class:`FU`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(FU)
        else:
            return self.__obtem_registros_com_filtros(
                FU,
                restricao=restricao,
                uhe=uhe,
                estagio=estagio,
                coeficiente=coeficiente,
            )

    def ft(
        self,
        restricao: Optional[int] = None,
        estagio: Optional[int] = None,
        ute: Optional[int] = None,
        coeficiente: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[FT, List[FT], pd.DataFrame]]:
        """
        Obtém um registro que cadastra os coeficientes das restrições
        elétricas.

        :param restricao: código que especifica o registro
        :type restricao: int | None
        :param estagio: o estágio do coeficiente
        :type estagio: int | None
        :param ute: o código da UTE para a restrição
        :type ute: int | None
        :param coeficiente: valor do coeficiente para a usina
            na restrição
        :type coeficiente: float | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se houverem.
        :rtype: :class:`FT` | list[:class:`FT`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(FT)
        else:
            return self.__obtem_registros_com_filtros(
                FT,
                restricao=restricao,
                ute=ute,
                estagio=estagio,
                coeficiente=coeficiente,
            )

    def fi(
        self,
        restricao: Optional[int] = None,
        estagio: Optional[int] = None,
        de: Optional[int] = None,
        para: Optional[int] = None,
        coeficiente: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[FI, List[FI], pd.DataFrame]]:
        """
        Obtém um registro que cadastra os coeficientes das restrições
        elétricas.

        :param restricao: código que especifica o registro
        :type restricao: int | None
        :param estagio: o estágio do coeficiente
        :type estagio: int | None
        :param de: o código do subsistema DE
        :type de: int | None
        :param para: o código do subsistema PARA
        :type para: int | None
        :param coeficiente: valor do coeficiente para a interligação
            na restrição
        :type coeficiente: float | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se houverem.
        :rtype: :class:`FI` | list[:class:`FI`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(FI)
        else:
            return self.__obtem_registros_com_filtros(
                FI,
                restricao=restricao,
                estagio=estagio,
                de=de,
                para=para,
                coeficiente=coeficiente,
            )

    def vi(
        self,
        uhe: Optional[int] = None,
        duracao: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[VI, List[VI], pd.DataFrame]]:
        """
        Obtém um registro que especifica os tempos de viagem da
        água em uma UHE existente no no estudo descrito
        pelo :class:`Dadger`.

        :param uhe: Índice da UHE associada aos tempos de viagem
        :type uhe: int | None
        :param duracao: duração, em horas, da viagem da água
        :type duracao: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`VI` | list[:class:`VI`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(VI)
        else:
            return self.__obtem_registros_com_filtros(
                VI, uhe=uhe, duracao=duracao
            )

    def ir(
        self, tipo: Optional[str] = None, df: bool = False
    ) -> Optional[Union[IR, List[IR], pd.DataFrame]]:
        """
        Obtém um registro que especifica os relatórios de saída
        a serem produzidos pelo DECOMP após a execução do estudo
        descrito no :class:`Dadger`.

        :param tipo: Mnemônico do tipo de relatório especificado
            no registro
        :type tipo: str | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`IR` | list[:class:`IR`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(IR)
        else:
            return self.__obtem_registros_com_filtros(IR, tipo=tipo)

    def rt(
        self, restricao: Optional[str] = None, df: bool = False
    ) -> Optional[Union[RT, List[RT], pd.DataFrame]]:
        """
        Obtém um registro que especifica uma retirada de restrição
        de soleira de vertedouro ou canal de desvio.

        :param restricao: Mnemônico da restrição retirada (CRISTA ou
            DESVIO)
        :type restricao: str | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RT` | list[:class:`RT`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(RT)
        else:
            return self.__obtem_registros_com_filtros(RT, restricao=restricao)

    def fc(
        self,
        tipo: Optional[str] = None,
        caminho: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[FC, List[FC], pd.DataFrame]]:
        """
        Obtém um registro que especifica os caminhos para os
        arquivos com a FCF do NEWAVE.

        :param tipo: Mnemônico do tipo de FCF especificado
            no registro
        :type tipo: str | None
        :param caminho: caminho para o arquivo com a FCF
        :type caminho: str | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`FC` | list[:class:`FC`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(FC)
        else:
            return self.__obtem_registros_com_filtros(
                FC, tipo=tipo, caminho=caminho
            )

    def ea(self, ree: Optional[int] = None) -> Optional[Union[EA, List[EA]]]:
        """
        Obtém um registro que especifica a ENA dos meses anteriores
        ao estudo.

        :param ree: Código do REE
        :type ree: int | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`EA` | list[:class:`EA`] | None
        """
        return self.__obtem_registros_com_filtros(EA, ree=ree)

    def es(
        self,
        ree: Optional[int] = None,
        numero_semanas: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[ES, List[ES], pd.DataFrame]]:
        """
        Obtém um registro que especifica a ENA das semanas anteriores
        ao estudo.

        :param ree: Código do REE
        :type ree: int | None
        :param numero_semanas: Número de semanas do mês anterior
        :type numero_semanas: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`ES` | list[:class:`ES`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(ES)
        else:
            return self.__obtem_registros_com_filtros(
                ES, ree=ree, numero_semanas=numero_semanas
            )

    def qi(
        self, uhe: Optional[int] = None, df: bool = False
    ) -> Optional[Union[QI, List[QI], pd.DataFrame]]:
        """
        Obtém um registro que especifica o tempo de viagem
        para cálculo da ENA.

        :param uhe: Código da UHE
        :type uhe: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`QI` | list[:class:`QI`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(QI)
        else:
            return self.__obtem_registros_com_filtros(QI, uhe=uhe)

    def ti(
        self, codigo: Optional[int] = None, df: bool = False
    ) -> Optional[Union[TI, List[TI], pd.DataFrame]]:
        """
        Obtém um registro que especifica as taxas de irrigação
        por posto (UHE) existente no estudo especificado no :class:`Dadger`

        :param codigo: Código da UHE associada ao registro
        :type codigo: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`TI` | list[:class:`TI`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(TI)
        else:
            return self.__obtem_registros_com_filtros(TI, codigo=codigo)

    def fp(
        self,
        codigo: Optional[int] = None,
        estagio: Optional[int] = None,
        tipo_entrada_janela_turbinamento: Optional[int] = None,
        numero_pontos_turbinamento: Optional[int] = None,
        limite_inferior_janela_turbinamento: Optional[float] = None,
        limite_superior_janela_turbinamento: Optional[float] = None,
        tipo_entrada_janela_volume: Optional[int] = None,
        numero_pontos_volume: Optional[int] = None,
        limite_inferior_janela_volume: Optional[float] = None,
        limite_superior_janela_volume: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[FP, List[FP], pd.DataFrame]]:
        """
        Obtém um registro que especifica as taxas de irrigação
        por posto (UHE) existente no estudo especificado no :class:`Dadger`

        :param codigo: Código da UHE associada ao registro
        :type codigo: int | None
        :param estagio: Estágio de definição da FP da UHE
        :type estagio: int | None
        :param tipo_entrada_janela_turbinamento: unidade de entrada
            dos valores da janela de turbinamento
        :type tipo_entrada_janela_turbinamento: int | None
        :param numero_pontos_turbinamento: número de pontos para
            discretização da janela
        :type numero_pontos_turbinamento: int | None
        :param limite_inferior_janela_turbinamento: limite inferior
            da janela
        :type limite_inferior_janela_turbinamento: float | None
        :param limite_superior_janela_turbinamento: limite superior
            da janela
        :type limite_superior_janela_turbinamento: float | None
        :param tipo_entrada_janela_volume: unidade de entrada
            dos valores da janela de volume
        :type tipo_entrada_janela_volume: int | None
        :param numero_pontos_volume: número de pontos para
            discretização da janela
        :type numero_pontos_volume: int | None
        :param limite_inferior_janela_volume: limite inferior
            da janela
        :type limite_inferior_janela_volume: float | None
        :param limite_superior_janela_volume: limite superior
            da janela
        :type limite_superior_janela_volume: float | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`FP` | list[:class:`FP`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(FP)
        else:
            return self.__obtem_registros_com_filtros(
                FP,
                codigo=codigo,
                estagio=estagio,
                tipo_entrada_janela_turbinamento=tipo_entrada_janela_turbinamento,
                numero_pontos_turbinamento=numero_pontos_turbinamento,
                limite_inferior_janela_turbinamento=limite_inferior_janela_turbinamento,
                limite_superior_janela_turbinamento=limite_superior_janela_turbinamento,
                tipo_entrada_janela_volume=tipo_entrada_janela_volume,
                numero_pontos_volume=numero_pontos_volume,
                limite_inferior_janela_volume=limite_inferior_janela_volume,
                limite_superior_janela_volume=limite_superior_janela_volume,
            )

    def rq(
        self, ree: Optional[int] = None, df: bool = False
    ) -> Optional[Union[RQ, List[RQ], pd.DataFrame]]:
        """
        Obtém um registro que especifica as vazões mínimas históricas
        por REE existentes no estudo especificado no :class:`Dadger`

        :param ree: Código do REE
        :type ree: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`RQ` | list[:class:`RQ`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(RQ)
        else:
            return self.__obtem_registros_com_filtros(RQ, ree=ree)

    def ve(
        self, codigo: Optional[int] = None, df: bool = False
    ) -> Optional[Union[VE, List[VE], pd.DataFrame]]:
        """
        Obtém um registro que especifica os volumes de espera
        por posto (UHE) existente no estudo especificado no :class:`Dadger`

        :param codigo: Código do posto da UHE associada
        :type codigo: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`VE` | list[:class:`VE`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(VE)
        else:
            return self.__obtem_registros_com_filtros(VE, codigo=codigo)

    def hv(
        self,
        codigo: Optional[int] = None,
        estagio_inicial: Optional[int] = None,
        estagio_final: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[HV, List[HV], pd.DataFrame]]:
        """
        Obtém um registro que cadastra uma restrição de volume mínimo
        armazenado existente no estudo descrito pelo :class:`Dadger`.

        :param codigo: código que especifica o registro
            da restrição de volume
        :type codigo: int | None
        :param estagio_inicial: estágio inicial da restrição de volume
        :type estagio_inicial: int | None
        :param estagio_final: estágio final da restrição de volume
        :type estagio_final: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`HV` | list[:class:`HV`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(HV)
        else:
            return self.__obtem_registros_com_filtros(
                HV,
                codigo=codigo,
                estagio_inicial=estagio_inicial,
                estagio_final=estagio_final,
            )

    def lv(  # noqa
        self,
        codigo: Optional[int] = None,
        estagio: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[LV, List[LV], pd.DataFrame]]:
        """
        Obtém um registro que especifica os limites inferior e
        superior de uma restrição de volume mínimo existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo: Índice do código que especifica o registro
            da restrição de volume
        :type codigo: int | None
        :param estagio: Estágio sobre o qual valerão os limites da
            restrição de volume
        :type estagio: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`LV` | list[:class:`LV`] | :class:`pd.DataFrame` | None

        **Exemplos**

        Para um objeto :class:`Dadger` que possua uma restrição HV
        de código 1, definida para os estágios de 1 a 5, com limites
        LV definidos apenas para o estágio 1, estes podem ser acessados com:

        >>> lv = dadger.lv(1, 1)
        >>> lv
            <idecomp.decomp.modelos.dadger.LV object at 0x0000026E5C269550>

        Se for acessado o registro LV de um estágio fora dos limites da
        restrição HV, isso resultará em um erro:

        >>> dadger.lv(1, 7)
            Traceback (most recent call last):
            ...
            ValueError: Estágio 7 fora dos limites do registro HV

        Por outro lado, se for acessado o registro LV em um estágio dentro
        dos limites do registro HV, porém sem limites próprios definidos,
        será criado um registro idêntico ao do último estágio existente,
        e este será retornado:

        >>> lv2 = dadger.lv(1, 5)
        >>> lv.limite_inferior == lv2.limite_inferior
            True

        """

        def cria_registro() -> Optional[LV]:
            hv = self.hv(codigo=codigo)
            if isinstance(hv, list) or hv is None:
                return None
            ei = hv.estagio_inicial
            ef = hv.estagio_final
            if any([estagio is None, ei is None, ef is None]):
                return None
            ultimo_registro = None
            if ei is not None and estagio <= ef:  # type: ignore
                for e in range(ei, estagio + 1):  # type: ignore
                    registro_estagio = self.__obtem_registros_com_filtros(
                        LV, codigo=codigo, estagio=e
                    )
                    if registro_estagio is not None:
                        ultimo_registro = registro_estagio
            if isinstance(ultimo_registro, LV):
                novo_registro = LV(
                    data=[None] * len(ultimo_registro.data),
                )
                novo_registro.codigo = codigo
                novo_registro.limite_inferior = ultimo_registro.limite_inferior
                novo_registro.limite_superior = ultimo_registro.limite_superior
                novo_registro.estagio = estagio
                self.data.add_after(ultimo_registro, novo_registro)
                return novo_registro
            return None

        if df:
            return self._as_df(LV)
        else:
            lv = self.__obtem_registros_com_filtros(
                LV, codigo=codigo, estagio=estagio
            )
            if isinstance(lv, list):
                return lv
            if lv is None:
                lv = cria_registro()
            return lv

    def cv(
        self,
        restricao: Optional[int] = None,
        estagio: Optional[int] = None,
        uhe: Optional[int] = None,
        coeficiente: Optional[float] = None,
        tipo: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[CV, List[CV], pd.DataFrame]]:
        """
        Obtém um registro que cadastra os coeficientes das restrições
        de volume.

        :param restricao: código que especifica o registro
        :type restricao: int | None
        :param estagio: o estágio do coeficiente
        :type estagio: int | None
        :param uhe: o código da UHE para a restrição
        :type uhe: int | None
        :param coeficiente: valor do coeficiente para a usina
            na restrição
        :type coeficiente: float | None
        :param tipo: o mnemônico de tipo da restrição
        :type tipo: str | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se houverem.
        :rtype: :class:`CV` | list[:class:`CV`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(CV)
        else:
            return self.__obtem_registros_com_filtros(
                CV,
                restricao=restricao,
                uhe=uhe,
                estagio=estagio,
                coeficiente=coeficiente,
                tipo=tipo,
            )

    def hq(
        self,
        codigo: Optional[int] = None,
        estagio_inicial: Optional[int] = None,
        estagio_final: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[HQ, List[HQ], pd.DataFrame]]:
        """
        Obtém um registro que cadastra uma restrição de vazão
        existente no estudo descrito pelo :class:`Dadger`.

        :param codigo: código que especifica o registro
            da restrição de vazão
        :type codigo: int | None
        :param estagio_inicial: estágio inicial da restrição de vazão
        :type estagio_inicial: int | None
        :param estagio_final: estágio final da restrição de vazão
        :type estagio_final: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`HQ` | list[:class:`HQ`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(HQ)
        else:
            return self.__obtem_registros_com_filtros(
                HQ,
                codigo=codigo,
                estagio_inicial=estagio_inicial,
                estagio_final=estagio_final,
            )

    def lq(  # noqa
        self,
        codigo: Optional[int] = None,
        estagio: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[LQ, List[LQ], pd.DataFrame]]:
        """
        Obtém um registro que especifica os limites inferiores e
        superiores por patamar de uma restrição de vazão existente
        no estudo descrito pelo :class:`Dadger`.

        :param codigo: Índice do código que especifica o registro
            da restrição de vazão
        :type codigo: int | None
        :param estagio: Estágio sobre o qual valerão os limites da
            restrição de vazão
        :type estagio: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`LQ` | list[:class:`LQ`] | :class:`pd.DataFrame` | None

        **Exemplos**

        Para um objeto :class:`Dadger` que possua uma restrição HQ
        de código 1, definida para os estágios de 1 a 5, com limites
        LQ definidos apenas para o estágio 1, estes podem ser acessados com:

        >>> lq = dadger.lq(1, 1)
        >>> lq
            <idecomp.decomp.modelos.dadger.LQ object at 0x0000026E5C269550>

        Se for acessado o registro LQ de um estágio fora dos limites da
        restrição HQ, isso resultará em um erro:

        >>> dadger.lq(1, 7)
            Traceback (most recent call last):
            ...
            ValueError: Estágio 7 fora dos limites do registro HQ

        Por outro lado, se for acessado o registro LQ em um estágio dentro
        dos limites do registro HQ, porém sem limites próprios definidos,
        será criado um registro idêntico ao do último estágio existente,
        e este será retornado:

        >>> lq2 = dadger.lq(1, 5)
        >>> lq.limites_inferiores == lq2.limites_inferiores
            True

        """

        def cria_registro() -> Optional[LQ]:
            hq = self.hq(codigo=codigo)
            if isinstance(hq, list) or hq is None:
                return None
            ei = hq.estagio_inicial
            ef = hq.estagio_final
            if any([estagio is None, ei is None, ef is None]):
                return None
            ultimo_registro = None
            if ei is not None and estagio <= ef:  # type: ignore
                for e in range(ei, estagio + 1):  # type: ignore
                    registro_estagio = self.__obtem_registros_com_filtros(
                        LQ, codigo=codigo, estagio=e
                    )
                    if registro_estagio is not None:
                        ultimo_registro = registro_estagio
            if isinstance(ultimo_registro, LQ):
                novo_registro = LQ(
                    data=[None] * len(ultimo_registro.data),
                )
                novo_registro.codigo = codigo
                novo_registro.limites_superiores = (
                    ultimo_registro.limites_superiores
                )
                novo_registro.limites_inferiores = (
                    ultimo_registro.limites_inferiores
                )
                novo_registro.estagio = estagio
                self.data.add_after(ultimo_registro, novo_registro)
                return novo_registro
            return None

        if df:
            return self._as_df(LQ)
        else:
            lq = self.__obtem_registros_com_filtros(
                LQ, codigo=codigo, estagio=estagio
            )
            if isinstance(lq, list):
                return lq
            if lq is None:
                lq = cria_registro()
            return lq

    def cq(
        self,
        restricao: Optional[int] = None,
        estagio: Optional[int] = None,
        uhe: Optional[int] = None,
        coeficiente: Optional[float] = None,
        tipo: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[CQ, List[CQ], pd.DataFrame]]:
        """
        Obtém um registro que cadastra os coeficientes das restrições
        de vazão.

        :param restricao: código que especifica o registro
        :type restricao: int | None
        :param estagio: o estágio do coeficiente
        :type estagio: int | None
        :param uhe: o código da UHE para a restrição
        :type uhe: int | None
        :param coeficiente: valor do coeficiente para a usina
            na restrição
        :type coeficiente: float | None
        :param tipo: o mnemônico de tipo da restrição
        :type tipo: str | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se houverem.
        :rtype: :class:`CQ` | list[:class:`CQ`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(CQ)
        else:
            return self.__obtem_registros_com_filtros(
                CQ,
                restricao=restricao,
                uhe=uhe,
                estagio=estagio,
                coeficiente=coeficiente,
                tipo=tipo,
            )

    def he(
        self,
        codigo: Optional[int] = None,
        estagio: Optional[int] = None,
        tipo_limite: Optional[int] = None,
        forma_calculo_produtibilidades: Optional[int] = None,
        tipo_valores_produtibilidades: Optional[int] = None,
        tipo_penalidade: Optional[int] = None,
        penalidade: Optional[float] = None,
        arquivo_produtibilidades: Optional[str] = None,
        df: bool = False,
    ) -> Optional[Union[HE, List[HE], pd.DataFrame]]:
        """
        Obtém um registro que cadastra uma restrição de energia
        armazenada existente no estudo descrito pelo :class:`Dadger`.

        :param codigo: código que especifica o registro
            da restrição de energia armazenada
        :type codigo: int | None
        :param estagio: estágio para o qual vale a
            restrição de energia armazenada
        :type estagio: int | None
        :param tipo_limite: flag para o tipo de limite considerado
        :type tipo_limite: int | None
        :param forma_calculo_produtibilidades: flag para a forma
            do cálculo das probutibilidades
        :type forma_calculo_produtibilidades: int | None
        :param tipo_valores_produtibilidades: flag para o tipo de
            valores das probutibilidades
        :type tipo_valores_produtibilidades: int | None
        :param tipo_penalidade: flag para o tipo de
            penalidade aplicada
        :type tipo_penalidade: int | None
        :param penalidade: valor de penalidade aplicada
        :type penalidade: float | None
        :param arquivo_produtibilidades: nome do arquivo com as
            produtibilidades das usinas
        :type arquivo_produtibilidades: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se houverem.
        :rtype: :class:`HE` | list[:class:`HE`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(HE)
        else:
            return self.__obtem_registros_com_filtros(
                HE,
                codigo=codigo,
                estagio=estagio,
                tipo_limite=tipo_limite,
                forma_calculo_produtibilidades=forma_calculo_produtibilidades,
                tipo_valores_produtibilidades=tipo_valores_produtibilidades,
                tipo_penalidade=tipo_penalidade,
                penalidade=penalidade,
                arquivo_produtibilidades=arquivo_produtibilidades,
            )

    def cm(
        self,
        codigo: Optional[int] = None,
        ree: Optional[int] = None,
        coeficiente: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[CM, List[CM], pd.DataFrame]]:
        """
        Obtém um registro que cadastra os coeficientes das restrições
        de energia armazenada.

        :param codigo: código que especifica o registro
        :type codigo: int | None
        :param ree: REE do coeficiente
        :type ree: int | None
        :param coeficiente: valor do coeficiente para a energia
        :type coeficiente: float | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se houverem.
        :rtype: :class:`CM` | list[:class:`CM`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(CM)
        else:
            return self.__obtem_registros_com_filtros(
                CM,
                codigo=codigo,
                ree=ree,
                coeficiente=coeficiente,
            )

    @property
    def ev(self) -> Optional[EV]:
        """
        Obtém o (único) registro que define a evaporação
        :class:`Dadger`

        :return: Um registro, se existir.
        :rtype: :class:`EV` | None.
        """
        return self.__obtem_registro(EV)

    @property
    def fj(self) -> Optional[FJ]:
        """
        Obtém o (único) registro que define o arquivo `polinjus`
        :class:`Dadger`

        :return: Um registro, se existir.
        :rtype: :class:`FJ` | None.
        """
        return self.__obtem_registro(FJ)

    @property
    def pu(self) -> Optional[PU]:
        """
        Obtém o (único) registro que define se será usado PL único.

        :return: Um registro, se existir.
        :rtype: :class:`PU` | None.
        """
        return self.__obtem_registro(PU)

    @property
    def rc(self) -> Optional[RC]:
        """
        Obtém o (único) registro que insere restrições do tipo
        escada.

        :return: Um registro, se existir.
        :rtype: :class:`RC` | None.
        """
        return self.__obtem_registro(RC)

    def pe(
        self,
        subsistema: Optional[int] = None,
        tipo: Optional[int] = None,
        penalidade: Optional[float] = None,
        df: bool = False,
    ) -> Optional[Union[PE, List[PE], pd.DataFrame]]:
        """
        Obtém um registro que altera penalidades de vertimento,
            intercâmbio e desvios.

        :param subsistema: Índice do subsistema
        :type subsistema: int | None
        :param tipo: tipo de restrição a ser modificada
        :type tipo: int | None
        :param penalidade: valor da penalidade
        :type penalidade: float | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`PE` | list[:class:`PE`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(PE)
        else:
            return self.__obtem_registros_com_filtros(
                PE, subsistema=subsistema, tipo=tipo, penalidade=penalidade
            )

    def ts(
        self,
        tolerancia_primaria: Optional[float] = None,
        tolerancia_secundaria: Optional[float] = None,
        zera_coeficientes: Optional[int] = None,
        tolerancia_teste_otimalidade: Optional[float] = None,
    ) -> Optional[Union[TS, List[TS]]]:
        """
        Obtém um registro que altera as tolerâncias do solver.

        :param tolerancia_primaria: valor da tolerância primária do solver.
        :type tolerancia_primaria: float | None
        :param tolerancia_secundaria: valor da tolerância secundária do solver.
        :type tolerancia_secundaria: float | None
        :param zera_coeficientes: funcionalidade de zerar os coeficientes de
            cortes não ótimos.
        :type zera_coeficientes: int | None
        :param tolerancia_teste_otimalidade: valor da tolerância usada no
            teste de otimalidade.
        :type tolerancia_teste_otimalidade: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`TS` | list[:class:`TS`] | None
        """
        return self.__obtem_registros_com_filtros(
            TS,
            tolerancia_primaria=tolerancia_primaria,
            tolerancia_secundaria=tolerancia_secundaria,
            zera_coeficientes=zera_coeficientes,
            tolerancia_teste_otimalidade=tolerancia_teste_otimalidade,
        )

    def pv(
        self,
        penalidade_variaveis_folga: Optional[float] = None,
        tolerancia_viabilidade_restricoes: Optional[float] = None,
        iteracoes_atualizacao_penalidade: Optional[int] = None,
        fator_multiplicacao_folga: Optional[float] = None,
        valor_inicial_variaveis_folga: Optional[float] = None,
        valor_final_variaveis_folga: Optional[float] = None,
    ) -> Optional[Union[PV, List[PV]]]:
        """
        Obtém um registro que altera as penalidades das variáveis
            de folga.

        :param penalidade_variaveis_folga: valor da nova penalidade das
            variáveis de folga
        :type penalidade_variaveis_folga: float | None
        :param tolerancia_viabilidade_restricoes: valor da tolerância para
            a viabilidade das restrições
        :type tolerancia_viabilidade_restricoes: float | None
        :param iteracoes_atualizacao_penalidade: número de iterações para
            a atualização da penalidade variável
        :type iteracoes_atualizacao_penalidade: int | None
        :param fator_multiplicacao_folga: o fator para multiplicação da
            folga
        :type fator_multiplicacao_folga: float | None
        :param valor_inicial_variaveis_folga: o valor inicial para as
            variáveis de folga
        :type valor_inicial_variaveis_folga: float | None
        :param valor_final_variaveis_folga: o valor final para as
            variáveis de folga
        :type valor_final_variaveis_folga: float | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`PV` | list[:class:`PV`] | None
        """
        return self.__obtem_registros_com_filtros(
            PV,
            penalidade_variaveis_folga=penalidade_variaveis_folga,
            tolerancia_viabilidade_restricoes=tolerancia_viabilidade_restricoes,
            iteracoes_atualizacao_penalidade=iteracoes_atualizacao_penalidade,
            fator_multiplicacao_folga=fator_multiplicacao_folga,
            valor_inicial_variaveis_folga=valor_inicial_variaveis_folga,
            valor_final_variaveis_folga=valor_final_variaveis_folga,
        )

    def cx(
        self,
        codigo_newave: Optional[int] = None,
        codigo_decomp: Optional[int] = None,
        df: bool = False,
    ) -> Optional[Union[CX, List[CX], pd.DataFrame]]:
        """
        Obtém um registro que altera as tolerâncias do solver.

        :param codigo_newave: código da usina no NEWAVE
        :type codigo_newave: int | None
        :param codigo_decomp: código da usina no DECOMP
        :type codigo_decomp: int | None
        :param df: ignorar os filtros e retornar
            todos os dados de registros como um DataFrame
        :type df: bool

        :return: Um ou mais registros, se existirem.
        :rtype: :class:`CX` | list[:class:`CX`] | :class:`pd.DataFrame` | None
        """
        if df:
            return self._as_df(CX)
        else:
            return self.__obtem_registros_com_filtros(
                CX,
                codigo_newave=codigo_newave,
                codigo_decomp=codigo_decomp,
            )

    @property
    def fa(self) -> Optional[FA]:
        """
        Obtém o (único) registro que define o arquivo de índices.

        :return: Um registro, se existir.
        :rtype: :class:`FA` | None.
        """
        return self.__obtem_registro(FA)

    @property
    def vt(self) -> Optional[VT]:
        """
        Obtém o (único) registro que define o arquivo com
            cenários de vento.

        :return: Um registro, se existir.
        :rtype: :class:`VT` | None.
        """
        return self.__obtem_registro(VT)

    @property
    def cs(self) -> Optional[CS]:
        """
        Obtém o (único) registro que habilita a
            consistência de dados.

        :return: Um registro, se existir.
        :rtype: :class:`CS` | None.
        """
        return self.__obtem_registro(CS)

    def pd(
        self, algoritmo: Optional[str] = None
    ) -> Optional[Union[PD, List[PD]]]:
        """
        Obtém um registro que especifica o algoritmo usado para a solução.

        :param algoritmo: Mnemônico do algoritmo
        :type algoritmo: str | None
        :return: Um ou mais registros, se existirem.
        :rtype: :class:`PD` | list[:class:`PD`] | None
        """
        return self.__obtem_registros_com_filtros(PD, algoritmo=algoritmo)
