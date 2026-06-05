def calcular_recarga(monto, premium=False):
    if not 1000 <= monto <= 50000:
        return "rechazado"

    bono = 0

    if monto >= 30000:
        bono = 0.25
    elif monto >= 10000:
        bono = 0.10

    total = monto * (1 + bono)

    if premium:
        total *= 1.05

    return round(total, 2)