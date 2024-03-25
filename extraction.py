import config as cfg
from nearestNeighbours import NearestNeighbours
from graph import Graph

def extract():
    csv = cfg.extraction["csvFileToLoad"]
    nearestNeighbours = NearestNeighbours()
    nearestNeighbours.generateIndex(csv)

    graph = Graph()
    graph.generateGraph(nearestNeighbours, csv)
    graph.saveGraph()

    return graph

#extract()

