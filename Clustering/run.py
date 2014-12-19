import networkx as nx
import pylab as plt
import itertools
import connections
import circle
import random
import math

G = nx.erdos_renyi_graph(100,p=0.01,directed=True)

centres = [(-5,-5),(-5,0),(-5,5),(0,-5),(0,0),(0,5),(5,-5),(5,0),(5,5)]

pos = {}

for i in range(100):
    G.add_node(i)
    pos[i] = plt.array( circle.circle_coordinates(math.floor(random.random()*10),math.floor(random.random()*10), 0.25 ) ) 
#G = connections.fully_connect_with_weights(G, List_of_vertices=[i for i in range(100)], w=1)

nx.draw(G, pos)
plt.show()