import numpy as np
import random as ran

class Agent:
    def __init__(self, start, map):                                                     #Agent receives the map and its starting square as inputs
        self.map = map
        self.query = start
        self.x = start[0]
        self.y = start[1]     
        self.score = 0                                                                  #Distance traveled + number of searches   
        self.distance = 0                  

class MapSpace_1:                                                                         #Holds all the info for a map space
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
    def __lt__(self, other):                                                            #Order the fringe based on how close to guarantee for target to be there
        if self.prob == other.prob:
            return self.manhattan < other.manhattan
        return self.prob*-1 < other.prob*-1

class MapSpace_2:                                                                         #Holds all the info for a map space
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
    def __lt__(self, other):                                                            #Order the fringe based on how close to guarantee to find target there
        if self.prob*(1-self.terrain) == other.prob*(1-other.terrain):
            return self.manhattan < other.manhattan
        return self.prob*(1-self.terrain)*-1 <other.prob*(1-other.terrain)*-1

class MapSpace_3:                                                                         #Holds all the info for a map space
    def __init__(self, dim, query, terrain, agent_space):         #Inputs are the space (query), the current map ,dimension, and agent's location
        self.query = query
        self.dim = dim
        self.x = query[0]
        self.y = query[1]
        self.terrain = terrain
        self.target = 0
        self.misses = 0
        self.init_prob = 1/(dim**2)
        self.prob = 1/(dim**2)
        self.manhattan = abs(query[0] - agent_space[0]) + abs(query[1] - agent_space[1])
    def __lt__(self, other):                                                            #Order the fringe based on how close to guarantee with a penalty commesurate with the distance to the square from current position
        return ((self.prob*-1) + ((1/(self.dim**3)) * self.manhattan)) < ((other.prob*-1) + ((1/(self.dim**3)) * other.manhattan))

#Create map functions are identical except for which Map_Space (and, thus, comparison method) they use

def create_map_1(dim):
    map = []
    terrains = [0.1, 0.3, 0.7, 0.9]                             #Possible false negative values
    start_x = ran.randint(0,dim-1)
    start_y = ran.randint(0,dim-1)
    start_space = (start_x, start_y)                            #Randomly choose agent starting square
    for x in range(dim):
        map.append([])                                          #Add a row
        for y in range(dim):
            t_num = ran.randint(0,3)                            #Choose a terrain at random
            map[x].append(MapSpace_1(dim, (x,y), terrains[t_num], start_space))                         #Add a map_space object at current position
    rand_x = ran.randint(0,dim-1)
    rand_y = ran.randint(0,dim-1)
    map[rand_x][rand_y].target = 1                                                      #Place the target at a random position
    my_agent = Agent(start_space, map)
    #print("The ({}, {}) spot holds the target.\n".format(rand_x, rand_y))
    #print("The agent starts at ({}, {}).\n".format(start_x, start_y))
    return [map, my_agent]

def create_map_2(dim):
    map = []
    terrains = [0.1, 0.3, 0.7, 0.9]
    start_x = ran.randint(0,dim-1)
    start_y = ran.randint(0,dim-1)
    start_space = (start_x, start_y)
    for x in range(dim):
        map.append([])
        for y in range(dim):
            t_num = ran.randint(0,3)
            map[x].append(MapSpace_2(dim, (x,y), terrains[t_num], start_space))
    rand_x = ran.randint(0,dim-1)
    rand_y = ran.randint(0,dim-1)
    map[rand_x][rand_y].target = 1
    my_agent = Agent(start_space, map)
    #print("The ({}, {}) spot holds the target.\n".format(rand_x, rand_y))
    #print("The agent starts at ({}, {}).\n".format(start_x, start_y))
    return [map, my_agent]

def create_map_3(dim):
    map = []
    terrains = [0.1, 0.3, 0.7, 0.9]
    start_x = ran.randint(0,dim-1)
    start_y = ran.randint(0,dim-1)
    start_space = (start_x, start_y)
    for x in range(dim):
        map.append([])
        for y in range(dim):
            t_num = ran.randint(0,3)
            map[x].append(MapSpace_3(dim, (x,y), terrains[t_num], start_space))
    rand_x = ran.randint(0,dim-1)
    rand_y = ran.randint(0,dim-1)
    map[rand_x][rand_y].target = 1
    my_agent = Agent(start_space, map)
    #print("The ({}, {}) spot holds the target.\n".format(rand_x, rand_y))
    #print("The agent starts at ({}, {}).\n".format(start_x, start_y))
    return [map, my_agent]

def create_all_maps(dim):                                           #Creates one map as above, then copies it twice but uses the other type of map_spaces in the copies (same terrains and locations of agent and target)
    maps = [[[],[]],[[],[]],[[],[]]]
    terrains = [0.1, 0.3, 0.7, 0.9]
    start_x = ran.randint(0,dim-1)
    start_y = ran.randint(0,dim-1)
    start_space = (start_x, start_y)
    rand_x = ran.randint(0,dim-1)
    rand_y = ran.randint(0,dim-1)

    for x in range(dim):
        maps[0][0].append([])
        for y in range(dim):
            t_num = ran.randint(0,3)
            maps[0][0][x].append(MapSpace_1(dim, (x,y), terrains[t_num], start_space))
    maps[0][0][rand_x][rand_y].target = 1
    my_agent_1 = Agent(start_space, maps[0][0])
    maps[0][1] = my_agent_1

    for x in range(dim):
        maps[1][0].append([])
        for y in range(dim):
            maps[1][0][x].append(MapSpace_2(dim, (x,y), maps[0][0][x][y].terrain, start_space))
    maps[1][0][rand_x][rand_y].target = 1
    my_agent_2 = Agent(start_space, maps[1][0])
    maps[1][1] = my_agent_2

    for x in range(dim):
        maps[2][0].append([])
        for y in range(dim):
            t_num = ran.randint(0,3)
            maps[2][0][x].append(MapSpace_3(dim, (x,y), maps[0][0][x][y].terrain, start_space))
    maps[2][0][rand_x][rand_y].target = 1
    my_agent_3 = Agent(start_space, maps[2][0])
    maps[2][1] = my_agent_3
    
    #print("The ({}, {}) spot holds the target.\n".format(rand_x, rand_y))
    #print("The agent starts at ({}, {}).\n".format(start_x, start_y))
    return maps                                                                 #return maps and their agents as a package for use in the statistical test method


def print_map(map):
    dim = len(map)
    pm = np.zeros((dim, dim), dtype=float)                                  #prints the current belief of the target being in each space on the map
    for i in range(dim):
        for j in range(dim):
            pm[i][j] = map[i][j].prob
    print(pm)

def print_terrain(map):
    dim = len(map)
    pm = np.zeros((dim, dim), dtype=float)                                 #prints the terrain (false negative value) of each space on the map
    for i in range(dim):
        for j in range(dim):
            pm[i][j] = map[i][j].terrain
    print(pm)

if __name__ == '__main__':
    output = create_map_3(5)
    my_map = output[0]
    print_map(my_map)
    print_terrain(my_map)