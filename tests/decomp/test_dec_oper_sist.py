from idecomp.decomp.dec_oper_sist import DecOperSist

from tests.mocks.mock_open import mock_open
from unittest.mock import MagicMock, patch

from tests.mocks.arquivos.dec_oper_sist import MockDecOperSist


def test_atributos_encontrados_dec_oper_sist():
    m: MagicMock = mock_open(read_data="".join(MockDecOperSist))
    with patch("builtins.open", m):
        rel = DecOperSist.le_arquivo("")
        assert rel.versao == "31.14"
        assert rel.tabela.at[0, "periodo"] == 1
        assert rel.tabela.at[0, "no"] == 1
        assert rel.tabela.at[0, "cenario"] == 1
        assert rel.tabela.at[0, "patamar"] == 1
        assert rel.tabela.at[0, "duracao"] == 40.00
        assert rel.tabela.at[0, "indice_submercado"] == 1
        assert rel.tabela.at[0, "nome_submercado"] == "SE"
        assert rel.tabela.at[0, "demanda_MW"] == 48383.0
        assert rel.tabela.at[0, "geracao_pequenas_usinas_MW"] == 3374.0
        assert rel.tabela.at[0, "geracao_termica_MW"] == 6509.80
        assert rel.tabela.at[0, "geracao_termica_antecipada_MW"] == 548.00
        assert rel.tabela.at[0, "geracao_hidroeletrica_MW"] == 33567.62
        assert rel.tabela.at[0, "geracao_eolica_MW"] == 0.00
        assert rel.tabela.at[0, "energia_bombeamento_MW"] == 13.58
        assert rel.tabela.at[0, "energia_importada_MW"] == 0.00
        assert rel.tabela.at[0, "energia_exportada_MW"] == 0.00
        assert rel.tabela.at[0, "intercambio_liquido_MW"] == 7576.16
        assert rel.tabela.at[0, "itaipu_50MW"] == 1900.00
        assert rel.tabela.at[0, "itaipu_60MW"] == 5009.89
        assert rel.tabela.at[0, "deficit_MW"] == 0.00
        assert rel.tabela.at[0, "ena_MWmes"] == 12608.1
        assert rel.tabela.at[0, "earm_inicial_MWmes"] == 47877.48
        assert rel.tabela.at[0, "earm_inicial_percentual"] == 23.43
        assert rel.tabela.at[0, "earm_final_MWmes"] == 52743.55
        assert rel.tabela.at[0, "earm_final_percentual"] == 25.81
        assert rel.tabela.at[0, "cmo"] == 956.18


def test_eq_dec_oper_sist():
    m: MagicMock = mock_open(read_data="".join(MockDecOperSist))
    with patch("builtins.open", m):
        rel1 = DecOperSist.le_arquivo("")
        rel2 = DecOperSist.le_arquivo("")
        assert rel1 == rel2


def test_neq_dec_oper_sist():
    m: MagicMock = mock_open(read_data="".join(MockDecOperSist))
    with patch("builtins.open", m):
        rel1 = DecOperSist.le_arquivo("")
        rel2 = DecOperSist.le_arquivo("")
        rel1.tabela.iloc[0, 0] = -1
        assert rel1 != rel2
