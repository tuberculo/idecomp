# Imports do próprio módulo
from idecomp._utils.leitura import Leitura
from .modelos.relato import DadosGeraisRelato
from .modelos.relato import CMORelato
from .modelos.relato import GeracaoTermicaSubsistemaRelato
from .modelos.relato import EnergiaArmazenadaSubsistemaRelato
from .modelos.relato import Relato
# Imports de módulos externos
import os
import numpy as np  # type: ignore
from traceback import print_exc
from typing import IO, List


class LeituraRelato(Leitura):
    """
    Realiza a leitura do arquivo relato.rvx
    existente em um diretório de saídas do DECOMP.

    Esta classe contém o conjunto de utilidades para ler
    e interpretar os campos de um arquivo relato.rvx, construindo
    um objeto `Relato` cujas informações são as mesmas do relato.rvx.

    Este objeto existe para retirar do modelo de dados a complexidade
    de iterar pelas linhas do arquivo, recortar colunas, converter
    tipos de dados, dentre outras tarefas necessárias para a leitura.

    Uma vez realizada a leitura do arquivo, as informações são guardadas
    internamente no atributo `Relato`.

    **Exemplos**

    >>> diretorio = "~/documentos/.../deck"
    >>> leitor = LeituraRelato(diretorio)
    >>> leitor.le_arquivo()
    # Ops, esqueci de pegar o objeto
    >>> relato = leitor.relato

    """
    str_inicio_dados = "Relatorio  dos  Dados  Gerais"
    str_inicio_cmo = "CUSTO MARGINAL DE OPERACAO  ($/MWh)"
    str_inicio_gt_subsis = "GERACAO TERMICA NOS SUSBSISTEMAS (MWmed)"
    str_inicio_earm_subsis = "ENERGIA ARMAZENADA NOS SUBSISTEMAS (%"
    str_fim_relato = "FIM DO PROCESSAMENTO"

    def __init__(self,
                 diretorio: str) -> None:
        super().__init__()
        self.diretorio = diretorio
        # Relato default, depois é substituído
        gt = GeracaoTermicaSubsistemaRelato([],
                                            np.ndarray([]))
        earm = EnergiaArmazenadaSubsistemaRelato([],
                                                 np.ndarray([]))
        self.relato = Relato(DadosGeraisRelato(0),
                             CMORelato([],
                                       np.ndarray([])),
                             gt,
                             earm)

    def le_arquivo(self,
                   relato_rev: str = "") -> Relato:
        """
        Faz a leitura do arquivo `relato.rvx`.
        """
        try:
            # Se não foi fornecido um nome de relato,
            # procura um relato no diretório
            if relato_rev == "":
                arquivos = os.listdir(self.diretorio)
                for a in arquivos:
                    if "relato.rv" in a:
                        relato_rev = a
                        break
                if len(relato_rev) == 0:
                    raise Exception("Não foi encontrado relato")
            # Lê o arquivo
            caminho = os.path.join(self.diretorio, relato_rev)
            with open(caminho, "r") as arq:
                self.relato = self._le_relato(arq)
                return self.relato
        except Exception:
            print_exc()
            return self.relato

    def _le_relato(self, arq: IO) -> Relato:
        """
        Faz a leitura do arquivo pmo.dat.
        """
        achou_dados_gerais = False
        achou_cmo = False
        achou_gt_subsis = False
        achou_earm_subsis = False
        linha = ""
        dados_gerais = DadosGeraisRelato(0)
        cmo = CMORelato([], np.array([]))
        gt_subsis = GeracaoTermicaSubsistemaRelato([], np.array([]))
        earm_subsis = EnergiaArmazenadaSubsistemaRelato([],
                                                        np.ndarray([]))
        while True:
            # Decide se lê uma linha nova ou usa a última lida
            linha = self._le_linha_com_backup(arq)
            if len(linha) == 0 or self._fim_arquivo(linha):
                self.relato = Relato(dados_gerais,
                                     cmo,
                                     gt_subsis,
                                     earm_subsis)
                break
            # Condição para iniciar uma leitura de dados
            if not achou_dados_gerais:
                achou = LeituraRelato.str_inicio_dados in linha
                achou_dados_gerais = achou
            if not achou_cmo:
                achou = LeituraRelato.str_inicio_cmo in linha
                achou_cmo = achou
            if not achou_gt_subsis:
                achou = LeituraRelato.str_inicio_gt_subsis in linha
                achou_gt_subsis = achou
            if not achou_earm_subsis:
                achou = LeituraRelato.str_inicio_earm_subsis in linha
                achou_earm_subsis = achou
            # Quando achar, le cada parte adequadamente
            if achou_dados_gerais:
                dados_gerais = self._le_dados_gerais(arq)
                achou_dados_gerais = False
            if achou_cmo:
                cmo = self._le_cmo(arq)
                achou_cmo = False
            if achou_gt_subsis:
                gt_subsis = self._le_gt_subsistema(arq)
                achou_gt_subsis = False
            if achou_earm_subsis:
                earm_subsis = self._le_earm_subsistema(arq)
                achou_earm_subsis = False

        return self.relato

    def _le_dados_gerais(self,
                         arq: IO
                         ) -> DadosGeraisRelato:
        """
        """
        # Salta uma linha
        self._le_linha_com_backup(arq)
        # Descobre o número de semanas
        dados = DadosGeraisRelato(0)
        while True:
            # Confere se a leitura não acabou
            linha = self._le_linha_com_backup(arq)
            if len(linha) < 3:
                return dados
            # Senão, lê mais uma linha
            if "Numero de semanas do mes inicial" in linha:
                dados.numero_semanas_1_mes = int(linha[-3:])

    def _le_cmo(self,
                arq: IO
                ) -> CMORelato:
        """
        Lê a tabela de CMO existente no arquivo relato do DECOMP.
        """
        # Salta uma linha
        self._le_linha_com_backup(arq)
        # Descobre o número de semanas
        linha = self._le_linha_com_backup(arq)
        sems = [s for s in linha.split(" ") if (len(s) > 0
                                                and "Sem" in s)]
        n_semanas = len(sems)
        subsistemas: List[str] = []
        tabela = np.zeros((80, n_semanas))
        # Salta outra linha
        self._le_linha_com_backup(arq)
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = self._le_linha_com_backup(arq)
            if "X------X" in linha:
                return CMORelato(subsistemas, tabela[:i, :])
            # Senão, lê mais uma linha
            # Subsistema
            ssis = linha[4:10].strip()
            subsistemas.append(ssis)
            # Semanas
            ci = 11
            nc = 10
            for j in range(n_semanas):
                cf = ci + nc
                tabela[i, j] = float(linha[ci:cf])
                ci = cf + 1
            i += 1

    def _le_gt_subsistema(self,
                          arq: IO
                          ) -> GeracaoTermicaSubsistemaRelato:
        """
        Lê a tabela de GT por subsistema
        existente no arquivo relato do DECOMP.
        """
        # Salta uma linha
        self._le_linha_com_backup(arq)
        # Descobre o número de semanas
        linha = self._le_linha_com_backup(arq)
        sems = [s for s in linha.split(" ") if (len(s) > 0
                                                and "Sem" in s)]
        n_semanas = len(sems)
        subsistemas: List[str] = []
        tabela = np.zeros((20, n_semanas))
        # Salta outra linha
        self._le_linha_com_backup(arq)
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = self._le_linha_com_backup(arq)
            if "X------X" in linha:
                return GeracaoTermicaSubsistemaRelato(subsistemas,
                                                      tabela[:i, :])
            # Senão, lê mais uma linha
            # Subsistema
            ssis = linha[4:10].strip()
            subsistemas.append(ssis)
            # Semanas
            ci = 11
            nc = 10
            for j in range(n_semanas):
                cf = ci + nc
                tabela[i, j] = float(linha[ci:cf])
                ci = cf + 1
            i += 1

    def _le_earm_subsistema(self,
                            arq: IO
                            ) -> EnergiaArmazenadaSubsistemaRelato:
        """
        Lê a tabela de EARM por subsistema
        existente no arquivo relato do DECOMP.
        """
        # Salta uma linha
        self._le_linha_com_backup(arq)
        # Descobre o número de semanas
        linha = self._le_linha_com_backup(arq)
        sems = [s for s in linha.split(" ") if (len(s) > 0
                                                and "Sem" in s)]
        n_semanas = len(sems)
        subsistemas: List[str] = []
        tabela = np.zeros((20, n_semanas + 1))
        # Salta outra linha
        self._le_linha_com_backup(arq)
        i = 0
        while True:
            # Confere se a leitura não acabou
            linha = self._le_linha_com_backup(arq)
            if "-------" in linha:
                return EnergiaArmazenadaSubsistemaRelato(subsistemas,
                                                         tabela[:i, :])
            # Senão, lê mais uma linha
            # Subsistema
            ssis = linha[4:16].strip()
            subsistemas.append(ssis)
            # Inicial e semanas
            ci = 23
            nc = 6
            for j in range(n_semanas + 1):
                cf = ci + nc
                tabela[i, j] = float(linha[ci:cf])
                ci = cf + 1
            i += 1

    def _fim_arquivo(self, linha: str) -> bool:
        return LeituraRelato.str_fim_relato in linha