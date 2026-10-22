
import pytest
from src.forca import forca

@pytest.mark.parametrize("senha, esperado", [
    ("abc", "fraca"),
    ("abcdefgh", "media"),
    ("abcdefghi", "media"),
    ("abcdefg1", "media"),
    ("abcdefg!", "media"),
    ("abcdef!!", "forte"),
])
def test_forca(senha, esperado):
    assert forca(senha) == esperado



@pytest.mark.parametrize("senha, esperado", [
    ("abcdefgh", "media"),      # 8 voltas (mínimo)
    ("abcdefghi", "media"),     # 9 voltas
    ("abcdefghij", "media"),    # 10 voltas
    ("a" * 100, "media"),       # 100 voltas
])
def test_laco(senha, esperado):
    assert forca(senha) == esperado
