import pandas as pd
from annoy import AnnoyIndex
import networkx as nx
import config as cfg

class NearestNeighbours():
    def __init__(self):
        self.__numTrees = cfg.extraction["numberOfTrees"]
        self.__featureDimensions = cfg.extraction["featureDimensions"]
        self.__chunkSize = cfg.extraction["chunkSize"]
        self.__featureColumnNames = cfg.extraction["featureColumnNames"]
        self.__idsColumnName = cfg.extraction["idsColumnName"]
        self.__indexFileName = cfg.extraction["annoyIndexFileSaveName"]
        self.__nearestNeighbours = cfg.extraction["nearestNeighbours"]
        self.__distanceCalculation = 'angular'

    # generate index from csv provided
    def generateIndex(self, csvFilePath: str):
        annoyIndex = AnnoyIndex(self.__featureDimensions, self.__distanceCalculation)
        csvReader = pd.read_csv(csvFilePath, chunksize=self.__chunkSize)
        for chunk in csvReader:
            featuresDf = chunk[self.__featureColumnNames].copy()
            features = featuresDf.values

            ids = chunk[self.__idsColumnName].values
            num_points = len(features)

            for i in range(num_points):
                annoyIndex.add_item(ids[i], features[i])

        annoyIndex.build(self.__numTrees)
        self.__index = annoyIndex
     
    # save index to local disk
    def saveIndex(self):
        assert(self.__index, "index is not created cannot save index")
        self.__index.save(self.__indexFileName)        
    
    # load index from local disk
    def loadIndex(self):
        self.__index = AnnoyIndex(self.__featureDimensions, self.__distanceCalculation)
        self.__index.load(self.__indexFileName)

    # get nearest neighbours for provided node
    def getNearestNeighbours(self, point: int):
       assert(self.__index, "index not found cannot save index")
       queryPoint = self.__index.get_item_vector(point)
       nearestNeighbors, distances = self.__index.get_nns_by_vector(queryPoint, self.__nearestNeighbours+1, include_distances=True)
       nearestNeighbors = nearestNeighbors[1:]  # Exclude the point itself
       distances = distances[1:]  # Exclude distance to itself 
       return [nearestNeighbors, distances]
        

