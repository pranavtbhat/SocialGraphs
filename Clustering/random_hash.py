import math
import networkx as nx
import pylab as plt
import circle

def circular_random_hash(G,colors,radius):
    
    centres = []
    pos = {}
    number_of_colors = len(colors)
    theta = 2*3.14/number_of_colors
    
    for i in range(number_of_colors):
        angle = theta * i
        centres.append( (radius*math.cos(angle), radius*math.sin(angle) )   )
        
    for v in G.nodes(data=False):
        G.node[v]['color'] = colors[ hash(v)%number_of_colors]
        bucket = centres[hash(v)%number_of_colors]
        pos[v] = plt.array(circle.circle_coordinates(bucket[0],bucket[1],1))
        
    return pos
    

G = nx.read_dot("/home/pranav/workspace/Netwoks/Data/graphs.dot")
G = G.to_undirected()
colors = ["blue","green","white","red","yellow","orange","pink","grey"]
pos = circular_random_hash(G, colors, radius=10) 

for v in G.nodes(data=False):
    nx.draw_networkx_nodes(G, pos, [v], node_size = G.degree(v)*50, node_color = G.node[v]['color'])
nx.draw_networkx_edges(G, pos, edgelist=G.edges(),width = 0.2)

plt.show()