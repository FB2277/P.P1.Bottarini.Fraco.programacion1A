#1. Crear una función llamada aplicarAumento que reciba como parámetro el precio de un producto y devuelva el valor del producto con un aumento del 5%. Realizar la llamada desde el main.


def aplicarAumento(precio = input("Ingrese el precio: ")):
    aumento = 5
    Aumento_precio = (precio * 5) / 100
    precio_con_aumento = precio + aumento
    return precio_con_aumento



aplicarAumento(precio = input("Ingrese el precio: "))


