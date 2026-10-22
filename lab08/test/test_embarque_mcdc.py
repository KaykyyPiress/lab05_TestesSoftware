
import pytest
from src.embarque import pode_embarcar
from src.mcdc import regra

conjuntos = [
    ("M1", ["0101", "1001", "1100", "1101", "1110"]),
    ("M2", ["0101", "1010", "1100", "1101", "1110"]),
    ("M3", ["0110", "1001", "1100", "1101", "1110"]),
    ("M4", ["0110", "1010", "1100", "1101", "1110"]),
]

@pytest.mark.parametrize("nome,casos", conjuntos)
def test_mcdc(nome, casos):
    for caso in casos:
        entrada = tuple(c == "1" for c in caso)

        assert pode_embarcar(*entrada) == regra(*entrada), (
            f"{nome} falhou na entrada {caso}"
        )
