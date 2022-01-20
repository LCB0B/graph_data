import networkx as nx

graph_path="../../Homo_sapiens_undirected.gml"
output_path="../Homo_sapiens_undirected_gcc.gml"

g=nx.read_gml(graph_path)

gcc = max(nx.connected_component_subgraphs(g), key=len)



# relabel nodes
label2new = {}
for nodeId, node in enumerate(gcc.nodes()):
	label2new[node]=str(nodeId)

gcc = nx.relabel_nodes(G=gcc, mapping=label2new)

nx.write_gml(gcc, output_path)
