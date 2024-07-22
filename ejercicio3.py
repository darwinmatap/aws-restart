#VERIFICA QUE LOS DOS NUMEROS INGRESADOS SEAN POSITIVOS
num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingrese otro numero: "))
if num1 and num2 >= 1:
    print("Los numeros ingresados son positivos.")
else:
    print("Ingreso un numero negativo.") 
print("\n")

#VERIFICA QUE SE CUMPLAN LAS DOS CONDICIONES DEBE TENER MAS DE 18 AÑOS Y TENER CEDULA VIGENTE
edad_votante = 10
cedula_vigente = True
if edad_votante >= 18 and cedula_vigente == True:
    print("Bienvenido puede votar")
else:
    print(f"Tienes {edad_votante} años, no cumples con todos los requisitos para votar")
print("\n")

#VERIFICA SI LA PERSONA TIENE CEDULA O ES MAYOR DE EDAD PARA ENTRAR A UN BAR
edad = 19
cedula = False
if edad >= 18 or cedula == True:
    print("Bienvenido puede entrar al Bar")
else:
    print(f"No cumples las condiciones internas para entrar al Bar")