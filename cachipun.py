import random as r

#Opciones
opciones = ["piedra", "papel", "tijeras"]

#Usuario elige opción
while True:
    usuario_elige = input("Elija su opción: piedra, papel o tijeras : ").lower()
    if usuario_elige in opciones:
        break
    else:
        print("Opcion invalida, elige entre piedra, papel o tijeras")

#Computadora Elige
computadora_elige = r.choice(opciones)

#Elegir ganador
if usuario_elige == computadora_elige:
    print("Empate!!")
elif (usuario_elige == "piedra" and computadora_elige == "tijera") or \
     (usuario_elige == "papel" and computadora_elige == "piedra") or \
     (usuario_elige == "tijera" and computadora_elige == "papel"):
    print(f"GANASTE!! la computadora eligió : {computadora_elige}")

else:
    print(f"PERDISTE!! la computadora eligió : {computadora_elige}")


