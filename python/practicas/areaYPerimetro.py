def menuFiguras():
    print("Escoge una figura:")
    print("1. Cuadrado")
    print("2. triangulo (isoseles(IGNORAR))")

def menuOperacion():
    print("Escribe la operacion a realizar")
    print("Area / perimetro")

def escogerFigura():
    figura = str(input("Escribe aquí: "))
    match(figura):
        case "1" | "cuadrado":
            return "cuadrado"
        case "2" | "triangulo":
            return "triangulo"

def calcularOperacion(figura, opcion, lado1 = 0, lado2 = 0, lado3 = 0):
    match(figura):
        case "cuadrado":
            match(opcion.lower()):
                case "area":
                    area = lado1**2
                    return area
                case "perimetro":
                    perimetro = lado1 * 4
                    return perimetro
        case "triangulo":
            match (opcion.lower()):
                case "area":
                    #hipotenusa lado 1 como base
                    cateto1 = lado1 / 2
                    altura = (lado2**2 - cateto1**2)**0.5
                    area = (lado1 * altura)/2
                    return area
                case "perimetro":
                    perimetro = lado1 + lado2 + lado3
                    return perimetro

def almacenarDatos(figura):
    match (figura):
        case "cuadrado":
            print("ingrese la base del cuadrado:")
            base = int(input())
            return base, 0, 0
        case "triangulo":
            print("ingrese los tres lados del triangulo")
            lado1 = int(input("Lado 1: "))
            lado2 = int(input("Lado 2: "))
            lado3 = int(input("Lado 3: "))
            return lado1, lado2, lado3


print("Bienvenido al sistema")
menuFiguras()
figura = escogerFigura() 
dato1, dato2, dato3 = almacenarDatos(figura)
menuOperacion()
operacion = str(input("Escibe aquí: "))
resultado = calcularOperacion(figura, operacion, dato1, dato2, dato3)
print(f"El resultado de efectuar el {operacion} del {figura} es igual a: {resultado}")
