import networkx as nx
from functools import wraps
import errno
import os
import signal

class TimeoutError(Exception):
    pass

def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator


def create_graph(instance):
    """
    INSTANCE: File name containing instance of problem
    Parses file, returns a networkx Digraph object
    Nodes have 'penalty' attributes: 1 for adults, 2 for children.
    """
    print("creating graph of " + instance)
    with open(instance) as f:
        n = int(f.readline())
        children_line = f.readline()
        if children_line != "\n":
            children = children_line.split(" ")
        else: 
            children = []
        g = nx.DiGraph()
        g.add_nodes_from(range(n), penalty=1)
        for c in children:
            if c == "\n":
                pass
            elif type(c) == int:
                g.node[c]['penalty'] = 2
            elif type(c) == str:
                g.node[int(c.strip())]['penalty'] = 2
        for i in range(n):
            row = f.readline()
            elements = row.split(" ")
            print(elements)
            for j in range(n):
                if "1" in elements[j]:
                    g.add_edge(i,j)
        print("num edges: " + str(len(nx.edges(g))))
    return g

"""DO NOT USE: RUNTIME EXOPNENTIAL"""
def find_cycles(input_graph):
    G = input_graph.copy(input_graph)
    nodes = G.nodes()
    list_cycles = []
    for node in nodes:
        list_cycles.extend(explore(node, node, G, []))
        G.remove_node(node)
    return list_cycles

def explore(root_node, node, input_graph, cycle):
    # At each vertex, we check to see if any of the edges lead back to the root
    # node. If so, we add that cycle to our list of cylces. If there are edges
    # which do not lead back to the vertex, we explore those nodes as well. 
    # Once we have searched all other edges, we return the list of cycles.

    #If the cycle has five elements in it, it can no longer qualify
    cycle.append(node)
    cycle_list = []
    if (len(cycle) == 6):
        return cycle_list
    # We look at all edges from node, checking if a cycle is found.
    # print(input_graph.edges(node, False ))
    for edge in input_graph.edges(node, False):
        next_vertex = edge[1]
        if next_vertex == root_node:
            cycle_list.append(cycle)
        else:
            updated_cycle = list(cycle)
            updated_graph = input_graph.copy()
            if node != root_node:
                updated_graph.remove_node(node)
            cycle_list.extend(explore(root_node, next_vertex, updated_graph, updated_cycle))
    return cycle_list 

"""Constructs an undirected graph of all valid cycles, with an edge between two nodes
   of the graph if the underlying cycles share at least one vertex"""
def construct_cluster_graph(G):
    list_cycles = list(nx.simple_cycles(G))
    for cycle in nx.simple_cycles(G):
        if len(cycle) > 5:
            list_cycles.remove(cycle)
    # We build our secondary graph of cycles
    CGraph = nx.Graph()
    counter = 0
    for cycle in list_cycles:
        penalty = 0
        for node in cycle:
            penalty += G.node[node]['penalty']
        CGraph.add_node(counter, penalty= penalty, nodes=cycle)
        counter += 1
    # If two clusters contain the same node, then we draw 
    # an edge between them.
    for cluster_a in CGraph:
        cluster_a_nodes = CGraph.node[cluster_a]['nodes']
        for cluster_b in CGraph:
            if cluster_a != cluster_b:
                cluster_b_nodes = CGraph.node[cluster_b]['nodes']
                if contain_same_element(cluster_a_nodes, cluster_b_nodes):
                    CGraph.add_edge(cluster_a, cluster_b)
    return CGraph

def contain_same_element(list_a, list_b):
    for element_a in list_a:
        for element_b in list_b:
            if element_a == element_b:
                return True
    return False






