import matplotlib
matplotlib.use('TkAgg')
from pylab import *

n = 120 # size of space: n x n
p = 0.6 # probability of initially panicky individuals

def initial_density(val = p):
    global p
    p = val
    return val

def initialize():
    global config, nextconfig
    config = zeros([n, n])
    for x in range(n):
        for y in range(n):
            config[x, y] = 1 if random() < p else 0
    nextconfig = zeros([n, n])
    
def observe():
    global config, nextconfig
    cla()
    imshow(config, vmin = 0, vmax = 1, cmap = cm.binary)

def update():
    global config, nextconfig
    for x in range(n):
        for y in range(n):
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    count += config[(x + dx) % n, (y + dy) % n]
            if config[x, y] == 0:
                nextconfig[x, y] = 1 if count == 3 else 0
            elif config[x,y] == 1:
                nextconfig[x, y] = 1 if count == 3 or count == 4 else 0
    config, nextconfig = nextconfig, config

import pycxsimulator
pycxsimulator.GUI(parameterSetters = [initial_density]).start(func=[initialize, observe, update])
