import pytest
from allpairspy import AllPairs
from src.frete import frete, esperado


@pytest.mark.parametrize(
    "peso, urgencia, seguro, regiao, resultado",
    [
        ("leve", "normal", False, "sul", 10),
        ("medio", "normal", False, "sudeste", 20),
        ("pesado", "normal", False, "sul", 40),
        ("leve", "normal", False, "norte", 18),
        ("medio", "expressa", False, "norte", 42),
        ("pesado", "expressa", True, "norte", 77),
        ("leve", "expressa", True, "sul", 20),
    ]
)
def test_esperado(peso, urgencia, seguro, regiao, resultado):
    assert frete(peso, urgencia, seguro, regiao) == resultado


@pytest.mark.parametrize(
    "peso, urgencia, seguro, regiao, resultado",
    [
        ("leve", "normal", False, "sul", 10),
        ("medio", "normal", False, "sudeste", 20),
        ("pesado", "normal", False, "sul", 40),
        ("leve", "normal", False, "norte", 18),
        ("medio", "expressa", False, "norte", 42),
        ("pesado", "expressa", True, "norte", 77),
        ("leve", "expressa", True, "sul", 20),
    ]
)
def test_esperado(peso, urgencia, seguro, regiao, resultado):
    assert esperado(peso, urgencia, seguro, regiao) == resultado

#---
PARAMS = [
    ["leve", "medio", "pesado"],
    ["normal", "expressa"],
    [False, True],
    ["sul", "sudeste", "norte"]
]

casos = list(AllPairs(PARAMS))


@pytest.mark.parametrize(
    "peso, urgencia, seguro, regiao",
    casos
)
def test_frete_pairwise(peso, urgencia, seguro, regiao):
    resultado = frete(peso, urgencia, seguro, regiao)
    valor_esperado = esperado(peso, urgencia, seguro, regiao)

    assert resultado == valor_esperado

    #--

from itertools import product

@pytest.mark.parametrize(
    "peso, urgencia, seguro, regiao",
    list(product(*PARAMS))
)
def test_frete_completo(peso, urgencia, seguro, regiao):
    resultado = frete(peso, urgencia, seguro, regiao)
    valor_esperado = esperado(peso, urgencia, seguro, regiao)

    assert resultado == valor_esperado