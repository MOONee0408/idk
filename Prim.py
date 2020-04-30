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

#función de Prim
def mst(inicio, grafo):
    visitado = set()
    aristas = []
    q = [(inicio, inicio)]
    while q:
        v1, v2 = q.pop()
        if v2 in visitado:
            continue
        visitado.add(v2)
        aristas.append((v1, v2))
        for v in grafo[v2]:
            if v in grafo:
                q.append((v2, v))
    del aristas[0]
    assert len(aristas) == len(grafo)-1
    return aristas

    #PARA INGRESAR DATOS DEL ALUMNO:
def AgregarAlumno():
    Alum = {}
    for interes in intereses:
        print(interes)
        n = int(input("Ingrese el puntaje para " + interes + ":\t" ))
        while (n < 0 or n > 100):
            n = int(input("¡Ingrese un número válido!\t"))
        Alum[interes] = n
    return Alum


def imprimirDict(Dict):
    for clave in Dict:
        print("Clave:\t " + str(clave) + "\tValor:\t" + str(Dict[clave]))

#Solo he colocado la información para poder ver como realizarlo, estoy pensando que sea con diccionarios
#sea más facil de trabajar, o la otra es trabajar con lista de listas. 
#igual quedaría después de ver mas la estructura del programa
intereses = ['Cfis','Mec', 'Mat', 
             'Cbiosa', 'Eco', 'Ssoc', 
             'Pol', 'Csoc', 'Adm', 'Org', 
             'ArttVis', 'ExpMus', 'ExpOral','ExpEsc']
carreras = [['arquitectura'], ['fisica'], ['ingenieria'], ['matematicas'], 
            ['biologia'], ['medicina'], ['psicologia'],['quimica'],
            ['administracion'],['comunicacion'],['derecho'], ['trabajo social'],
            ['diseño grafico'],['historia'],['literatura'],['musica']]

CAreaI = {'arq': {'Mec', 'Mat', 'Org', 'ArttVis'}, 
          'fis': {'Cfis','Mec', 'Mat'}, 
          'ing':{'Cfis','Mec', 'Mat'}, 
          'mat':{'Cfis', 'Mat', 'Org'}}
CAreaII = {'bio': {'Cfis', 'Cbiosa', 'Eco', 'Org'}, 
           'med': {'Cfis', 'Mat', 'Cbiosa', 'Ssoc'}, 
           'psi':{'Cbiosa','Ssoc', 'Csoc', 'Org', 'ExpOral'}, 
           'quim':{'Mec', 'Mat', 'Cbiosa', 'Eco'}}
CAreaIII = {'adm': {'Mat', 'Adm', 'Org', }, 
            'com': {'Ssoc', 'Pol', 'Csoc', 'ExpOral','ExpEsc'},
            'der':{'Ssoc', 'Pol', 'Csoc',  'Org', 'ExpOral','ExpEsc'}, 
            'trabsoc':{'Eco', 'Ssoc', 'Csoc',  'Org', 'ExpOral','ExpEsc'}}
CAreaIV = {'disgraf': {'Pol', 'Csoc', 'ArttVis', 'ExpEsc'}, 
           'hist': {'Ssoc', 'Pol', 'Csoc', 'ExpOral','ExpEsc'}, 
           'lit':{'Ssoc', 'ExpOral','ExpEsc'}, 
           'mus':{'ExpMus', 'ExpOral','ExpEsc'}}



#Alum={'Cfis': 55,'Mec': 54, 'Mat':66, 'Cbiosa':47, 'Eco': 42, 'Ssoc': 36, 'Pol':42 , 'Csoc': 50, 'Adm': 58, 'Org': 42, 'ArtVis': 62, 'ExpMus': 66, 'ExpOral': 49,'ExpEsc': 72}

Alum = AgregarAlumno()
Alumno = Alum.copy()

#Elimina todos los valores menores a 45
for clave in Alum:
    if Alum[clave] < 45:
        Alumno.pop(clave,None)

#También podemos hacer que se agregen todos los valores mayores a 45
#for clave in Alum:
    #if Alum[clave] > 45:
        #Alumno[clave] = Alum[clave]
#imprimirDict(Alumno)
        

n = len(Alumno) #Tamaño de nuestro diccionario

lista_Dict = [] #Esta lista guardará todos los pares de nuestro diccionario.
for clave in Alumno:   
    lista_Dict.append([Alumno[clave], clave]) #Agrega primero valor y luego clave, ej. [[72, 'Ssoc'],...]

lista_Dict.sort(reverse=True) #Nos organiza la lista de manera descendente, ej. [[72, 'Ssoc],...,[47, 'Adm']]
#print("lista:"+ str(lista_Dict))


definitiva = [] #En esta lista se guardan las listas que se muestra en la linea 113
#Este ciclo nos busca todas las listas para formar nuestro grafo
for clave in CAreaI:
    guardado = []
    print("\nCarrera:\t")
    print(clave)
    print("Intereses:")
    print(CAreaI[clave])
    for y in CAreaI[clave]:
        for i in range(len(lista_Dict)):
            if y == lista_Dict[i][1]:
                print("Sí esta " + str(y) + " en: " +  str(clave))
                guardado.append(y)
    print(guardado)
    m = len(guardado)
    print(m)
    definitiva.append([m,clave,1]) #Se guardará el numero de coincidencias, carrera y Area
    
    
definitiva.sort(reverse=True)
for i in definitiva:
    print(i)


#ESTA PARTE ES APARTE, NOS PRUEBA QUE FUNCIONA LA FUNCIÓN PRIM
grafo = CrearGrafo([[10, 2], [7, 4], [11, 3], [1, 12], [6, 8], [10, 3], [4, 9], [5, 7], [8, 12], [2, 11], [1, 6], [0, 10], [7, 2], [12, 5]])
min_grafo = CrearGrafo(mst(0, grafo))
imprimirDict(min_grafo) 
#print(min_grafo)

#Crea una lista con los datos.
lista = [sorted(min_grafo[k]) for k in sorted(min_grafo)]
print(lista)
