from behave import given, when, then
from recargaya.recargas import calcular_recarga


@given('una recarga de {monto:d} pesos')
def step_impl(context, monto):
    context.monto = monto
    context.premium = False


@given('una recarga de {monto:d} pesos con plan premium')
def step_impl(context, monto):
    context.monto = monto
    context.premium = True


@when('se calcula la recarga')
def step_impl(context):
    context.resultado = calcular_recarga(context.monto, context.premium)


@then('el resultado debe ser rechazada')
def step_impl(context):
    assert context.resultado == "rechazado"


@then('el resultado debe ser {esperado}')
def step_impl(context, esperado):
    assert float(context.resultado) == float(esperado)