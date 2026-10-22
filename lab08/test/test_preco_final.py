
import pytest
from src.preco_final import preco_final_correto

@pytest.mark.parametrize("preco,vip,esperado", [
    (60, True, 50),
    (200, False, 200),
    (40, False, 50),
    (100, True, 80),
])
def test_preco_final(preco, vip, esperado):
    assert preco_final_correto(preco, vip) == esperado
