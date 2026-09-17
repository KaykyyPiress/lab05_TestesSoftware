import pytest
from src.carteira_digital import CarteiraDigital, SaldoInsuficienteError


def test_saldo_inicial_padrao():
    # Arrange
    carteira = CarteiraDigital()

    # Act
    saldo = carteira.saldo

    # Assert
    assert saldo == 0


def test_saldo_inicial_informado():
    # Arrange
    carteira = CarteiraDigital(100)

    # Act
    saldo = carteira.saldo

    # Assert
    assert saldo == 100


def test_depositar_valor():
    # Arrange
    carteira = CarteiraDigital(100)

    # Act
    carteira.depositar(50)

    # Assert
    assert carteira.saldo == 150


def test_sacar_valor_dentro_do_saldo():
    # Arrange
    carteira = CarteiraDigital(100)

    # Act
    carteira.sacar(40)

    # Assert
    assert carteira.saldo == 60

#Ex2
def test_saque_com_saldo_insuficiente():
    # Arrange
    carteira = CarteiraDigital(100)

    # Act
    with pytest.raises(SaldoInsuficienteError) as erro:
        carteira.sacar(150)

    # Assert
    assert str(erro.value) == "saldo insuficiente"

def test_saldo_nao_muda_apos_saque_sem_saldo():
    # Arrange
    carteira = CarteiraDigital(100)

    # Act
    try:
        carteira.sacar(150)
    except SaldoInsuficienteError:
        pass

    # Assert
    assert carteira.saldo == 100

#Ex 3
