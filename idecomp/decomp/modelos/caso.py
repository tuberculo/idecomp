from cfinterface.components.section import Section
from cfinterface.components.line import Line
from cfinterface.components.literalfield import LiteralField
from typing import IO


class NomeCaso(Section):
    """
    Bloco com o nome do caso do arquivo de
    entrada do DECOMP `caso.dat`.
    """

    def __init__(self, previous=None, next=None, data=None) -> None:
        super().__init__(previous, next, data)
        self.__linha = Line([LiteralField(80, 0)])

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, NomeCaso):
            return False
        bloco: NomeCaso = o
        if not all(
            [
                isinstance(self.data, str),
                isinstance(o.data, str),
            ]
        ):
            return False
        else:
            return self.data == bloco.data

    # Override
    def read(self, file: IO):
        self.data = self.__linha.read(file.readline())[0]

    # Override
    def write(self, file: IO):
        file.write(self.__linha.write([self.data]))
