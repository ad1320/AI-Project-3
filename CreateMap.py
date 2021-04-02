import numpy as np
import random as ran

class Agent:
    def __init__(self, start, map):                                                        #Agent receives the map and its starting square as inputs
        self.map = map
        self.query = start
        self.x = start[0]
        self.y = start[1]                          

class MapSpace:                                                                      #Holds all the info for a map space
    def __init__(self, dim, query, terrain):                                         #Inputs are the space (query), the current map and dimension
        self.query = query
        self.x = query[0]
        self.y = query[1]
        self.terrain = terrain
        self.target = 0
        self.misses = 0
        self.init_prob = 1/(dim**2)
        self.prob = 1/(dim**2)
    def __lt__(self, other):                                                        #Order the fringe based on how close to guarantee
        return self.prob < other.prob



def create_map(dim):
    map = []
    terrains = [0.1, 0.3, 0.7, 0.9]
    for x in range(dim):
        map.append([])
        for y in range(dim):
            t_num = ran.randint(0,3)
            map[x].append(MapSpace(dim, (x,y), terrains[t_num]))
    rand_x = ran.randint(0,dim-1)
    rand_y = ran.randint(0,dim-1)
    map[rand_x][rand_y].target = 1

def print_map(map):
    dim = len(map)
    pm = np.zeros((dim, dim), dtype=int)
    for i in range(dim):
        for j in range(dim):
            pm[i][j] = map[i][j].prob
    print(pm)