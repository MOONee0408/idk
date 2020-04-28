#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:01:08 2020

@author: JessicaOrtiz
"""

def create_graph(edgelist):
    graph = {}
    for e1, e2 in edgelist:
        graph.setdefault(e1, []).append(e2)
        graph.setdefault(e2, []).append(e1)
    return graph

# Prim's
def mst(start, graph):
    closed = set()
    edges = []
    q = [(start, start)]
    while q:
        v1, v2 = q.pop()
        if v2 in closed:
            continue
        closed.add(v2)
        edges.append((v1, v2))
        for v in graph[v2]:
            if v in graph:
                q.append((v2, v))
    del edges[0]
    assert len(edges) == len(graph)-1
    return edges

graph = create_graph([[10, 2], [7, 4], [11, 3], [1, 12], [6, 8], [10, 3], [4, 9], [5, 7], [8, 12], [2, 11], [1, 6], [0, 10], [7, 2], [12, 5]])
min_graph = create_graph(mst(0, graph))
print(min_graph)

lista = [sorted(min_graph[k]) for k in sorted(min_graph)]
#[[10], [6], [7, 11], [10, 11], [7, 9], [7, 12], [1, 8], [2, 4, 5], [6, 12], [4], [0, 3], [2, 3], [5, 8]]
print(lista)