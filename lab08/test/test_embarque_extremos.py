
import pytest
from src.embarque import pode_embarcar
from src.mcdc import regra

@pytest.mark.parametrize("entrada", [
    (True, True, True, True),       # Todos V
    (False, False, False, False),   # Todos F
])
def test_embarque(entrada):
    assert pode_embarcar(*entrada) == regra(*entrada)
