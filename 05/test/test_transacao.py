from src.transacao import classificar_transacao
import pytest

@pytest.mark.parametrize(
    "valor, resultado_esperado",
    [
        (50, "pequena"),
        (99, "pequena"),
        (100, "media"),
        (500, "media"),
        (999, "media"),
        (1000, "grande"),
        (1500, "grande"),
    ],
    ids=[
        "valor-pequeno",
        "limite-antes-de-100",
        "limite-100-media",
        "valor-medio",
        "limite-antes-de-1000",
        "limite-1000-grande",
        "valor-grande",
    ]
)
def test_classificar_transacao(valor, resultado_esperado):
    assert classificar_transacao(valor) == resultado_esperado