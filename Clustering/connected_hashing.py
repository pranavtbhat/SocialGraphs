import math
import networkx as nx
import pylab as plt
import circle
import pygraphviz as pg

def circular_connected_hash(G,colors,radius):
    
    centres = []
    pos = {}
    number_of_colors = len(colors)
    theta = 2*3.14/number_of_colors
    
    for i in range(number_of_colors):
        angle = theta * i
        centres.append( (radius*math.cos(angle), radius*math.sin(angle) )   )
    
    subgraphs = list(nx.connected_component_subgraphs(G))

    for i in range(len(subgraphs)):
        color = colors[hash(i)%number_of_colors]
        bucket = centres[hash(i)%number_of_colors]

        for v in subgraphs[i].nodes(data=False):
            if not 'color' in G.node[v]:
                G.node[v]['color'] = color
                pos[v] = plt.array(circle.circle_coordinates(bucket[0],bucket[1],2))
    
    return pos
    


G = nx.read_dot("/home/pranav/workspace/Netwoks/Data/graphs.dot")

G = G.to_undirected()
colors = ["blue","green","white","red","yellow","orange","pink","grey"]
pos = circular_connected_hash(G, colors, radius=10) 


for v in G.nodes(data=False):
    nx.draw_networkx_nodes(G, pos, [v], 50, node_color = G.node[v]['color'])
nx.draw_networkx_edges(G, pos, edgelist=G.edges(),width = 0.3)

plt.show()