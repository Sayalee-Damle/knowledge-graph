from collections import defaultdict
from dataclasses import dataclass
from networkx.classes.graph import Graph
from typing import Union


@dataclass
class MyNode():
    id: str
    visited: bool
    cluster_id: Union[None, int]


def find_subgraphs(network: Graph) -> list[Graph]:
    list_nodes = network.nodes()
    my_nodes = create_my_neighbors(list_nodes)
    
    def visit_nodes(my_graph: list[MyNode], cluster_id: Union[None, int]):
        cluster_counter = 1
        for my_node in my_graph:

            if my_node.visited == False:
                if cluster_id is not None:
                    my_node.cluster_id = cluster_id
                else:
                    my_node.cluster_id = cluster_counter
                    cluster_counter += 1
                my_node.visited = True
                neighbors = list(network.neighbors(my_node.id))
                my_neighbors = [node for node in my_nodes if node.id in neighbors]
                visit_nodes(my_neighbors, my_node.cluster_id)

   
            
    visit_nodes(my_nodes, cluster_id=None)
    cluster_dict = defaultdict(list)
    for node in my_nodes:
        cluster_dict[node.cluster_id].append(node)
    return cluster_dict

def create_my_neighbors(neighbors):
    my_neighbors = [MyNode(id = neighbor, visited = False, cluster_id = None) for neighbor in neighbors]
    return my_neighbors     
    


if __name__ == '__main__':
    mynode = MyNode(id = 'Car', visited = False)
    print(mynode)


