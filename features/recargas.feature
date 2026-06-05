Feature: Cálculo de recargas en RecargaYa

  Como sistema de recargas
  Quiero aplicar reglas de bonificación según monto
  Para calcular beneficios correctamente

  Scenario: recarga inválida menor al mínimo
    Given una recarga de 500 pesos
    When se calcula la recarga
    Then el resultado debe ser rechazada

  Scenario: recarga en rango válido sin bonificación
    Given una recarga de 5000 pesos
    When se calcula la recarga
    Then el resultado debe ser 5000

  Scenario: bonificación del 10 por ciento
    Given una recarga de 10000 pesos
    When se calcula la recarga
    Then el resultado debe ser 11000

  Scenario: bonificación del 25 por ciento
    Given una recarga de 30000 pesos
    When se calcula la recarga
    Then el resultado debe ser 37500

  Scenario Outline: recargas con plan premium
    Given una recarga de <monto> pesos con plan premium
    When se calcula la recarga
    Then el resultado debe ser <resultado>

    Examples:
      | monto | resultado |
      | 10000 | 11550    |
      | 30000 | 39375    |