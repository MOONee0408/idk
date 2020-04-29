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


grafo = CrearGrafo([[10, 2], [7, 4], [11, 3], [1, 12], [6, 8], [10, 3], [4, 9], [5, 7], [8, 12], [2, 11], [1, 6], [0, 10], [7, 2], [12, 5]])
min_grafo = CrearGrafo(mst(0, grafo))
print(min_grafo)

lista = [sorted(min_grafo[k]) for k in sorted(min_grafo)]
print(lista)
