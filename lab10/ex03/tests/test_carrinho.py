
import pytest
from src.carrinho import Carrinho


def test_carrinho_vazio():
    carrinho = Carrinho()
    assert carrinho.total == 0


def test_adicionar_produto():
    carrinho = Carrinho()
    carrinho.adicionar(2500)
    assert carrinho.total == 2500


def test_adicionar_quantidade():
    carrinho = Carrinho()
    carrinho.adicionar(2500, 2)
    assert carrinho.total == 5000


def test_preco_zero():
    carrinho = Carrinho()

    with pytest.raises(ValueError):
        carrinho.adicionar(0)


def test_cupom_dez():
    carrinho = Carrinho()
    carrinho.adicionar(5000)
    carrinho.aplicar_cupom("DEZ")

    assert carrinho.total == 5000


def test_cupom_invalido():
    carrinho = Carrinho()

    with pytest.raises(ValueError):
        carrinho.aplicar_cupom("XYZ")


def test_adicionar_apos_cupom():
    carrinho = Carrinho()
    carrinho.aplicar_cupom("DEZ")
    carrinho.adicionar(1000)

    assert carrinho.total == 900

def test_cupom_dez():
    carrinho = Carrinho()
    carrinho.adicionar(5000)
    carrinho.aplicar_cupom("DEZ")

    assert carrinho.total == 5000


def test_adicionar_apos_cupom():
    carrinho = Carrinho()
    carrinho.aplicar_cupom("DEZ")
    carrinho.adicionar(1000)

    assert carrinho.total == 1000
