import numpy as np
import random as ran
import CreateMap
import heapq

def search_space(space, agent):
    agent.score += 1                                                                            #Each search increases agent's score
    if not space.target:
        return 0
    if ran.random() > space.terrain:
        return 1
    else:
        return 0

# def prob_formula(prob, dim, miss_rate, n):
#     return (prob)/(1-(1/dim**2)+((1/dim**2)*(miss_rate**n)))

# def update_map(unsearched_list, map):
#     dim = len(map)
#     for space in unsearched_list:
#         space.prob = prob_formula(space.prob, dim, space.terrain, space.misses)

def prob_contains(map_space, fail_space, agent):                                                #Calculates P(in cell I | failure cell J)
    prob_given_fail = map_space.prob / (fail_space.prob*fail_space.terrain+1-fail_space.prob)
    map_space.prob = prob_given_fail
    map_space.manhattan = abs(map_space.x - agent.x) + abs(map_space.y - agent.y)

def fail_in_current(fail_space, agent):                                                         #Calculates P(in cell J | failure cell J)
    new_prob = fail_space.prob * fail_space.terrain / (fail_space.prob * fail_space.terrain + 1 - fail_space.prob)
    fail_space.prob = new_prob
    fail_space.manhattan = abs(fail_space.x - agent.x) + abs(fail_space.y - agent.y)

def update_prob_map(fringe, agent, fail_space):
    for space in fringe:
        prob_contains(space, fail_space, agent)

def agent_1(dim):
    creation_output = CreateMap.create_map(dim)
    environment = creation_output[0]
    my_agent = creation_output[1]
    CreateMap.print_terrain(environment)
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
                return my_agent.score
        fail_in_current(goal_search, my_agent)
        update_prob_map(fringe, my_agent, goal_search)
        fringe.append(goal_search)
            
if __name__ == '__main__':
    score = agent_1(5)
    print("Your score is {}.\n".format(score))



