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

grafo = CrearGrafo([[10, 2], [7, 4], [11, 3], [1, 12], [6, 8], [10, 3], [4, 9], [5, 7], [8, 12], [2, 11], [1, 6], [0, 10], [7, 2], [12, 5]])
min_grafo = CrearGrafo(mst(0, grafo))
print(min_grafo)

lista = [sorted(min_grafo[k]) for k in sorted(min_grafo)]
#[[10], [6], [7, 11], [10, 11], [7, 9], [7, 12], [1, 8], [2, 4, 5], [6, 12], [4], [0, 3], [2, 3], [5, 8]]
print(lista)
