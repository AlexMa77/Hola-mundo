def calcularPromedio (nota1,nota2,nota3):
    sum=nota1+nota2+nota3 
    prom=sum / 3
    return prom

def consultarMulta (tipoMulta):
    multas = {1: 10, 2: 15, 3: 20, 4: 30}
    return multas.get(tipoMulta, -1)

def calcularValorHora (salario):
    horas= salario / 160
    return horas

def calcularSubtotal (precioProducto, cantidad, porcentajeDescuento):
    subtotalSinDescuento = precioProducto * cantidad 
    descuento =subtotalSinDescuento  * porcentajeDescuento / 100
    total = subtotalSinDescuento - descuento
    return total

def calcularValorDescuento (precio,porcentajeDescuento) :
    valorDescuento = (precio * porcentajeDescuento) / 100
    return valorDescuento