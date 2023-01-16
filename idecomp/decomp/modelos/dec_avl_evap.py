# Imports de módulos externos
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField


from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV


class TabelaAvlEvap(TabelaCSV):
    """
    Bloco com as informações de avaliação da representação linear
    para a evaporação.
    """

    BEGIN_PATTERN = "-----;-----;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=5),
            LiteralField(size=14),
            IntegerField(size=4),
            IntegerField(size=5),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=2),
            FloatField(size=10, decimal_digits=3),
            FloatField(size=10, decimal_digits=2),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "periodo",
        "codigoUsina",
        "nomeUsina",
        "submercado",
        "ree",
        "volumeArmazenadoHm3",
        "evaporacaoCalculadaHm3",
        "evaporacaoModeloHm3",
        "desvioAbsolutoHm3",
        "desvioPercentual",
    ]
    END_PATTERN = ""
