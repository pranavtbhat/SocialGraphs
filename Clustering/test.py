import re
import networkx as nx

G = nx.Graph()

with open("/home/pranav/workspace/Netwoks/Data/graph.dot") as file:
    
    re1='(\\d+)'    # Integer Number 1
    re2='.*?'    # Non-greedy match on filler
    re3='(\\d+)'    # Integer Number 2
    re4='.*?'    # Non-greedy match on filler
    re5='(\\d+)'    # Integer Number 3
    
    rg = re.compile(re1+re2+re3+re4+re5,re.IGNORECASE|re.DOTALL)
    
    for line in file.readlines():
        
        m = rg.search(line)
        if m:
            int1=m.group(1)
            int2=m.group(2)
            int3=m.group(3)
            
            if not G.get_edge_data(int1,int2):
                G.add_edge(int1, int2, weight= int3)


nx.write_dot(G, path="/home/pranav/workspace/Netwoks/Data/graphs.dot")