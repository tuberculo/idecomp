# Imports de módulos externos
from cfinterface.components.line import Line
from cfinterface.components.integerfield import IntegerField
from cfinterface.components.literalfield import LiteralField
from cfinterface.components.floatfield import FloatField


from idecomp.decomp.modelos.blocos.tabelacsv import TabelaCSV


class TabelaCortesEvap(TabelaCSV):
    """
    Bloco com as informações dos cortes da evaporação linear.
    """

    BEGIN_PATTERN = "-----;-----;--------------;"
    LINE_MODEL = Line(
        [
            IntegerField(size=5),
            IntegerField(size=5),
            LiteralField(size=14),
            IntegerField(size=4),
            IntegerField(size=5),
            FloatField(size=22, decimal_digits=10),
            FloatField(size=22, decimal_digits=10),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=11, decimal_digits=2),
            FloatField(size=17, decimal_digits=10),
            FloatField(size=12, decimal_digits=14),
        ],
        delimiter=";",
    )
    COLUMN_NAMES = [
        "periodo",
        "indice_usina",
        "nome_usina",
        "submercado",
        "ree",
        "derivada_cota_area",
        "derivada_volume_cota",
        "volume_referencia_hm3",
        "evaporacao_referencia_hm3",
        "coeficiente_volume",
        "rhs_volume",
    ]
    END_PATTERN = ""
