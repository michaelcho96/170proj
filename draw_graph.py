import matplotlib.pyplot as plt
from utils import create_graph
import networkx as nx

filename = "instances/12.in"
G = create_graph(filename)
nx.draw(G)
plt.show()