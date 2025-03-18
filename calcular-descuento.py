def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento dado un porcentaje y el total de la compra.
    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento a aplicar (por defecto 10%).
    :return: Monto del descuento.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Llamadas a la función
monto1 = 100  # Ejemplo de monto total de compra
monto2 = 200  # Otro ejemplo con diferente monto

# Primera llamada con el descuento por defecto
monto_descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - monto_descuento1

# Segunda llamada con un descuento específico del 15%
monto_descuento2 = calcular_descuento(monto2, 15)
monto_final2 = monto2 - monto_descuento2

# Mostrar los resultados
print(f"Compra 1: Monto total = ${monto1}, Descuento = ${monto_descuento1}, Monto final = ${monto_final1}")
print(f"Compra 2: Monto total = ${monto2}, Descuento = ${monto_descuento2}, Monto final = ${monto_final2}")
