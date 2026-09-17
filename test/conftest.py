import os
import pytest
from src.carteira_digital import CarteiraDigital
from src.carteira_digital2 import CarteiraDigital2
from src.transferencia import transferir


@pytest.fixture
def carteira_com_log():
    log_path = "carteira.log"

    # Setup
    if os.path.exists(log_path):
        os.remove(log_path)

    carteira = CarteiraDigital2(log_path=log_path)

    try:
        yield carteira
    finally:
        # Teardown
        if os.path.exists(log_path):
            os.remove(log_path)

#ex 5



@pytest.fixture
def duas_carteiras():
    origem = CarteiraDigital(1000)
    destino = CarteiraDigital(0)

    return origem, destino