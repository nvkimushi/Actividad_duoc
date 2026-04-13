# ETAPAS:
# Un sistema que consulte la edad, y de acuerdo a ella indique si la persona es mayor de edad o no.
try:
    edad = int(input("Por favor, ingrese su edad:"))
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad.")
except:
    print("...")
# Crear un programa de validación de usuario y contraseña (consultar usuario y contraseña), los únicos dos usuarios conectados son:
# User1: pedro   	Contraseña1: 1234
# User2: angel		Contraseña2: a4s1

usuario1 = "Pedro"
contrasena = "1234"
usuario2 = "Angel"
contrasena2 = "a4s1"

user = input("Ingrese un usuario:\n")
contraseña = input("Ingrese contraseña:\n")
if user == usuario1 and contraseña == contrasena or user == usuario2 and contraseña == contrasena2:
    print("Bienvenido")
else:
    print("Usuario, o contraseña erroneo.")
# Solicitar el ingreso de 3 notas por pantalla, luego calcular el promedio de las 3 notas (cada nota tiene la misma ponderación), finalmente indicar con una salida de pantalla “Aprobado” en el caso de que el promedio sea igual o mayor a 4.0.
cantidad = 3
acumulador_nota = 0
for x in range(3):
    nota = float(input(f"ingrese nota ({x+1})\n"))
    acumulador_nota = acumulador_nota + nota
promedio = acumulador_nota / cantidad
if promedio >= 4:
    print("aprobado")
else:
    print("reprobado")
