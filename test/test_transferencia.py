import pytest

from src.transferencia import transferir
from src.carteira_digital import SaldoInsuficienteError


@pytest.mark.parametrize(
    "valor",
    [100, 250, 1000],
    ids=[
        "transferencia-100",
        "transferencia-250",
        "transferencia-1000",
    ]
)
def test_transferencia_bem_sucedida(duas_carteiras, valor):
    # Arrange
    origem, destino = duas_carteiras

    # Act
    transferir(origem, destino, valor)

    # Assert
    assert origem.saldo == 1000 - valor
    assert destino.saldo == valor



def test_transferencia_sem_saldo_nao_altera(duas_carteiras):
    # Arrange
    origem, destino = duas_carteiras

    saldo_origem_antes = origem.saldo
    saldo_destino_antes = destino.saldo

    # Act
    with pytest.raises(SaldoInsuficienteError):
        transferir(origem, destino, 1500)

    # Assert
    assert origem.saldo == saldo_origem_antes
    assert destino.saldo == saldo_destino_antes