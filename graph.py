import pandas as pd
from nearestNeighbours import NearestNeighbours
import networkx as nx
import config as cfg

class Graph():
    def __init__(self):
        self.__graph = nx.DiGraph()
        self.__chunkSize = cfg.extraction["chunkSize"]
        self.__idsColumnName = cfg.extraction["idsColumnName"]
        self.__graphFileName = cfg.extraction["graphFileSaveName"]

    # generate graph from provided index 
    def generateGraph(self, index: NearestNeighbours, csvFilePath: str):
        csvReader = pd.read_csv(csvFilePath, chunksize=self.__chunkSize)
        for chunk in csvReader:
            ids = chunk[self.__idsColumnName].values
            num_points = len(ids)
            for i in range(num_points):
                point = ids[i]
                [nearestNeighbors, distances] = index.getNearestNeighbours(point)
                self.__addEdges(point, nearestNeighbors, distances)

    # save graph to disk location
    def saveGraph(self):
        assert(self.__graph, "cannot save graph, graph not found")
        nx.write_pajek(self.__graph, self.__graphFileName)

    # load graph from disk location to memory
    def loadGraph(self):
        G = nx.read_pajek(self.__graphFileName)
        self.__graph = nx.Graph(G)
    
    # get direct edges to neighbors
    def getNeighbours(self, point):
        return list(self.__graph.successors(point))
    
    # perform search
    def aStartSearch(self, startNode, endNode): 
        try:
            path = nx.astar_path(self.__graph, startNode, endNode)
            return path
        except nx.NetworkXNoPath:
            print("No path found between the nodes.")
            return None
    
    # add edges from source to provided neighbours
    def __addEdges(self, point, neighbors, distances): 
        for neighbor, distance in zip(neighbors, distances):
            self.__graph.add_edge(point, neighbor, weight=distance)
