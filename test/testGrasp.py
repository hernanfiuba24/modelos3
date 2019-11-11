import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, '..',  '..', 'src')))
from testUtils import *
from grasp import *
from graph import *
from readGraph import *

def run():
    df_adyacents = readGraph("../files/hallwaysGraph.json",
                             {"id": str, "adyacents": list})
    graph = Graph(df_adyacents, False)
    
    sources = [0, 1]
    target = 13

    grasp = Grasp(sources, graph)
    test("The best path to 13 is [13, 4, 3, 2, 1]",
         grasp.bestPathTo(target)[1], [13, 4, 3, 2, 1])
    test("The best cost to 13 is 4", grasp.bestPathTo(target)[0], 4)


run()
