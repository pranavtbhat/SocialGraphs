import networkx as nx
import pylab as plt

colors = ["red","green","blue","white","black","orange"]

G = nx.erdos_renyi_graph(100, 0.01,1)
G = G.to_undirected()

nx.emp
H = nx.Graph()

for v in G.nodes_iter():
    H.add_node(v,color=colors[hash(v)%6])

for e in G.edges():
    if H.node[e[0]]['color'] == H.node[e[1]]['color']:
        H.add_edge(e[0],e[1],weight=1)
    else:
        H.add_edge(e[0],e[1],weight=100)
        
pos = nx.spring_layout(G, dim, k, pos, fixed, iterations, weight, scale)

for n in G.nodes():
    lst =[]
    lst.append(n)       
    nx.draw_networkx_nodes(H, pos, lst, node_size=200, node_color=H.node[n]['color'])
    
nx.draw_networkx_edges(G, pos, G.edges())
plt.show()
    

