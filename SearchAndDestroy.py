import numpy as np
import random as ran
import CreateMap
import heapq
import math
import matplotlib.pyplot as plt

def search_space(space, agent):
    agent.score += 1                                                                            #Each search increases agent's score
    if not space.target:
        space.misses+=1
        return 0
    if ran.random() > space.terrain:
        return 1
    else:
        space.misses+=1
        return 0

# def prob_formula(prob, dim, miss_rate, n):
#     return (prob)/(1-(1/dim**2)+((1/dim**2)*(miss_rate**n)))

# def update_map(unsearched_list, map):
#     dim = len(map)
#     for space in unsearched_list:
#         space.prob = prob_formula(space.prob, dim, space.terrain, space.misses)

def prob_contains(map_space, fail_prob, fail_terrain, agent):                                                #Calculates P(in cell I | failure cell J)
    prob_given_fail = map_space.prob / (fail_prob*fail_terrain+1-fail_prob)
    map_space.prob = prob_given_fail
    map_space.manhattan = abs(map_space.x - agent.x) + abs(map_space.y - agent.y)

def fail_in_current(fail_space, agent):                                                         #Calculates P(in cell J | failure cell J)
    new_prob = fail_space.prob * fail_space.terrain / (fail_space.prob * fail_space.terrain + 1 - fail_space.prob)
    fail_space.prob = new_prob
    fail_space.manhattan = abs(fail_space.x - agent.x) + abs(fail_space.y - agent.y)

def update_prob_map(fringe, agent, fail_prob, fail_terrain):
    for space in fringe:
        prob_contains(space, fail_prob, fail_terrain, agent)

def agent_1(dim):
    creation_output = CreateMap.create_map_1(dim)
    environment = creation_output[0]
    my_agent = creation_output[1]
    #CreateMap.print_terrain(environment)
    fringe = []                                                                         #Holds all map spaces for probability checking
    for x in range(dim):
        for y in range(dim):
            fringe.append(environment[x][y])
    while(True):
        CreateMap.print_map(environment)
        print(sum_probs(environment))
        heapq.heapify(fringe)
        goal_search = heapq.heappop(fringe)                                             #Highest probability && Lowest manhattan
        agent_space = (my_agent.x, my_agent.y)
        if agent_space == goal_search.query:                                            #Highest prob is current space
            check = search_space(goal_search, my_agent)                                 #Check if target is found
            if check:
                CreateMap.print_map(environment)
                return my_agent.score
        else:                                                                           #Agent needs to travel
            my_agent.score += goal_search.manhattan                                     #Distance traveled is manhattan, no need to actually travel for basic agent
            my_agent.x = goal_search.x                                                  #Update agent's location
            my_agent.y = goal_search.y
            check = search_space(goal_search, my_agent)                                 #Check if target is found
            if check:
                CreateMap.print_map(environment)
                print("It took {} searches in {} terrain {} to hit the target.\n".format(goal_search.misses+1, goal_search.terrain, goal_search.query))
                return my_agent.score
        fail_prob = goal_search.prob
        fail_terrain = goal_search.terrain
        fail_in_current(goal_search, my_agent)
        update_prob_map(fringe, my_agent, fail_prob, fail_terrain)
        fringe.append(goal_search)

def agent_1_dep(dim, environment, my_agent):
    #CreateMap.print_terrain(environment)
    fringe = []                                                                         #Holds all map spaces for probability checking
    for x in range(dim):
        for y in range(dim):
            fringe.append(environment[x][y])
    while(True):
        #CreateMap.print_map(environment)
        heapq.heapify(fringe)
        goal_search = heapq.heappop(fringe)                                             #Highest probability && Lowest manhattan
        agent_space = (my_agent.x, my_agent.y)
        if agent_space == goal_search.query:                                            #Highest prob is current space
            check = search_space(goal_search, my_agent)                                 #Check if target is found
            if check:
                CreateMap.print_map(environment)
                return my_agent.score
        else:                                                                           #Agent needs to travel
            my_agent.score += goal_search.manhattan                                     #Distance traveled is manhattan, no need to actually travel for basic agent
            my_agent.x = goal_search.x                                                  #Update agent's location
            my_agent.y = goal_search.y
            check = search_space(goal_search, my_agent)                                 #Check if target is found
            if check:
                CreateMap.print_map(environment)
                print("It took {} searches in {} terrain {} to hit the target.\n".format(goal_search.misses+1, goal_search.terrain, goal_search.query))
                return my_agent.score
        fail_prob = goal_search.prob
        fail_terrain = goal_search.terrain
        fail_in_current(goal_search, my_agent)
        update_prob_map(fringe, my_agent, fail_prob, fail_terrain)
        fringe.append(goal_search)

def agent_2(dim):
    creation_output = CreateMap.create_map_2(dim)
    environment = creation_output[0]
    my_agent = creation_output[1]
    #CreateMap.print_terrain(environment)
    fringe = []                                                                         #Holds all map spaces for probability checking
    for x in range(dim):
        for y in range(dim):
            fringe.append(environment[x][y])
    while(True):
        #CreateMap.print_map(environment)
        heapq.heapify(fringe)
        goal_search = heapq.heappop(fringe)                                             #Highest probability && Lowest manhattan
        agent_space = (my_agent.x, my_agent.y)
        if agent_space == goal_search.query:                                            #Highest prob is current space
            check = search_space(goal_search, my_agent)                                 #Check if target is found
            if check:
                CreateMap.print_map(environment)
                return my_agent.score
        else:                                                                           #Agent needs to travel
            my_agent.score += goal_search.manhattan                                     #Distance traveled is manhattan, no need to actually travel for basic agent
            my_agent.x = goal_search.x                                                  #Update agent's location
            my_agent.y = goal_search.y
            check = search_space(goal_search, my_agent)                                 #Check if target is found
            if check:
                CreateMap.print_map(environment)
                print("It took {} searches in {} terrain {} to hit the target.\n".format(goal_search.misses+1, goal_search.terrain, goal_search.query))
                return my_agent.score
        fail_prob = goal_search.prob
        fail_terrain = goal_search.terrain
        fail_in_current(goal_search, my_agent)
        update_prob_map(fringe, my_agent, fail_prob, fail_terrain)
        fringe.append(goal_search)

def agent_2_dep(dim, environment, my_agent):
    #CreateMap.print_terrain(environment)
    fringe = []                                                                         #Holds all map spaces for probability checking
    for x in range(dim):
        for y in range(dim):
            fringe.append(environment[x][y])
    while(True):
        #CreateMap.print_map(environment)
        heapq.heapify(fringe)
        goal_search = heapq.heappop(fringe)                                             #Highest probability && Lowest manhattan
        agent_space = (my_agent.x, my_agent.y)
        if agent_space == goal_search.query:                                            #Highest prob is current space
            check = search_space(goal_search, my_agent)                                 #Check if target is found
            if check:
                CreateMap.print_map(environment)
                return my_agent.score
        else:                                                                           #Agent needs to travel
            my_agent.score += goal_search.manhattan                                     #Distance traveled is manhattan, no need to actually travel for basic agent
            my_agent.x = goal_search.x                                                  #Update agent's location
            my_agent.y = goal_search.y
            check = search_space(goal_search, my_agent)                                 #Check if target is found
            if check:
                CreateMap.print_map(environment)
                print("It took {} searches in {} terrain {} to hit the target.\n".format(goal_search.misses+1, goal_search.terrain, goal_search.query))
                return my_agent.score
        fail_prob = goal_search.prob
        fail_terrain = goal_search.terrain
        fail_in_current(goal_search, my_agent)
        update_prob_map(fringe, my_agent, fail_prob, fail_terrain)
        fringe.append(goal_search)

def agent_3(dim):
    creation_output = CreateMap.create_map_3(dim)
    environment = creation_output[0]
    my_agent = creation_output[1]
    #CreateMap.print_terrain(environment)
    fringe = []                                                                         #Holds all map spaces for probability checking
    for x in range(dim):
        for y in range(dim):
            fringe.append(environment[x][y])
    while(True):
        #CreateMap.print_map(environment)
        heapq.heapify(fringe)
        goal_search = heapq.heappop(fringe)                                             #Highest probability && Lowest manhattan
        agent_space = (my_agent.x, my_agent.y)
        if agent_space == goal_search.query:                                            #Highest prob is current space
            check = search_space(goal_search, my_agent)                                 #Check if target is found
            if check:
                CreateMap.print_map(environment)
                return my_agent.score
        else:                                                                           #Agent needs to travel
            my_agent.score += goal_search.manhattan                                     #Distance traveled is manhattan, no need to actually travel for basic agent
            my_agent.x = goal_search.x                                                  #Update agent's location
            my_agent.y = goal_search.y
            check = search_space(goal_search, my_agent)                                 #Check if target is found
            if check:
                CreateMap.print_map(environment)
                print("It took {} searches in {} terrain {} to hit the target.\n".format(goal_search.misses+1, goal_search.terrain, goal_search.query))
                return my_agent.score
        fail_prob = goal_search.prob
        fail_terrain = goal_search.terrain
        fail_in_current(goal_search, my_agent)
        update_prob_map(fringe, my_agent, fail_prob, fail_terrain)
        fringe.append(goal_search)

def agent_3_dep(dim, environment, my_agent):
    creation_output = CreateMap.create_map_3(dim)
    #CreateMap.print_terrain(environment)
    fringe = []                                                                         #Holds all map spaces for probability checking
    for x in range(dim):
        for y in range(dim):
            fringe.append(environment[x][y])
    while(True):
        #CreateMap.print_map(environment)
        heapq.heapify(fringe)
        goal_search = heapq.heappop(fringe)                                             #Highest probability && Lowest manhattan
        agent_space = (my_agent.x, my_agent.y)
        if agent_space == goal_search.query:                                            #Highest prob is current space
            check = search_space(goal_search, my_agent)                                 #Check if target is found
            if check:
                CreateMap.print_map(environment)
                return my_agent.score
        else:                                                                           #Agent needs to travel
            my_agent.score += goal_search.manhattan                                     #Distance traveled is manhattan, no need to actually travel for basic agent
            my_agent.x = goal_search.x                                                  #Update agent's location
            my_agent.y = goal_search.y
            check = search_space(goal_search, my_agent)                                 #Check if target is found
            if check:
                CreateMap.print_map(environment)
                print("It took {} searches in {} terrain {} to hit the target.\n".format(goal_search.misses+1, goal_search.terrain, goal_search.query))
                return my_agent.score
        fail_prob = goal_search.prob
        fail_terrain = goal_search.terrain
        fail_in_current(goal_search, my_agent)
        update_prob_map(fringe, my_agent, fail_prob, fail_terrain)
        fringe.append(goal_search)

def sum_probs(map):
    total = 0
    dim = len(map)
    for x in range(dim):
        for y in range(dim):
            total += map[x][y].prob
    return total
            
def compare_agents(agent_1, agent_2, agent_3, dim, trials):
    count_1 = 0
    count_2 = 0
    count_3 = 0
    for y in range(trials):                                            #Perform 100 tests per density
        maps = CreateMap.create_all_maps(dim)
        count_1 += agent_1_dep(dim, maps[0][0], maps[0][1])
        count_2 += agent_2_dep(dim, maps[1][0], maps[1][1])                                      
        count_3 += agent_3_dep(dim, maps[2][0], maps[2][1])
    print(count_1/trials, count_2/trials, count_3/trials)

if __name__ == '__main__':
    #score = agent_1(2)
    #print("Your score is {}.\n".format(score))
    compare_agents(agent_1, agent_2, agent_3, 10, 100)



