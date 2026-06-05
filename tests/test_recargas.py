from recargaya.recargas import calcular_recarga


def test_recarga_invalida_menor_1000():
    assert calcular_recarga(500) == "rechazado"