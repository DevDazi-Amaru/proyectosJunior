#Hola
print("Bienvenido, Te dire si tu numero es par o impar")
numero = int(input("Digita acá: "))
if (numero % 2 == 0):
    print(f"El numero {numero} es par")
elif ((numero % 2 == 1) or (numero % 2 == -1)):
    print(f"El numero {numero} es impar")
else:
    print("Ingrese el digito en formato de numero, o ingrese un numero real entero.")