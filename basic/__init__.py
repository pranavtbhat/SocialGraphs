import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G = nx.erdos_renyi_graph(30,.05)
nx.write_dot(G,"data.dot")

