from graph import Graph
import random
def load():
    graph = Graph()
    graph.loadGraph()
    neighbours = graph.getNeighbours(591532)
    print(neighbours)

load()