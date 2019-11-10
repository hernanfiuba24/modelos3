from dijkstra import *
from digraph import *
from readGraph import *


def run():
    df_adyacents = readGraph("files/hallwaysDigraph-reduce.json",
                             {"id": str, "adyacents": list})
    digraph = Digraph(df_adyacents, True)
    digraph.draw("test")
    d = Dijkstra(digraph, 0)
    print(d.distances)

run()
