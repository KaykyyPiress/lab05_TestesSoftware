
from src.fila import Fila


def test_fila_inicia_vazia():
    fila = Fila()
    assert fila.aguardando == 0


def test_emitir_primeira_senha_normal():
    fila = Fila()
    assert fila.emitir("normal") == "N1"


def test_emitir_primeira_senha_prioritaria():
    fila = Fila()
    assert fila.emitir("prioritaria") == "P1"
