from dijkstra import *
from digraph import *
from readGraph import *


def run():
    df_adyacents = readGraph("files/hallwaysDigraph.json",
                             {"id": str, "adyacents": list})
    digraph = Digraph(df_adyacents, False)
    digraph.draw("test")
    source1 = 0
    dFromSource1 = Dijkstra(digraph, source1)
    for i in range(len(dFromSource1.distances)):
        print("distances to from " + str(source1)  + " to "+ str(i) + " is: " + str(dFromSource1.distances[i]))
        print("path to from " + str(source1)  + " to "+ str(i) + " is: " + str(dFromSource1.getPathTo(i)))

    source2 = 1
    dFromSource2 = Dijkstra(digraph, source2)
    for i in range(len(dFromSource2.distances)):
        print("distances to from " + str(source2)  + " to "+ str(i) + " is: " + str(dFromSource2.distances[i]))
        print("path to from " + str(source2)  + " to "+ str(i) + " is: " + str(dFromSource2.getPathTo(i)))

    target = 13
    if (dFromSource1.distances[target] < dFromSource2.distances[target]):
        print("the best path to go " + str(target) + " is from source " + str(source1) + ". The cost is : " + str(dFromSource1.distances[target]) + ". the path is : " + str(dFromSource1.getPathTo(target)))
    else:
        print("the best path to go " + str(target) + " is from source " + str(source2) + ". The cost is : " + str(dFromSource2.distances[target]) + ". the path is : " + str(dFromSource2.getPathTo(target)))
run()
