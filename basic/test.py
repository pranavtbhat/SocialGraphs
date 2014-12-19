import networkx as nx
import pylab as plt

G = nx.read_dot("/home/pranav/workspace/Netwoks/Data/graph.dot")
G = G.to_undirected()
target_node = 13

pos=nx.random_layout(G)

for h in nx.connected_component_subgraphs(G):
    if target_node in h:
        nx.draw(h,pos,node_size=20,node_color='red')
    else:
        nx.draw(h,pos,node_color='white')

