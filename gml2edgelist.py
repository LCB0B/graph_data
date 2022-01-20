import os
import sys
import numpy as np
import networkx as nx
from scipy.sparse import csr_matrix
import scipy.io as sio

base_folder = "./"
#dataset_name = "citeseer_newborn"
datasets=["blogcatalog_newborn_gcc_residual", "ca-AstroPh_gcc_residual", "ca-GrQc_gcc_residual", "ca-HepTh_gcc_residual", "citeseer_undirected_gcc_residual", "cora_undirected_gcc_residual", "dblp_undirected_gcc_residual", "facebook_combined_gcc_residual", "gnutella09_relabeledgcc_residual", "Homo_sapiens_undirected_gcc_residual", "wiki-Vote_gcc_residual"]

for dataset_name in datasets:
	
	input_path = os.path.join(base_folder+"residuals/", dataset_name + ".gml")
	output_path = os.path.join(base_folder+"residuals/", dataset_name + ".edgelist")
	output_path2 = os.path.join(base_folder+"residuals/", dataset_name + "_noweight.edgelist")

	g = nx.read_gml(input_path)
	N = g.number_of_nodes()

	with open(output_path, 'w') as fin:
		for edge in g.edges():
			fin.write("{} {} {}\n".format(edge[0], edge[1], 1.0) )
			

	with open(output_path2, 'w') as fin:
		for edge in g.edges():
		        fin.write("{} {}\n".format(edge[0], edge[1]) )


