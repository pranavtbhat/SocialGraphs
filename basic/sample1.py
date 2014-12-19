import networkx as nx
import random
import pylab as py
from math import floor

G = nx.complete_graph(20)

for edge in G.edges():
    if floor(edge[0]/5.)!=floor(edge[1]/5.):
        if random.random()<0.95:
            G.remove_edge(edge[0],edge[1])




fixedpos = {1:(1,1), 6:(-1,-1), 11:(-1,1), 16:(1,-1)}

print(fixedpos.keys())
pos = nx.spring_layout(G, fixed = fixedpos.keys(), pos = fixedpos)

nx.draw_networkx(G, pos=pos)

py.show()