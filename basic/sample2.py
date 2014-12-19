import networkx as nx
import pylab as plt

G=nx.Graph()

for i in range(10):
    G.add_node(i, attr_dict={'num':i})

print(G.node.values())