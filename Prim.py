#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:01:08 2020

@author: JessicaOrtiz
"""


def CrearGrafo(lista):
    grafo = {}
    for e1, e2 in lista:
        grafo.setdefault(e1, []).append(e2)
        grafo.setdefault(e2, []).append(e1)
    return grafo

# Prim's
def mst(inicio, grafo):
    closed = set()
    aristas = []
    q = [(inicio, inicio)]
    while q:
        v1, v2 = q.pop()
        if v2 in closed:
            continue
        closed.add(v2)
        aristas.append((v1, v2))
        for v in grafo[v2]:
            if v in grafo:
                q.append((v2, v))
    del aristas[0]
#    assert len(aristas) == len(grafo)-1
    return aristas

intereses = ['ciencias fisicas','mecanico', 'matematicas', 
             'ciencias biologicas', 'ecologia', 'servicio social', 
             'politico', 'ciencias sociales', 'administrativo', 'organizacional', 
             'artistico', 'expresion musical', 'expresion oral','expresion escrita']

TArea={'arquitectura': ['mecanico', 'matematicas', 'organizacional', 'artistico'], 
       'fisica': ['ciencias fisicas','mecanico', 'matematicas'], 
       'ingenieria':['ciencias fisicas','mecanico', 'matematicas'], 
       'matematicas':['ciencias fisicas', 'matematicas', 'organizacional'],
       'biologia': ['ciencias fisicas', 'ciencias biologicas', 'ecologia', 'organizacional'], 
       'medicina': ['ciencias fisicas', 'matematicas', 'ciencias biologicas', 'servicio social'], 
       'psicologia':['ciencias biologicas','servicio social', 'ciencias sociales', 'organizacional', 'expresion oral'], 
       'quimica':['mecanico', 'matematicas', 'ciencias biologicas', 'ecologia'],
       'administracion': ['matematicas', 'administrativo', 'organizacional' ], 
       'comunicacion': ['servicio social', 'politico', 'ciencias sociales', 'expresion oral','expresion escrita'],
       'derecho':['servicio social', 'politico', 'ciencias sociales',  'organizacional' 'expresion oral','expresion escrita'], 
       'trabajo social':['ecologia', 'servicio social', 'ciencias sociales',  'organizacional' 'expresion oral','expresion escrita'],
       'diseño grafico': ['politico', 'ciencias sociales', 'artistico', 'expresion escrita'], 
       'historia': ['servicio social', 'politico', 'ciencias sociales', 'expresion oral','expresion escrita'], 
       'literatura':['servicio social', 'expresion oral','expresion escrita'], 
       'musica':['expresion musical', 'expresion oral','expresion escrita']}


CAreaI = {'arquitectura': ['mecanico', 'matematicas', 'organizacional', 'artistico'], 
          'fisica': ['ciencias fisicas','mecanico', 'matematicas'], 
          'ingenieria':['ciencias fisicas','mecanico', 'matematicas'], 
          'matematicas':['ciencias fisicas', 'matematicas', 'organizacional']}
CAreaII = {'biologia': ['ciencias fisicas', 'ciencias biologicas', 'ecologia', 'organizacional'], 
           'medicina': ['ciencias fisicas', 'matematicas', 'ciencias biologicas', 'servicio social'], 
           'psicologia':['ciencias biologicas','servicio social', 'ciencias sociales', 'organizacional', 'expresion oral'], 
           'quimica':['mecanico', 'matematicas', 'ciencias biologicas', 'ecologia']}
CAreaIII = {'administracion': ['matematicas', 'administrativo', 'organizacional' ], 
            'comunicacion': ['servicio social', 'politico', 'ciencias sociales', 'expresion oral','expresion escrita'],
            'derecho':['servicio social', 'politico', 'ciencias sociales',  'organizacional' 'expresion oral','expresion escrita'], 
            'trabajo social':['ecologia', 'servicio social', 'ciencias sociales',  'organizacional' 'expresion oral','expresion escrita']}
CAreaIV = {'diseño grafico': ['politico', 'ciencias sociales', 'artistico', 'expresion escrita'], 
           'historia': ['servicio social', 'politico', 'ciencias sociales', 'expresion oral','expresion escrita'], 
           'literatura':['servicio social', 'expresion oral','expresion escrita'], 
           'musica':['expresion musical', 'expresion oral','expresion escrita']}

Alum={'ciencias fisicas': 55,'mecanico': 54, 'matematicas':66, 
        'ciencias biologicas':47, 'ecologia': 42, 'servicio social': 36, 
        'politico':42 , 'ciencias sociales': 50, 'administrativo': 58, 'organizacional': 42, 
        'artistico': 48, 'expresion musical': 66, 'expresion oral': 49,'expresion escrita': 72}


#PARA INGRESAR DATOS DEL ALUMNO:
def AgregarAlumno():
    Alum = {}
    for interes in intereses:
        n = int(input("Ingrese el puntaje para " + interes + ":\t" ))
        while (n < 0 or n > 100):
            n = int(input("¡Ingrese un número válido!\t"))
        Alum[interes] = n
    return Alum
   
#NOS IMPRIME EL DICCIONARIO CON CADA CLAVE Y SUS VALORES RESPECTIVOS    
def imprimirDict(Dict):
    for clave in Dict:
        print("Clave:\t " + str(clave) + "\tValor:\t" + str(Dict[clave]))

#VERIFICA SI HAY MÁS ELEMENTOS CON LOS CUALES RELACIONAR
#Ejemplo: Hay 3 aptitudes que son de area 1 así que las combina... mates con mecan, mates con arq, mecan con arq (?)
def idk(anteriores, lista_grafo, definitiva, i):
    for k in range(len(anteriores)): 
        if anteriores[k][1] == definitiva[i][1] and anteriores[k][2] != definitiva[i][2]:
            lista_grafo.append([anteriores[k][2],definitiva[i][2]])

def main():
#    Alum = AgregarAlumno()
    Alumno = Alum.copy()
    #Se eliminan todos los elementos que sean menores a 45 por ser puntajes bajos
    for clave in Alum:
        if Alum[clave] < 45:
            Alumno.pop(clave,None)
    
    #En lista_Dict solo se almacenan lista con cada uno de los elementos que quedaron, es decir todas las aptitudes con puntaje mayor a 45
    lista_Dict = [] #Lista de listas
    for clave in Alumno:   
        lista_Dict.append([Alumno[clave], clave]) #[puntaje, "aptitud"] EJEMPLO: [[72, 'expresion escrita']]
    
    lista_Dict.sort(reverse=True) #el reverse es para que se ordene de Mayor a menor puntaje

    definitiva = [] #LISTA DE LISTAS guardará todos los datos necesarios para poder crear las relaciones
    #ESTO QUIERE DECIR  numero de coincidencias (cuantas aptitudes coinciden con cada carrera),
    #el area al que corresponden y la aptitud
    for clave in TArea:
        cont = 0 #Contador auxiliar que nos dice cuantas aptitudes son iguales a las de la carrera (COINCIDENCIAS)
        for y in TArea[clave]:
            for i in range(len(lista_Dict)):
                if y == lista_Dict[i][1]: #Verifica que sean iguales cada uno de las aptitudes del alumno con las requeridas en la carrera
                    cont = cont + 1 
                    break
        if clave in CAreaI:                           #                                  [coincidencias,    Area,   interes]
            definitiva.append([cont,1, clave])#Lo que se comento en la linea 119 EJEMPLO [3,                  4 ,  'musica']
        elif clave in CAreaII:
            definitiva.append([cont,2, clave])
        elif clave in CAreaIII:
            definitiva.append([cont,3, clave])
        elif clave in CAreaIV:
            definitiva.append([cont,4, clave])
    
    print("\n\n")    
    definitiva.sort(reverse=True) #REVERSE, lo mismo que linea 116, es para ordenar de mayor a menor
#    for i in definitiva: 
#        print(i)
    maxpts = definitiva[0][0] # Numero maximo de puntos(COINCIDENCIAS)
    #print("Numero maximo de puntos:\t", maxpts)
    lista_grafo = [] #GUARDA LAS RELACIONES, estas serán necesarias para la 
    pts = maxpts #esta variable guarda los puntos, es auxiliar para poder iterar 
    paso= False #variable auxiliar que nos ayuda a identificar si un elemento de la misma area (ya guardada) tiene menos puntos
    #Revisar Linea 163 y 168 
    areaS = [] #Nos ayuda para poder ver si falta algun elemento de alguna area, revisar linea 163
    anteriores = [] #Guarda los elementos que ya se crearon sus relaciones.
    for i in range(len(definitiva)):
        if definitiva[i][0] == pts: 
            
            if len(anteriores) == 0:
                lista_grafo.append(['indef',definitiva[i][2]])
                anteriores.append(definitiva[i])
                c = 1
                areaS.append(definitiva[i][1])
            elif definitiva[i] not in anteriores and pts ==maxpts:
                lista_grafo.append(['indef',definitiva[i][2]])
                anteriores.append(definitiva[i])
                c = c +1
                areaS.append(definitiva[i][1])
                idk(anteriores, lista_grafo, definitiva, i)
            elif pts < maxpts and definitiva[i][1] not in areaS and paso ==False:
                lista_grafo.append(['indef',definitiva[i][2]])
                c = c + 1
                anteriores.append(definitiva[i])
                idk(anteriores, lista_grafo, definitiva, i)
                if definitiva[i+1][0] != pts:
                    paso = True  
            else:
                anteriores.append(definitiva[i])
                idk(anteriores, lista_grafo, definitiva, i)
        else:
            pts = pts -1
            anteriores.append(definitiva[i])
            idk(anteriores, lista_grafo, definitiva, i)
    #
    #print("\n\nAsociaciones")
    for i in lista_grafo: 
        print("\n",i)     
    graph = CrearGrafo(lista_grafo)
#    print("\n\ngrafo normal:\n")
#    imprimirDict(graph)
    minimo_grafo = CrearGrafo(mst('indef', graph))
    print("grafo minimo:\n")
    imprimirDict(minimo_grafo)


print("\t\t<--BIENVENIDO-->")

print("<<Universidad Nacional Autonoma de México>>")
print("Facultad de ingeniería")
print("Ingenieria en Computación")
print("Estructuras Discretas")
print("Proyecto final")
print("Integrantes:") #Datos del programa
bandera=False
while bandera==False:
    print("\n Menu:\n[1]Ejecutar \n[2]Salir\n")
    try:
        opcion=int(input("Selecciona una opcion:\n"))
        bandera=True
    except:
        print("¡Opcion no valida! ")
    if (opcion == 1):
        main()
    elif (opcion == 2):
        break
    bandera=False

#
#print("\n\n")       
#grafo = CrearGrafo([[10, 2], [7, 4], [11, 3], [1, 12], [6, 8], [10, 3], [4, 9], [5, 7], [8, 12], [2, 11], [1, 6], [0, 10], [7, 2], [12, 5]])
#imprimirDict(grafo)
#min_grafo = CrearGrafo(mst(0, grafo))
#imprimirDict(min_grafo)
##print(min_grafo)
#
#lista = [sorted(min_grafo[k]) for k in sorted(min_grafo)]
##[[10], [6], [7, 11], [10, 11], [7, 9], [7, 12], [1, 8], [2, 4, 5], [6, 12], [4], [0, 3], [2, 3], [5, 8]]
#print(lista)


        
