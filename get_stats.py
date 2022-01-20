import networkx as nx
import numpy as np
import sys

inpath=sys.argv[1]

g = nx.read_gml(inpath)

N = g.number_of_nodes()
M = g.number_of_edges()
connected = nx.is_connected(g)

print(f"Number of nodes: {N}")
print(f"Number of edges: {M}")
print(f"Connected: {connected}")
