def calcular_recarga(monto, premium=False):
    if not 1000 <= monto <= 50000:
        return "rechazado"

    return monto