def calcular_recarga(monto, premium=False):
    if not 1000 <= monto <= 50000:
        return "rechazado"

    if monto >= 30000:
        bono = 0.25
    elif monto >= 10000:
        bono = 0.10
    else:
        bono = 0

    return monto * (1 + bono)