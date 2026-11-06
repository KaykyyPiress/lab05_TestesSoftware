
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

    assert carrinho.total == 1000


def test_cupom_vinte_no_limite():
    carrinho = Carrinho()
    carrinho.adicionar(30000)
    carrinho.aplicar_cupom("VINTE")

    assert carrinho.total == 24000


def test_cupom_vinte_abaixo_do_minimo():
    carrinho = Carrinho()
    carrinho.adicionar(29999)
    carrinho.aplicar_cupom("VINTE")

    assert carrinho.total == 29999


def test_quantidade_zero():
    carrinho = Carrinho()

    with pytest.raises(ValueError):
        carrinho.adicionar(1000, 0)


def test_quantidade_fracionaria():
    carrinho = Carrinho()

    with pytest.raises(ValueError):
        carrinho.adicionar(1000, 1.5)


def test_quantidade_booleana():
    carrinho = Carrinho()

    with pytest.raises(ValueError):
        carrinho.adicionar(1000, True)


def test_segundo_cupom_substitui_primeiro():
    carrinho = Carrinho()
    carrinho.adicionar(30000)

    carrinho.aplicar_cupom("VINTE")
    assert carrinho.total == 24000

    carrinho.aplicar_cupom("DEZ")
    assert carrinho.total == 27000


def test_quantidade_negativa():
    carrinho = Carrinho()

    with pytest.raises(ValueError):
        carrinho.adicionar(1000, -1)


def test_cupom_dez_no_limite():
    carrinho = Carrinho()
    carrinho.adicionar(10000)
    carrinho.aplicar_cupom("DEZ")

    assert carrinho.total == 9000


def test_cupom_ativa_quando_subtotal_atinge_minimo():
    carrinho = Carrinho()
    carrinho.adicionar(9000)
    carrinho.aplicar_cupom("DEZ")

    assert carrinho.total == 9000

    carrinho.adicionar(1000)

    assert carrinho.total == 9000
