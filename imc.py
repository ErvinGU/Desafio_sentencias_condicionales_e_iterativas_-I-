""" "Calcular imc y clasificar según OMS" """

""" Ingresar peso y altura """
peso_en_Kg = float(input("Ingrese su peso en Kg : "))
altura_en_cm = float(input("Ingrese su altura en cm : "))

"""Calculo del IMC"""
altura = altura_en_cm / 100 #se divide en 100 para pasa a metros
imc = peso_en_Kg / (altura **2)

print(f"Su IMC es : {imc:.2f}")

"""Clasificación OMS """

if imc < 18.5:
    clasificacion = "Bajo Peso"
elif 18.5 <= imc < 25:
    clasificacion = "Peso Adecuado"
elif 25 <= imc < 30:
    clasificacion = "Sobrepeso"
elif 30 <= imc < 35:
    clasificacion = "Obesidad Grado I"
elif 35 <= imc < 40:
    clasificacion = "Obesidad Grado II"
else:
    clasificacion = "Obesidad Grado III"

print(f"Su clasificación según la OMS es : {clasificacion}")
