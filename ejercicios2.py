
print(".:: BIENVENIDO AL SISTEMA DE VOTACION 2024::.")
edad = int(input("Debe ingresar su edad para poder votar: "))
if edad >= 18:
    print("Eres mayor de edad puedes votar.")
else:
    print("Eres menor de edad no puedes votar.")
print("\n")

print(".:: BIENVENIDO AL SISTEMA DE TEMPERATURA::.")
temp = float(input("Ingresa una temperatura en grados Celsius: "))
if temp <= 0:
    print("El agua está en estado sólido.")
elif 0 < temp < 100:
    print("El agua está en estado líquido.")
else:
    print("El agua está en estado gaseoso.")
print("\n")

numero = int(input("Ingresa un número entero: "))
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")



