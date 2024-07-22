import random

print("JUEGO ADIVINA EL NUMERO")
print("Las reglas son simples, pienso un numero y tu adivinas")

number = random.randint(1,10) #Simula la accion de pienso un numero

isGuessRight = False

while isGuessRight != True:
    guess = int(input("Ingresa un numero: "))
    if int(guess) == number:
        isGuessRight = True
        print("Ganaste")
    else:
        print("Intentalo nuevamente")