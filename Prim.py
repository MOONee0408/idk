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


intereses = ['Cfis','Mec', 'Mat', 
             'Cbiosa', 'Eco', 'Ssoc', 
             'Pol', 'Csoc', 'Adm', 'Org', 
             'ArtVis', 'ExpMus', 'ExpOral','ExpEsc']
carreras = [['arquitectura'], ['fisica'], ['ingenieria'], ['matematicas'], 
            ['biologia'], ['medicina'], ['psicologia'],['quimica'],
            ['administracion'],['comunicacion'],['derecho'], ['trabajo social'],
            ['diseño grafico'],['historia'],['literatura'],['musica']]


TArea={'arq': ['Mec', 'Mat', 'Org', 'ArtVis'], 
          'fis': ['Cfis','Mec', 'Mat'], 
          'ing':['Cfis','Mec', 'Mat'], 
          'mat':['Cfis', 'Mat', 'Org'],
          'bio': {'Cfis', 'Cbiosa', 'Eco', 'Org'}, 
           'med': {'Cfis', 'Mat', 'Cbiosa', 'Ssoc'}, 
           'psi':{'Cbiosa','Ssoc', 'Csoc', 'Org', 'ExpOral'}, 
           'quim':{'Mec', 'Mat', 'Cbiosa', 'Eco'},
           'adm': {'Mat', 'Adm', 'Org', }, 
            'com': {'Ssoc', 'Pol', 'Csoc', 'ExpOral','ExpEsc'},
            'der':{'Ssoc', 'Pol', 'Csoc',  'Org', 'ExpOral','ExpEsc'}, 
            'trabsoc':{'Eco', 'Ssoc', 'Csoc',  'Org', 'ExpOral','ExpEsc'},
            'disgraf': {'Pol', 'Csoc', 'ArtVis', 'ExpEsc'}, 
           'hist': {'Ssoc', 'Pol', 'Csoc', 'ExpOral','ExpEsc'}, 
           'lit':{'Ssoc', 'ExpOral','ExpEsc'}, 
           'mus':{'ExpMus', 'ExpOral','ExpEsc'}}


CAreaI = {'arq': ['Mec', 'Mat', 'Org', 'ArtVis'], 
          'fis': ['Cfis','Mec', 'Mat'], 
          'ing':['Cfis','Mec', 'Mat'], 
          'mat':['Cfis', 'Mat', 'Org']}
CAreaII = {'bio': {'Cfis', 'Cbiosa', 'Eco', 'Org'}, 
           'med': {'Cfis', 'Mat', 'Cbiosa', 'Ssoc'}, 
           'psi':{'Cbiosa','Ssoc', 'Csoc', 'Org', 'ExpOral'}, 
           'quim':{'Mec', 'Mat', 'Cbiosa', 'Eco'}}
CAreaIII = {'adm': {'Mat', 'Adm', 'Org', }, 
            'com': {'Ssoc', 'Pol', 'Csoc', 'ExpOral','ExpEsc'},
            'der':{'Ssoc', 'Pol', 'Csoc',  'Org', 'ExpOral','ExpEsc'}, 
            'trabsoc':{'Eco', 'Ssoc', 'Csoc',  'Org', 'ExpOral','ExpEsc'}}
CAreaIV = {'disgraf': {'Pol', 'Csoc', 'ArtVis', 'ExpEsc'}, 
           'hist': {'Ssoc', 'Pol', 'Csoc', 'ExpOral','ExpEsc'}, 
           'lit':{'Ssoc', 'ExpOral','ExpEsc'}, 
           'mus':{'ExpMus', 'ExpOral','ExpEsc'}}

#Alum={'Cfis': 55,'Mec': 54, 'Mat':66, 
#        'Cbiosa':47, 'Eco': 42, 'Ssoc': 68, 
#        'Pol':42 , 'Csoc': 50, 'Adm': 58, 'Org': 42, 
#        'ArtVis': 48, 'ExpMus': 66, 'ExpOral': 49,'ExpEsc': 72}


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
