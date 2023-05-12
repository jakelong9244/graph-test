import networkx as nx
import matplotlib.pyplot as plt
import random as r

G = nx.Graph()

r.seed(1)
for x in range(1,11):
    G.add_node(x,coords=[r.randint(0,10),r.randint(0,10)])


'''
G.add_nodes_from(range(1,11))
G.add_node(2,coords=[5,6])
G.add_node(1,coords=[3,4])
G.add_edge(1,2,dist=[(G.nodes[1]["coords"][0]-G.nodes[2]["coords"][0]), (G.nodes[1]["coords"][1]-G.nodes[2]["coords"][1])])
'''



print(G.nodes.data())
print(G.edges)