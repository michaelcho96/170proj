import networkx as nx
from functools import wraps
import errno
import os
import signal
from best_solutions import write_file
from collections import defaultdict

solved_instance_list = [1, 3, 5, 6, 9, 10, 21, 23, 25, 27, 28, 31, 32, 33, 36, 41, 42, 43,
                        44, 52, 55, 64, 67, 72, 77, 78, 80, 82, 86, 92, 95, 96, 97, 99, 100,
                        101, 112, 115, 116, 119, 121, 142, 152, 163, 174, 186, 192, 199, 214,
                        223, 231, 233, 245, 247, 265, 267, 272, 275, 278, 280, 294, 298, 300,
                        309, 326, 328, 337, 342, 355, 362, 364, 375, 376, 385, 410, 425, 428,
                        444, 447, 450, 452, 466, 471, 473, 488]

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


""" INSTANCE: File name containing instance of problem
    Parses file, returns a networkx Digraph object
    Nodes have 'penalty' attributes: 1 for adults, 2 for children. """
def create_graph(instance):
    
    with open(instance) as f:
        n = int(f.readline())
        children_line = f.readline()
        if children_line != "\n":
            children = children_line.split()
            # print(children)
        else: 
            children = []
        g = nx.DiGraph()
        g.add_nodes_from(range(n), penalty=1)
        for c in children:
            if c == "\n" or c == " ":
                pass
            elif type(c) == int:
                g.node[c]['penalty'] = 2
            elif type(c) == str:
                g.node[int(c.strip())]['penalty'] = 2
        for i in range(n):
            row = f.readline()
            elements = row.split()
            # print(elements)
            for j in range(n):
                if "1" in elements[j]:
                    g.add_edge(i,j)
        # print("num edges: " + str(len(nx.edges(g))))
    return g

""" DO NOT USE: RUNTIME |V|^6 """
def find_cycles(input_graph):
    G = input_graph.copy()
    cycle_list = []
    list_nodes = G.nodes()
    for node in list_nodes:
        print("searching node " + str(node))
        cycle_list.extend(_explore2(node, node, G, [node]))
        G.remove_node(node)
    return cycle_list

def _explore(node, input_graph, counter):
    cycle_list = []
    node_previsit = counter
    G.node[node]['pre-visit'] = node_previsit
    counter += 1
    for edge in input_graph.edges(node, False):
        next_vertex = edge[1]
        if G.node[next_vertex]['pre-visit'] < node_previsit:
            # We explore for cycles
            # Place code here
            print("error: need code")
        cycles_list.extend(__explore(next_vertex))

def _explore2(root_node, node, input_graph, path):
    cycle_list = []
    if len(path) == 6: # If the path already has six vertices, then there is no valid cycle
        return cycle_list
    for edge in input_graph.edges(node, False):
        next_node = edge[1]
        if next_node == root_node:
            cycle_list.append(path)
        else:
            updated_path = list(path)
            updated_path.append(next_node)
            updated_graph = input_graph.copy()
            if node != root_node:
                updated_graph.remove_node(node)
            cycle_list.extend(_explore2(root_node, next_node, updated_graph, updated_path)) # Recursive call
    return cycle_list


        
""" Constructs an undirected graph of all valid cycles, with an edge between two nodes
   of the graph if the underlying cycles share at least one vertex """
def construct_cluster_graph(G):
    list_cycles = list(modified_simple_cycles(G))
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

""" Helper function for construct_cluster_graph() """
def contain_same_element(list_a, list_b):
    for element_a in list_a:
        for element_b in list_b:
            if element_a == element_b:
                return True
    return False

"""Takes in a list of cycles and outputs a submittable format """
def format_output_cycles(cycle_list):
    output_string = ""
    for cycle in cycle_list:
        for node in cycle:
            output_string += str(node)
            output_string += " "
        output_string = output_string[0:len(output_string) - 1]
        output_string = output_string + "; "
    output_string = output_string[0:len(output_string) - 2]
    return output_string

def find_total_penalty(G):
    penalty = 0
    for node in G.nodes():
        penalty += G.node[node]['penalty']
    return penalty


def add_solutions(list_solutions):
    write_file(list_solutions)

def validate_formatted_solution(solution):
    cycle_list = []
    used_nodes = []
    cycle_tokens = solution.split(";")
    for node_tokens in cycle_tokens:
        cycle = []
        node_token = node_tokens.split(" ")
        for node in node_token:
            if node != '' and node != '\n':
                if int(node) in used_nodes:
                    print("repeat node")
                    return False
                cycle.append(int(node))
                used_nodes.append(int(node))
        if len(cycle) < 2:
            print("cycle of length 1")
            return False
        cycle_list.append(cycle)
    for cycle in cycle_list:
        if len(cycle) > 5:
            return False
    return True

def comprehensive_solution_validation(solution, G):
    if not validate_formatted_solution(solution):
        return False
    else:
        solution = solution.replace('\n', "")
        solution = solution.replace('', "")
        #print("solution: " + solution)
        list_cycles = solution.split(";")

        # Each token in tokens1 is a list of cycles
        for cycle in list_cycles:
            # each token in tokens2 is a node
            nodes = cycle.split(" ")
            list_nodes = []
            for node in nodes:
                if node != '' and node != '\n':
                    list_nodes.append(node)
            #print("list_nodes: " + str(list_nodes))
            for index in range(0, len(list_nodes)):
                edge_to_check = ()
                if index == len(list_nodes) - 1:
                    edge_to_check = (int(list_nodes[index]), int(list_nodes[0]))
                else:
                    edge_to_check = (int(list_nodes[index]), int(list_nodes[index + 1]))
                #print("Checking: " + str(edge_to_check))
                if not contains_edge(G, edge_to_check):
                 #   print("Contains edge not in graph.")
                    return False
    return True

def contains_edge(G, input_edge):
    for edge in G.edges():
        if edge == input_edge:
            return True
    return False

def condensed_list(solved_instance_list):
    instance_list = []
    for index in range(1,293):
        if not index in solved_instance_list:
            instance_list.append(index)
    return instance_list

def read_solution_line(line):
    instance_tokens = line.split(":")
    type_tokens = line.split(",")
    tokens = line.split("|")
    #Finding instance number
    instance_number = int(instance_tokens[0])
    #FInding algorithm
    type_token2 = type_tokens[0].split(" ")
    algorithm_type = type_token2[1]
    #Finding penalty
    penalty = int(tokens[1])
    #Finding solution
    solution = tokens[2]
    solution = solution.replace('\n', "")
    solution = solution.replace('', "")
    return [instance_number, algorithm_type, penalty, solution]

def simple_k_cycles(G, k):
    """Find simple cycles (elementary circuits) of a directed graph.
    An simple cycle, or elementary circuit, is a closed path where no
    node appears twice, except that the first and last node are the same.
    Two elementary circuits are distinct if they are not cyclic permutations
    of each other.
    This is a nonrecursive, iterator/generator version of Johnson's
    algorithm [1]_.  There may be better algorithms for some cases [2]_ [3]_.
    Parameters
    ----------
    G : NetworkX DiGraph
       A directed graph
    Returns
    -------
    cycle_generator: generator
       A generator that produces elementary cycles of the graph.  Each cycle is
       a list of nodes with the first and last nodes being the same.
    Examples
    --------
    >>> G = nx.DiGraph([(0, 0), (0, 1), (0, 2), (1, 2), (2, 0), (2, 1), (2, 2)])
    >>> len(list(nx.simple_cycles(G)))
    5
    To filter the cycles so that they don't include certain nodes or edges,
    copy your graph and eliminate those nodes or edges before calling
    >>> copyG = G.copy()
    >>> copyG.remove_nodes_from([1])
    >>> copyG.remove_edges_from([(0, 1)])
    >>> len(list(nx.simple_cycles(copyG)))
    3
    Notes
    -----
    The implementation follows pp. 79-80 in [1]_.
    The time complexity is `O((n+e)(c+1))` for `n` nodes, `e` edges and `c`
    elementary circuits.
    References
    ----------
    .. [1] Finding all the elementary circuits of a directed graph.
       D. B. Johnson, SIAM Journal on Computing 4, no. 1, 77-84, 1975.
       http://dx.doi.org/10.1137/0204007
    .. [2] Enumerating the cycles of a digraph: a new preprocessing strategy.
       G. Loizou and P. Thanish, Information Sciences, v. 27, 163-182, 1982.
    .. [3] A search strategy for the elementary cycles of a directed graph.
       J.L. Szwarcfiter and P.E. Lauer, BIT NUMERICAL MATHEMATICS,
       v. 16, no. 2, 192-204, 1976.
    See Also
    --------
    cycle_basis
    """
    """
    def _unblock(thisnode,blocked,B):
        stack=set([thisnode])
        while stack:
            node=stack.pop()
            if node in blocked:
                blocked.remove(node)
                stack.update(B[node])
                B[node].clear()

    # Johnson's algorithm requires some ordering of the nodes.
    # We assign the arbitrary ordering given by the strongly connected comps
    # There is no need to track the ordering as each node removed as processed.
    subG = type(G)(G.edges_iter()) # save the actual graph so we can mutate it here
                              # We only take the edges because we do not want to
                              # copy edge and node attributes here.
    sccs = list(nx.strongly_connected_components(subG))
    while sccs:
        scc=sccs.pop()
        # order of scc determines ordering of nodes
        startnode = scc.pop()
        # Processing node runs "circuit" routine from recursive version
        path=[startnode]
        blocked = set() # vertex: blocked from search?
        closed = set() # nodes involved in a cycle
        blocked.add(startnode)
        B=defaultdict(set) # graph portions that yield no elementary circuit
        stack=[ (startnode,list(subG[startnode])) ]  # subG gives component nbrs
        while stack:
            if len(path) > k:
                break
            thisnode,nbrs = stack[-1]
            if nbrs:
                nextnode = nbrs.pop()
#                    print thisnode,nbrs,":",nextnode,blocked,B,path,stack,startnode
#                    f=raw_input("pause")
                if nextnode == startnode:
                    yield path[:]
                    closed.update(path)
#                        print "Found a cycle",path,closed
                elif nextnode not in blocked:
                    path.append(nextnode)
                    stack.append( (nextnode,list(subG[nextnode])) )
                    closed.discard(nextnode)
                    blocked.add(nextnode)
                    continue
            # done with nextnode... look for more neighbors
            if not nbrs:  # no more nbrs
                if thisnode in closed:
                    _unblock(thisnode,blocked,B)
                else:
                    for nbr in subG[thisnode]:
                        if thisnode not in B[nbr]:
                            B[nbr].add(thisnode)
                stack.pop()
#                assert path[-1]==thisnode
                path.pop()
        # done processing this node
        subG.remove_node(startnode)
        H=subG.subgraph(scc)  # make smaller to avoid work in SCC routine
        sccs.extend(list(nx.strongly_connected_components(H))) """

def modified_simple_cycles(G):
    """Find simple cycles (elementary circuits) of a directed graph.

    An simple cycle, or elementary circuit, is a closed path where no
    node appears twice, except that the first and last node are the same.
    Two elementary circuits are distinct if they are not cyclic permutations
    of each other.

    This is a nonrecursive, iterator/generator version of Johnson's
    algorithm [1]_.  There may be better algorithms for some cases [2]_ [3]_.

    Parameters
    ----------
    G : NetworkX DiGraph
       A directed graph

    Returns
    -------
    cycle_generator: generator
       A generator that produces elementary cycles of the graph.  Each cycle is
       a list of nodes with the first and last nodes being the same.

    Examples
    --------
    >>> G = nx.DiGraph([(0, 0), (0, 1), (0, 2), (1, 2), (2, 0), (2, 1), (2, 2)])
    >>> list(nx.simple_cycles(G))
    [[2], [2, 1], [2, 0], [2, 0, 1], [0]]

    Notes
    -----
    The implementation follows pp. 79-80 in [1]_.

    The time complexity is O((n+e)(c+1)) for n nodes, e edges and c
    elementary circuits.

    To filter the cycles so that they don't include certain nodes or edges,
    copy your graph and eliminate those nodes or edges before calling.
    >>> copyG = G.copy()
    >>> copyG.remove_nodes_from([1])
    >>> copyG.remove_edges_from([(0,1)])
    >>> list(nx.simple_cycles(copyG))
    [[2], [2, 0], [0]]

    References
    ----------
    .. [1] Finding all the elementary circuits of a directed graph.
       D. B. Johnson, SIAM Journal on Computing 4, no. 1, 77-84, 1975.
       http://dx.doi.org/10.1137/0204007

    .. [2] Enumerating the cycles of a digraph: a new preprocessing strategy.
       G. Loizou and P. Thanish, Information Sciences, v. 27, 163-182, 1982.

    .. [3] A search strategy for the elementary cycles of a directed graph.
       J.L. Szwarcfiter and P.E. Lauer, BIT NUMERICAL MATHEMATICS,
       v. 16, no. 2, 192-204, 1976.

    See Also
    --------
    cycle_basis
    """
    def _unblock(thisnode,blocked,B):
        stack=set([thisnode])
        while stack:
            node=stack.pop()
            if node in blocked:
                blocked.remove(node)
                stack.update(B[node])
                B[node].clear()

    # Johnson's algorithm requires some ordering of the nodes.
    # We assign the arbitrary ordering given by the strongly connected comps
    # There is no need to track the ordering as each node removed as processed.
    subG = type(G)(G.edges_iter()) # save the actual graph so we can mutate it here
                              # We only take the edges because we do not want to
                              # copy edge and node attributes here.
    sccs = list(nx.strongly_connected_components(subG))
    while sccs:
        scc=sccs.pop()
        # order of scc determines ordering of nodes
        startnode = scc.pop()
        # Processing node runs "circuit" routine from recursive version
        path=[startnode]
        blocked = set() # vertex: blocked from search?
        closed = set() # nodes involved in a cycle
        blocked.add(startnode)
        B=defaultdict(set) # graph portions that yield no elementary circuit
        stack=[ (startnode,list(subG[startnode])) ]  # subG gives component nbrs
        while stack:
            if len(path) > 5:
                break
            thisnode,nbrs = stack[-1]
            if nbrs:
                nextnode = nbrs.pop()
#                    print thisnode,nbrs,":",nextnode,blocked,B,path,stack,startnode
#                    f=raw_input("pause")
                if nextnode == startnode and len(path) <= 5:
                    yield path[:]
                    closed.update(path)
#                        print "Found a cycle",path,closed
                elif nextnode not in blocked:
                    path.append(nextnode)
                    stack.append( (nextnode,list(subG[nextnode])) )
                    closed.discard(nextnode)
                    blocked.add(nextnode)
                    continue
            # done with nextnode... look for more neighbors
            if not nbrs:  # no more nbrs
                if thisnode in closed:
                    _unblock(thisnode,blocked,B)
                else:
                    for nbr in subG[thisnode]:
                        if thisnode not in B[nbr]:
                            B[nbr].add(thisnode)
                stack.pop()
#                assert path[-1]==thisnode
                path.pop()
        # done processing this node
        subG.remove_node(startnode)
        H=subG.subgraph(scc)  # make smaller to avoid work in SCC routine
        sccs.extend(list(nx.strongly_connected_components(H)))

