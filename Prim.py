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
    assert len(aristas) == len(grafo)-1
    return aristas


intereses = ['ciencias fisicas','mecanico', 'matematicas', 
             'ciencias biologicas', 'ecologia', 'servicio social', 
             'politico', 'ciencias sociales', 'administrativo', 'organizacional', 
             'artistico', 'expresion musical', 'expresion oral','expresion escrita']
carreras = [['arquitectura'], ['fisica'], ['ingenieria'], ['matematicas'], 
            ['biologia'], ['medicina'], ['psicologia'],['quimica'],
            ['administracion'],['comunicacion'],['derecho'], ['trabajo social'],
            ['diseño grafico'],['historia'],['literatura'],['musica']]


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

intereses = ['ciencias fisicas','mecanico', 'matematicas', 
             'ciencias biologicas', 'ecologia', 'servicio social', 
             'politico', 'ciencias sociales', 'administrativo', 'organizacional', 
             'artistico', 'expresion musical', 'expresion oral','expresion escrita']
carreras = [['arquitectura'], ['fisica'], ['ingenieria'], ['matematicas'], 
            ['biologia'], ['medicina'], ['psicologia'],['quimica'],
            ['administracion'],['comunicacion'],['derecho'], ['trabajo social'],
            ['diseño grafico'],['historia'],['literatura'],['musica']]


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

#Alum={'ciencias fisicas': 55,'mecanico': 54, 'matematicas':66, 
#        'ciencias biologicas':47, 'ecologia': 42, 'servicio social': 36, 
#        'politico':42 , 'ciencias sociales': 50, 'administrativo': 58, 'organizacional': 42, 
#        'artistico': 48, 'expresion musical': 66, 'expresion oral': 49,'expresion escrita': 72}


#PARA INGRESAR DATOS DEL ALUMNO:
def AgregarAlumno():
    Alum = {}
    for interes in intereses:
        n = int(input("Ingrese el puntaje para " + interes + ":\t" ))
        while (n < 0 or n > 100):
            n = int(input("¡Ingrese un número válido!\t"))
        Alum[interes] = n
    return Alum
   
def imprimirDict(Dict):
    for clave in Dict:
        print("Clave:\t " + str(clave) + "\tValor:\t" + str(Dict[clave]))


Alum = AgregarAlumno()
#copia = Alum.copy()
Alumno = Alum.copy()
for clave in Alum:
    if Alum[clave] < 45:
        Alumno.pop(clave,None)

n = len(Alumno) #print(n)

lista_Dict = []
for clave in Alumno:   
    lista_Dict.append([Alumno[clave], clave])
lista_Dict.sort(reverse=True)
#print("lista:"+ str(lista_Dict))

areaI = []
areaII = []
areaIII = []
areaIV = []
definitiva = []
for clave in TArea:
    guardado = []
    for y in TArea[clave]:
        for i in range(len(lista_Dict)):
            if y == lista_Dict[i][1]:
                guardado.append(y)
    m = len(guardado)
    if clave in CAreaI:
        definitiva.append([m,1, clave])
        areaI.append([m, clave])
    elif clave in CAreaII:
        definitiva.append([m,2, clave])
        areaII.append([m, clave])
    elif clave in CAreaIII:
        definitiva.append([m,3, clave])
        areaIII.append([m, clave])
    elif clave in CAreaIV:
        definitiva.append([m,4, clave])
        areaIV.append([m, clave])

print("\n\n")    
definitiva.sort(reverse=True)
for i in definitiva: 
    print(i)

maxpts = definitiva[0][0]
print("Numero maximo de puntos:\t", maxpts)

lista_grafo = []
pts = maxpts
paso= False
areaS = []
anteriores = []
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
            for k in range(len(anteriores)): 
                if anteriores[k][1] == definitiva[i][1] and anteriores[k][2] != definitiva[i][2]:
                    lista_grafo.append([anteriores[k][2],definitiva[i][2]])
                    
        elif pts < maxpts and definitiva[i][1] not in areaS and paso ==False:
            lista_grafo.append(['indef',definitiva[i][2]])
            c = c + 1
            anteriores.append(definitiva[i])
            for k in range(len(anteriores)): 
                if anteriores[k][1] == definitiva[i][1] and anteriores[k][2] != definitiva[i][2]:
                    lista_grafo.append([anteriores[k][2],definitiva[i][2]])
            if definitiva[i+1][0] != pts:
                paso = True  
        else:
            anteriores.append(definitiva[i])
            for k in range(len(anteriores)): 
                
                if anteriores[k][1] == definitiva[i][1] and anteriores[k][2] != definitiva[i][2]:
                    lista_grafo.append([anteriores[k][2],definitiva[i][2]])
    else:
        pts = pts -1
        anteriores.append(definitiva[i])
        for k in range(len(anteriores)): 
            if anteriores[k][1] == definitiva[i][1] and anteriores[k][2] != definitiva[i][2]:
                lista_grafo.append([anteriores[k][2],definitiva[i][2]])

print("\n\nAsociaciones")
for i in lista_grafo: 
    print("\n",i)     
graph = CrearGrafo(lista_grafo)
print("\n\ngrafo normal:\n")
imprimirDict(graph)
minimo_grafo = CrearGrafo(mst('indef', graph))
print("grafo minimo:\n")
imprimirDict(minimo_grafo)
