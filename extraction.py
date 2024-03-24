import pandas as pd
from annoy import AnnoyIndex
import networkx as nx
import config as cfg

NUMBER_OF_FEATURE = 5

def build_annoy_index(csv_file_path, chunk_size=cfg.extraction["chunkSize"], num_trees=10):
    annoy_index = AnnoyIndex(cfg.extraction["featureDimensions"], 'angular')

    csv_reader = pd.read_csv(csv_file_path, chunksize=chunk_size)
    for chunk in csv_reader:
        featuresDf = chunk[cfg.extraction["featureColumnNames"]].copy()
        features = featuresDf.values

        ids = chunk["ids"].values
        num_points = len(features)

        for i in range(num_points):
            annoy_index.add_item(ids[i], features[i])

    annoy_index.build(num_trees)
    return annoy_index

def build_directed_graph(annoy_index, csv_file_path, chunk_size=cfg.extraction["chunkSize"], n_neighbors=cfg.extraction["nearestNeighbours"], ):
    graph = nx.DiGraph()

    csv_reader = pd.read_csv(csv_file_path, chunksize=chunk_size)
    for chunk in csv_reader:
        ids = chunk["ids"].values
        num_points = len(ids)

        for i in range(num_points):
            query_point = annoy_index.get_item_vector(ids[i])
            nearest_neighbors, distances = annoy_index.get_nns_by_vector(query_point, n_neighbors+1, include_distances=True)
            nearest_neighbors = nearest_neighbors[1:]  # Exclude the point itself
            distances = distances[1:]  # Exclude distance to itself

            for neighbor, distance in zip(nearest_neighbors, distances):
                graph.add_edge(i, neighbor, weight=distance)

    return graph

def saveData(annoy_index, directed_graph):
    annoy_index.save(cfg.extraction["annoyIndexFileSaveName"])
    nx.write_pajek(directed_graph, cfg.extraction["graphFileSaveName"])

# Example usage
csv_file_path = cfg.extraction["csvFileToLoad"]
annoy_index = build_annoy_index(csv_file_path)
directed_graph = build_directed_graph(annoy_index, csv_file_path)
saveData(annoy_index, directed_graph)