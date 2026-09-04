#mas simple que el de area lol
print("Seleccione en que formato esta la temperatura incial")
print("1. Fahrenheit (°F)")
print("2. Celsius (°C)")
Opcion = input("Escribe acá: ").lower()
tempIni = int(input("Escribe la temperatura acá: "))
factorConversion = 1.8
if (Opcion == "1" or Opcion == "fahrenheit" or Opcion == "°f"):
    temFin = (tempIni * factorConversion) + 32
    print(f"La conversion de {tempIni}°F es: {temFin}°C ")
elif (Opcion == "2" or Opcion == "celsius" or Opcion == "°C"):
    temFin = (tempIni - 32) / factorConversion
    print(f"La conversion de {tempIni}°C es: {temFin}°F ")
else:
    print("Ha ocurrido un error, vuelva a iniciar el programa y seleccione una accion correcta")