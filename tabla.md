En este apartado realizaré el diseño una tabla de casos de prueba aplicando partición de equivalencia y valores límite para el campo de monto.

Ya que fue solicitada junto con el Gherkin.

# Tabla de casos de prueba - RecargaYa

## Reglas de negocio del monto
Es necesario tenerlas en cuenta para que se facilite ralizar la tabla de partción de equivalencias.
- Mínimo permitido: $1.000
- Máximo permitido: $50.000
- < 1000 o > 50000 → Rechazado
- ≥ 10.000 → 10% bonificación
- ≥ 30.000 → 25% bonificación
- Premium → +5% adicional sobre bonificación

-

## Partición de equivalencia

| Clase                | Rango de entrada | Resultado esperado |
|----------------------|------------------|-------------------|
| Inválido bajo        | monto < 1000 | rechazado |
| Válido pero sin bono | 1000 – 9999 | monto sin cambios |
| Bono de 10%          | 10000 – 29999 | +10% |
| Bono de 25%          | 30000 – 50000 | +25% |
| Inválido alto        | > 50000 | rechazado |



## Valores límite 

| Caso | Entrada | Resultado esperado | Justificación |
|---|--------|-------------------|--------------|
| 1 | 999 | rechazado | límite inferior inválido |
| 2 | 1000 | válido | mínimo permitido |
| 3 | 9999 | 9999 | antes del bono 10% |
| 4 | 10000 | 11000 | inicio bono 10% |
| 5 | 29999 | 32999.9 | antes bono 25% |
| 6 | 30000 | 37500 | inicio bono 25% |
| 7 | 50000 | 62500 | máximo válido |
| 8 | 50001 | rechazado | límite superior inválido |