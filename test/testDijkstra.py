import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, '..',  '..', 'src')))
from testUtils import *
from readGraph import *
from graph import *
from dijkstra import *

def run():
    df_adyacents = readGraph("../files/hallwaysGraph.json",
                             {"id": str, "adyacents": list})
    graph = Graph(df_adyacents, False)
    graph.draw("test", [])
    source = 0
    dijkstra = Dijkstra(graph, source)

    test("distances to from 0 to 0 is: 0", dijkstra.getDistanceTo(0), 0)
    test("distances to from 0 to 1 is: 10", dijkstra.getDistanceTo(1), 10)
    test("distances to from 0 to 2 is: 9", dijkstra.getDistanceTo(2), 9)
    test("distances to from 0 to 3 is: 8", dijkstra.getDistanceTo(3), 8)
    test("distances to from 0 to 4 is: 7", dijkstra.getDistanceTo(4), 7)
    test("distances to from 0 to 5 is: 6", dijkstra.getDistanceTo(5), 6)
    test("distances to from 0 to 6 is: 5", dijkstra.getDistanceTo(6), 5)
    test("distances to from 0 to 7 is: 4", dijkstra.getDistanceTo(7), 4)
    test("distances to from 0 to 8 is: 3", dijkstra.getDistanceTo(8), 3)
    test("distances to from 0 to 9 is: 2", dijkstra.getDistanceTo(9), 2)
    test("distances to from 0 to 10 is: 1", dijkstra.getDistanceTo(10), 1)
    test("distances to from 0 to 11 is: 10", dijkstra.getDistanceTo(11), 10)
    test("distances to from 0 to 12 is: 9", dijkstra.getDistanceTo(12), 9)
    test("distances to from 0 to 13 is: 8", dijkstra.getDistanceTo(13), 8)
    test("distances to from 0 to 14 is: 7", dijkstra.getDistanceTo(14), 7)
    test("distances to from 0 to 15 is: 6", dijkstra.getDistanceTo(15), 6)
    test("distances to from 0 to 16 is: 5", dijkstra.getDistanceTo(16), 5)
    test("distances to from 0 to 17 is: 4", dijkstra.getDistanceTo(17), 4)
    test("distances to from 0 to 18 is: 3", dijkstra.getDistanceTo(18), 3)
    test("distances to from 0 to 19 is: 2", dijkstra.getDistanceTo(19), 2)
    test("distances to from 0 to 20 is: 3", dijkstra.getDistanceTo(20), 3)

    test("The best path from 0 to 0 is: [0]", dijkstra.getPathTo(0), [0])
    test("The best path from 0 to 1 is: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]", dijkstra.getPathTo(
        1), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0])
    test("The best path from 0 to 2 is: [2, 3, 4, 5, 6, 7, 8, 9, 10, 0]", dijkstra.getPathTo(
        2), [2, 3, 4, 5, 6, 7, 8, 9, 10, 0])
    test("The best path from 0 to 3 is: [3, 4, 5, 6, 7, 8, 9, 10, 0]", dijkstra.getPathTo(
        3), [3, 4, 5, 6, 7, 8, 9, 10, 0])
    test("The best path from 0 to 4 is: [4, 5, 6, 7, 8, 9, 10, 0]", dijkstra.getPathTo(
        4), [4, 5, 6, 7, 8, 9, 10, 0])
    test("The best path from 0 to 5 is: [5, 6, 7, 8, 9, 10, 0]", dijkstra.getPathTo(
        5), [5, 6, 7, 8, 9, 10, 0])
    test("The best path from 0 to 6 is: [6, 7, 8, 9, 10, 0]", dijkstra.getPathTo(
        6), [6, 7, 8, 9, 10, 0])
    test("The best path from 0 to 7 is: [7, 8, 9, 10, 0]", dijkstra.getPathTo(
        7), [7, 8, 9, 10, 0])
    test("The best path from 0 to 8 is: [8, 9, 10, 0]", dijkstra.getPathTo(
        8), [8, 9, 10, 0])
    test("The best path from 0 to 9 is: [9, 10, 0]",
         dijkstra.getPathTo(9), [9, 10, 0])
    test("The best path from 0 to 10 is: [10, 0]",
         dijkstra.getPathTo(10), [10, 0])
    test("The best path from 0 to 11 is: [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]", dijkstra.getPathTo(
        11), [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0])
    test("The best path from 0 to 12 is: [12, 3, 4, 5, 6, 7, 8, 9, 10, 0]", dijkstra.getPathTo(
        12), [12, 3, 4, 5, 6, 7, 8, 9, 10, 0])
    test("The best path from 0 to 13 is: [13, 4, 5, 6, 7, 8, 9, 10, 0]", dijkstra.getPathTo(
        13), [13, 4, 5, 6, 7, 8, 9, 10, 0])
    test("The best path from 0 to 14 is:  [14, 5, 6, 7, 8, 9, 10, 0]", dijkstra.getPathTo(
        14), [14, 5, 6, 7, 8, 9, 10, 0])
    test("The best path from 0 to 15 is:  [15, 6, 7, 8, 9, 10, 0]", dijkstra.getPathTo(
        15),  [15, 6, 7, 8, 9, 10, 0])
    test("The best path from 0 to 16 is: [16, 7, 8, 9, 10, 0]", dijkstra.getPathTo(
        16), [16, 7, 8, 9, 10, 0])
    test("The best path from 0 to 17 is:  [17, 8, 9, 10, 0]", dijkstra.getPathTo(
        17),  [17, 8, 9, 10, 0])
    test("The best path from 0 to 18 is: [18, 9, 10, 0]", dijkstra.getPathTo(
        18), [18, 9, 10, 0])
    test("The best path from 0 to 19 is: [19, 10, 0]", dijkstra.getPathTo(
        19), [19, 10, 0])
    test("The best path from 0 to 20 is: [20, 19, 10, 0]", dijkstra.getPathTo(
        20), [20, 19, 10, 0])


run()
