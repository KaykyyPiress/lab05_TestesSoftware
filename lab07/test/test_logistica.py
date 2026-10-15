from src.logistica import gerar_pairwise


def test_quantidade_pairwise():
    casos = gerar_pairwise()

    print(f"\nQuantidade de casos: {len(casos)}")

    assert len(casos) >= 9
    assert len(casos) < 54

from itertools import product
from src.logistica import PARAMS, gerar_pairwise, pares_de


def test_cobertura_pairwise():
    casos_completos = list(product(*PARAMS))
    casos_pairwise = gerar_pairwise()

    pares_completos = pares_de(casos_completos)
    pares_gerados = pares_de(casos_pairwise)

    assert pares_gerados == pares_completos
    assert len(pares_gerados) == 45

def test_pares_descobertos():
    casos_completos = list(product(*PARAMS))
    casos_pairwise = gerar_pairwise()[:3]

    pares_completos = pares_de(casos_completos)
    pares_gerados = pares_de(casos_pairwise)

    pares_descobertos = pares_completos - pares_gerados

    print(f"\nPares não cobertos: {len(pares_descobertos)}")
    print(f"Exemplos: {list(pares_descobertos)[:5]}")

    assert len(pares_descobertos) > 0