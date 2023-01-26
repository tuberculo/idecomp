# Imports de módulos externos
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField


from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV


class TabelaOperUsie(TabelaCSV):
    """
    Bloco com a operação por estação elevatória.
    """

    BEGIN_PATTERN = "-----;------;------;-----;--------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=6),
            IntegerField(size=6),
            IntegerField(size=5),
            FloatField(size=8, decimal_digits=2),
            IntegerField(size=5),
            LiteralField(size=14),
            IntegerField(size=4),
            LiteralField(size=15),
            IntegerField(size=7),
            IntegerField(size=7),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "periodo",
        "no",
        "cenario",
        "patamar",
        "duracao",
        "indiceUsina",
        "nomeUsina",
        "indiceSubmercado",
        "nomeSubmercado",
        "indiceUsinaJusante",
        "indiceUsinaMontante",
        "vazaoBombeadaM3S",
        "energiaBombeamentoMW",
        "vazaoBombeadaMinimaM3S",
        "vazaoBombeadaMaximaM3S",
    ]
    END_PATTERN = ""
