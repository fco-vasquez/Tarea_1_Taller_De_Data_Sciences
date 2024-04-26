import random
import csv
#-------------- Funciones ---------------------------------
def generar_genero():
    genero = random.choice(["Femenino","Masculino"])
    return genero

def generar_respuesta():
    respuesta = random.choice(["Si","No","Tal Vez"])
    return respuesta

def generar_edad():
    edad = random.randint(18,45)
    return edad

#----------------------------------------------------------
datos = []

for i in range(50):
    genero = generar_genero()
    edad = generar_edad()
    respuesta = generar_respuesta()
    datos.append((genero, edad, respuesta))

with open("encuesta.csv","w", newline ="") as archivo:
    csv_w = csv.writer(archivo, delimiter =" ")
    csv_w.writerow(["Sexo","Edad","Respuesta"])
    csv_w.writerows(datos)

