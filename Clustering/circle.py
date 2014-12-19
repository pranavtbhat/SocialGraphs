import networkx as nx
import pylab as plt
import itertools as itools
import math 
import random


def circle_coordinates(centreX,centreY,radius):
    t = abs(2*3.14*random.random())
    
    u = radius*random.random()
        
    return [centreX + u*math.cos(t), centreY + u*math.sin(t)]

