
import pytest
from fila import Fila


def test_fila_inicia_vazia():
    fila = Fila()
    assert fila.aguardando == 0


def test_emitir_primeira_senha_normal():
    fila = Fila()
    assert fila.emitir("normal") == "N1"


def test_emitir_primeira_senha_prioritaria():
    fila = Fila()
    assert fila.emitir("prioritaria") == "P1"


def test_numeracao_independente():
    fila = Fila()

    assert fila.emitir("normal") == "N1"
    assert fila.emitir("prioritaria") == "P1"
    assert fila.emitir("normal") == "N2"
    assert fila.emitir("prioritaria") == "P2"


def test_tipo_invalido():
    fila = Fila()

    with pytest.raises(ValueError):
        fila.emitir("vip")

    assert fila.aguardando == 0


def test_chamar_fila_vazia():
    fila = Fila()

    with pytest.raises(IndexError):
        fila.chamar()


def test_chamar_senha_normal():
    fila = Fila()

    assert fila.emitir("normal") == "N1"
    assert fila.aguardando == 1

    assert fila.chamar() == "N1"
    assert fila.aguardando == 0


def test_prioritaria_passa_na_frente():
    fila = Fila()

    fila.emitir("normal")
    fila.emitir("prioritaria")

    assert fila.chamar() == "P1"
    assert fila.chamar() == "N1"
    assert fila.aguardando == 0


def test_ordem_de_chegada_por_tipo():
    fila = Fila()

    fila.emitir("normal")
    fila.emitir("normal")
    fila.emitir("prioritaria")
    fila.emitir("prioritaria")

    assert fila.chamar() == "P1"
    assert fila.chamar() == "P2"
    assert fila.chamar() == "N1"
    assert fila.chamar() == "N2"


def test_duas_prioritarias_seguidas():
    fila = Fila()

    fila.emitir("normal")
    fila.emitir("prioritaria")
    fila.emitir("prioritaria")
    fila.emitir("prioritaria")

    assert fila.chamar() == "P1"
    assert fila.chamar() == "P2"
    assert fila.chamar() == "N1"
    assert fila.chamar() == "P3"


def test_zerar_contagem_apos_normal():
    fila = Fila()

    fila.emitir("normal")
    fila.emitir("normal")

    for _ in range(4):
        fila.emitir("prioritaria")

    assert fila.chamar() == "P1"
    assert fila.chamar() == "P2"
    assert fila.chamar() == "N1"

    assert fila.chamar() == "P3"
    assert fila.chamar() == "P4"
    assert fila.chamar() == "N2"


def test_mais_de_duas_prioritarias_sem_normal():
    fila = Fila()

    fila.emitir("prioritaria")
    fila.emitir("prioritaria")
    fila.emitir("prioritaria")
    fila.emitir("prioritaria")

    assert fila.chamar() == "P1"
    assert fila.chamar() == "P2"
    assert fila.chamar() == "P3"
    assert fila.chamar() == "P4"
    assert fila.aguardando == 0
