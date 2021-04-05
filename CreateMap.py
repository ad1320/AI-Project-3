import numpy as np
import random as ran

class Agent:
    def __init__(self, start, map):                                                     #Agent receives the map and its starting square as inputs
        self.map = map
        self.query = start
        self.x = start[0]
        self.y = start[1]     
        self.score = 0                                                                  #Distance traveled + number of searches                     

class MapSpace:                                                                         #Holds all the info for a map space
    def __init__(self, dim, query, terrain, agent_space):         #Inputs are the space (query), the current map ,dimension, and agent's location
        self.query = query
        self.x = query[0]
        self.y = query[1]
        self.terrain = terrain
        self.target = 0
        self.misses = 0
        self.init_prob = 1/(dim**2)
        self.prob = 1/(dim**2)
        self.manhattan = abs(query[0] - agent_space[0]) + abs(query[1] - agent_space[1])
    def __lt__(self, other):                                                            #Order the fringe based on how close to guarantee
        if self.prob == other.prob:
            return self.manhattan < other.manhattan
        return self.prob*-1 < other.prob*-1

def create_map(dim):
    map = []
    terrains = [0.1, 0.3, 0.7, 0.9]
    start_x = ran.randint(0,dim-1)
    start_y = ran.randint(0,dim-1)
    start_space = (start_x, start_y)
    for x in range(dim):
        map.append([])
        for y in range(dim):
            t_num = ran.randint(0,3)
            map[x].append(MapSpace(dim, (x,y), terrains[t_num], start_space))
    rand_x = ran.randint(0,dim-1)
    rand_y = ran.randint(0,dim-1)
    map[rand_x][rand_y].target = 1
    my_agent = Agent(start_space, map)
    print("The ({}, {}) spot holds the target.\n".format(rand_x, rand_y))
    print("The agent starts at ({}, {}).\n".format(start_x, start_y))
    return [map, my_agent]

def print_map(map):
    dim = len(map)
    pm = np.zeros((dim, dim), dtype=float)
    for i in range(dim):
        for j in range(dim):
            pm[i][j] = map[i][j].prob
    print(pm)

def print_terrain(map):
    dim = len(map)
    pm = np.zeros((dim, dim), dtype=float)
    for i in range(dim):
        for j in range(dim):
            pm[i][j] = map[i][j].terrain
    print(pm)

if __name__ == '__main__':
    output = create_map(5)
    my_map = output[0]
    print_map(my_map)
    print_terrain(my_map)