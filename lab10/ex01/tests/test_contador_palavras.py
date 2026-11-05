from src.contador_palavras import contar_palavras


def test_texto_vazio():
    assert contar_palavras("") == {}