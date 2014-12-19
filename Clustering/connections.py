import networkx as nx
import pylab as plt
import itertools as itools
import math 
import random
import Clustering
 
def fully_connect_with_weights(G,List_of_vertices,w):
    if G.is_directed():
        edges = itools.permutations(List_of_vertices,2)
    else:
        edges = itools.combinations(List_of_vertices,2)
    lst = []
    
    for e in edges:
        G.add_edge(e[0],e[1],weight=w)
    return G

