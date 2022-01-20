import os
import sys
import numpy as np
import networkx as nx
from scipy.sparse import csr_matrix
import scipy.io as sio

base_folder="./"

datasets=["blogcatalog_newborn_gcc_residual", "citeseer_newborn_gcc_residual", "cora_newborn_gcc_residual", "dblp_newborn_gcc_residual",  "Homo_sapiens_newborn_gcc_residual"]
#datasets=["blogcatalog_newborn_gcc_residual", "ca-AstroPh_gcc_residual", "ca-GrQc_gcc_residual", "ca-HepTh_gcc_residual", "citeseer_undirected_gcc_residual", "cora_undirected_gcc_residual", "dblp_undirected_gcc_residual", "facebook_combined_gcc_residual", "gnutella09_relabeledgcc_residual", "Homo_sapiens_undirected_gcc_residual", "wiki-Vote_gcc_residual"]

for dataset_name in datasets:
	
	input_path = os.path.join(base_folder+"residuals/", dataset_name + ".gml")
	output_path = os.path.join(base_folder+"residuals/", dataset_name + ".mat")

	g = nx.read_gml(input_path)

	print(g.number_of_nodes(), g.number_of_edges())


	M = nx.adjacency_matrix(g, nodelist = [str(node) for node in range(g.number_of_nodes())])

	#S=np.asarray(M.todense())
	#print(S.shape, type(S))
	#M.astype(np.)
	S=M*1.0
	mdict={'network': S}



	sio.savemat(file_name=output_path, mdict=mdict, do_compression=False)

