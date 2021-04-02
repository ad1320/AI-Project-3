import numpy as np
import random as ran
import CreateMap

def search_space(space):
    if not space.target:
        return 0
    if ran.random() > space.terrain:
        return 1
    else:
        return 0

def prob_formula(prob, dim, miss_rate, n):
    return (prob)/(1-(1/dim**2)+((1/dim**2)*(miss_rate**n)))

def update_map(unsearched_list, map):
    dim = len(map)
    for space in unsearched_list:
        space.prob = prob_formula(space.prob, dim, space.terrain, space.misses)



