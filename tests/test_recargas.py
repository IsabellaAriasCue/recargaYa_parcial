from recargaya.recargas import calcular_recarga


def test_recarga_invalida_menor_1000():
    assert calcular_recarga(500) == "rechazado"

def test_bono_10_por_ciento():
    assert calcular_recarga(10000) == 11000

