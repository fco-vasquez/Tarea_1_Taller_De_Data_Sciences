import csv
import pandas as pd #Queria que se vieran los datos tal cual como se veian en el csv y solo supe hacerlo con panda
import statistics

def leer_datos(): #Muestra la tabla de datos del archivo seleccionado por el usuario
    archivo = input('Ingrese el nombre del archivo: ')
    df = pd.read_csv(archivo, sep=' ')
    print(df)

def transformar_datos(nombre_archivo): #Transforma el archivo csv en una diccionarios
    datos_diccionario = {'Sexo': [], 'Edad': [], 'Respuesta': []}

    with open(nombre_archivo, newline='') as archivo:
        lector_csv = csv.DictReader(archivo, delimiter=' ')
        for fila in lector_csv:
            datos_diccionario['Sexo'].append(fila['Sexo'])
            datos_diccionario['Edad'].append(int(fila['Edad']))
            datos_diccionario['Respuesta'].append(fila['Respuesta'])

    return datos_diccionario #Me devuelve un diccionario donde las key son Sexo, Edad, Respuesta

def  hombre_estadistica(datos):
    masculino = {'Edad': [], 'Respuesta': []}
    respuestas = []
    for i in range(len(datos['Sexo'])):
        if datos['Sexo'][i] == 'Masculino':
            masculino['Edad'].append(datos['Edad'][i])
            respuesta = datos['Respuesta'][i]
            masculino['Respuesta'].append(respuesta)
            respuestas.append(respuesta)

    #Estadistica Edades
    media_edades = round(statistics.mean(masculino['Edad']), 1)
    moda_edades = round(statistics.mode(masculino['Edad']),1)

    #Estadistica Respuesta
    moda_respuestas = statistics.mode(respuestas)
    return masculino, media_edades, moda_edades, moda_respuestas

def  mujer_estadistica(datos):
    femenino = {'Edad': [], 'Respuesta': []}
    respuestas = []
    for i in range(len(datos['Sexo'])):
        if datos['Sexo'][i] == 'Femenino':
            femenino['Edad'].append(datos['Edad'][i])
            respuesta = datos['Respuesta'][i]
            femenino['Respuesta'].append(respuesta)
            respuestas.append(respuesta)

    #Estadistica Edad
    media_edad = round(statistics.mean(femenino['Edad']),1)
    moda_edad = round(statistics.mode(femenino['Edad']),1)

    #Estadistica Respuesta
    moda_respuesta = statistics.mode(respuestas)
    return femenino, media_edad, moda_edad, moda_respuesta

def estadistica_general(datos):
    edades = datos['Edad']
    respuesta_si = 0
    respuesta_no = 0
    respuesta_talvez = 0

    #Estadistica edades
    media_edades = round(statistics.mean(edades),1)
    moda_edades = round(statistics.mode(edades),1)

    #Contador de respuestas
    for respuesta in datos['Respuesta']:
        if respuesta == 'Si':
            respuesta_si += 1
        elif respuesta == 'No':
            respuesta_no += 1
        elif respuesta == 'Tal Vez':
            respuesta_talvez += 1

    return moda_edades, media_edades, respuesta_no, respuesta_talvez, respuesta_si

def rango_edad(datos):
    rangos = {
        "18-25": {"Masculino": 0, "Femenino": 0, "Edad":[], "Respuesta": [] },
        "26-30": {"Masculino": 0, "Femenino": 0, "Edad":[], "Respuesta": []},
        "31-35": {"Masculino": 0, "Femenino": 0, "Edad":[], "Respuesta": []},
        "36-45": {"Masculino": 0, "Femenino": 0, "Edad":[], "Respuesta": []}
    }

    for i in range(len(datos['Sexo'])):
        edad = datos['Edad'][i]
        sexo = datos['Sexo'][i]
        respuestas = datos['Respuesta'][i]

        if 18 <= edad <= 25:
            rangos["18-25"][sexo] += 1
            rangos["18-25"]["Edad"].append(edad)
            rangos["18-25"]["Respuesta"].append(respuestas)
        elif 26 <= edad <= 30:
            rangos["26-30"][sexo] += 1
            rangos["26-30"]["Edad"].append(edad)
            rangos["26-30"]["Respuesta"].append(respuestas)
        elif  31 <= edad <= 35:
            rangos["31-35"][sexo] += 1
            rangos["31-35"]["Edad"].append(edad)
            rangos["31-35"]["Respuesta"].append(respuestas)
        elif 36 <= edad <= 45:
            rangos["36-45"][sexo] += 1
            rangos["36-45"]["Edad"].append(edad)
            rangos["36-45"]["Respuesta"].append(respuestas)

    for rango, info in rangos.items():
        moda_edad, media_edad, respuesta_no, respuesta_si, respuesta_talvez = estadistica_general(info)
        moda_respuesta = max(('No', respuesta_no), ('Si', respuesta_si), ('Tal Vez', respuesta_talvez), key=lambda x: x[1])[0]
        info['Media_Edad'] = media_edad
        info['Moda_Edad'] = moda_edad
        info['Moda_Respuesta'] = moda_respuesta
    return rangos

def save_results(nombre_archivo, output):
    with open(nombre_archivo, 'a') as file:
        file.write(output)

def inicio(): #Realiza las solicitudes del usuario
    opcion = 0
    output = " "
    nombre_archivo_results = "resultados.txt"

    while opcion != 'F':
        print( "////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print('Elije:\na. Leer Archivo de Datos\nb. Mostrar Estadisticas Generales\nc. Filtrar Datos por sexo y mostrar estadistica\n'
              'd. Filtrar Datos por rango de edad y mostrar estadistica\ne. Guardar resultados en un archivo\nf. Salir')
        print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

        opcion = input().upper()

        if opcion == 'A':
            datos = leer_datos()
            print(datos)

        elif opcion == 'B':
            archivo = transformar_datos(input('Seleccione el archivo que quiere analizar: '))
            media_edades, moda_edades, respuesta_si, respuesta_no, respuesta_talvez = estadistica_general(archivo)

            print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
            print("La media de las edades es: ", media_edades)
            print("La moda de las edades es: ", moda_edades)
            print("Respuestas Si: ", respuesta_si)
            print("Respuestas No: ", respuesta_no)
            print("Respuestas Tal Vez: ", respuesta_talvez)
            print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

            #DESPUES DE VARIOS INTENTOS CON ESTO LOGRO GUARDAR EN UN ARCHIVO TXT LO QUE IMPRIME POR PANTALLA
            output += "///////////////////////////////////////////////////////////////////////////////////////////////////////////////" + "\n"
            output += " La media de las edades es: " + str(media_edades) + "\n"
            output += "La moda de las edades es: " + str(moda_edades)   + "\n"
            output += "Respuestas Si: " + str(respuesta_si) + "\n"
            output += "Respuestas No: " + str(respuesta_no) + "\n"
            output += "Respuesta Tal Vez: " + str(respuesta_talvez) + "\n"
            output += "///////////////////////////////////////////////////////////////////////////////////////////////////////////////" + "\n"

            save_results(nombre_archivo_results, output)
            output = " " #Con esto reinicio la variable para la siguiente parte

        elif opcion == 'C':
            genero = input("Elija si desea la estadistica de: \n A. Masculino\nB. Femenino ").lower()

            if genero == 'a':
                archivo = transformar_datos(input('Seleccione el archivo que quiere analizar: '))
                masculino, media_hombre, moda_hombre, moda_hombre_respuesta = hombre_estadistica(archivo)

                print( "//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                print("Datos Masculinos: ")
                print("Edades: ", masculino['Edad']) #Para verificar que la estadistica esta correcta
                print("Respuestas: ", masculino['Respuesta']) #Para verificar que la estadistica esta correcta
                print("Media Edad: ", media_hombre)
                print("Moda Edad: ", moda_hombre)
                print("Moda Respuesta: ", moda_hombre_respuesta)
                print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

                # DESPUES DE VARIOS INTENTOS CON ESTO LOGRO GUARDAR EN UN ARCHIVO TXT LO QUE IMPRIME POR PANTALLA
                output += "///////////////////////////////////////////////////////////////////////////////////////////////////////////////" + "\n"
                output += "Datos Masculinos: \n"
                output += "Edad: " + str(masculino['Edad']) + "\n"
                output += "Respuestas: " + str(masculino['Respuesta']) + "\n"
                output += "Media: " + str(media_hombre) + "\n"
                output += "Moda: " + str(moda_hombre) + "\n"
                output += "Moda Respuesta: " + str(moda_hombre_respuesta) + "\n"
                output += "///////////////////////////////////////////////////////////////////////////////////////////////////////////////" + "\n"

                save_results(nombre_archivo_results, output)
                output = " "

            elif genero == 'b':
                archivo = transformar_datos(input('Seleccione el archivo que quiere analizar: '))
                femenino, media_mujer, moda_mujer, moda_mujer_respuesta = mujer_estadistica(archivo)

                print(
                    "//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                print("Datos Masculinos: ")
                print("Edades: ", femenino['Edad'])  # Para verificar que la estadistica esta correcta
                print("Respuestas: ", femenino['Respuesta'])  # Para verificar que la estadistica esta correcta
                print("Media Edad: ", media_mujer)
                print("Moda Edad: ", moda_mujer)
                print("Moda Respuesta: ", moda_mujer_respuesta)
                print( "//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

                # DESPUES DE VARIOS INTENTOS CON ESTO LOGRO GUARDAR EN UN ARCHIVO TXT LO QUE IMPRIME POR PANTALLA
                output += "///////////////////////////////////////////////////////////////////////////////////////////////////////////////" + "\n"
                output += "Datos Femeninos: \n"
                output += "Edad: " + str(femenino['Edad']) + "\n"
                output += "Respuestas: " + str(femenino['Respuesta']) + "\n"
                output += "Media: " + str(media_mujer) + "\n"
                output += "Moda: " + str(moda_mujer) + "\n"
                output += "Moda Respuesta: " + str(moda_mujer_respuesta) + "\n"
                output += "///////////////////////////////////////////////////////////////////////////////////////////////////////////////" + "\n"

                save_results(nombre_archivo_results, output)
                output = " "

        elif opcion == 'D':
            archivo = transformar_datos(input('Seleccione el archivo que quiere analizar: '))
            resultados = rango_edad(archivo)

            for rango, info in resultados.items():
                print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                print("Rango Edad: ", rango)
                print("Hombres: ", info["Masculino"])
                print("Mujeres: ", info["Femenino"])
                print("Media de Edad: ", info['Media_Edad'])
                print("Moda de Edad: ", info['Moda_Edad'])
                print("Moda de Respuesta: ", info['Moda_Respuesta'])
                print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

                output += "///////////////////////////////////////////////////////////////////////////////////////////////////////////////" + "\n"
                output += "Rango edad: " + str(rango) +"\n"
                output += "Hombres: " + str(info["Masculino"]) + "\n"
                output += "Mujer: " + str(info["Femenino"]) + "\n"
                output += "Media de Edad: " + str(info['Media_Edad']) + "\n"
                output += "Moda de Edad: " + str(info['Moda_Edad']) + "\n"
                output += "Moda de Respuesta: " + str(info['Moda_Respuesta']) + "\n"
                output += "///////////////////////////////////////////////////////////////////////////////////////////////////////////////" + "\n"

                save_results(nombre_archivo_results, output)
                output = " "

        elif opcion =='E':
            print("Resultados guardados en: ", nombre_archivo_results)

inicio()
