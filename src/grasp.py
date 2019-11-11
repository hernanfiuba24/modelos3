from dijkstra import *
import sys

class Grasp:
    def __init__(self, sources, graph):
        self.sources = sources
        self.graph = graph
        self.dijkstras = {}
        for source in sources:
            self.dijkstras[source] = Dijkstra(self.graph, source)

    def bestPathTo(self, target):
        bestDijkstra = None
        bestDistance = sys.maxint
        for source in self.dijkstras:
            if self.dijkstras[source].getDistanceTo(target) < bestDistance:
                bestDistance = self.dijkstras[source].getDistanceTo(target)
                bestDijkstra = self.dijkstras[source]
        return [bestDijkstra.getDistanceTo(target), bestDijkstra.getPathTo(target)]
