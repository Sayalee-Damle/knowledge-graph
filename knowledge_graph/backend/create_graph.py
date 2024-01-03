import shutil
from typing import List
import networkx as nx
import matplotlib.pyplot as plt
from itertools import chain
from uuid import uuid4

import knowledge_graph.backend.create_ontology as ontology
from knowledge_graph.configuration.config import cfg
import knowledge_graph.backend.create_subgraphs as subg
import knowledge_graph.backend.read_graph as read_g
from knowledge_graph.backend.model import Ontology, OntologyRelation
import knowledge_graph.backend.create_subgraphs as subg

def create_network(ontology_relations: List[Ontology]):
    G = nx.Graph()
    for i in ontology_relations:
        src = i.source
        target = i.target
        attribute = i.relation_name
        G.add_edge(src, target, edge_labels=attribute)
    return G



def create_subgraph(G):
    path_desc = cfg.desc_dir/f"graph_desc_{uuid4()}.txt"
    dict_graphs = subg.find_subgraphs(G)
    print(dict_graphs)
    options = {
        "node_color": "none",
        "node_size": 100,
        "node_shape": "s",
        "width": 3,
        "arrowstyle": "-|>",
        "arrowsize": 12,
        "arrows": True,
        "font_size": 8,
    }
    path_fig = cfg.save_fig_path
    if path_fig.exists():
        shutil.rmtree(path_fig)
    path_fig.mkdir(parents=True)
    for k, v in dict_graphs.items():
        
        print(k)
        print("in for")
        H = G.subgraph([node.id for node in v])

        print(path_fig)
        
        path_subg = path_fig / f"subgraph_{k}.gefx"
        nx.write_gexf(H, path_subg)
        
        try:
            read_g.save_description(path_subg, path_desc)
        except:
            pass
    return path_desc
        # plt.show()


if __name__ == "__main__":
    import create_subgraphs as subg

    
    lst = [OntologyRelation(source='Car', target='Motor vehicle', relation_name='is_a'), OntologyRelation(source='Car', target='Wheels', relation_name='has'), OntologyRelation(source='Car', target='Roads', relation_name='runs_on'), OntologyRelation(source='Car', target='People', relation_name='transports'), OntologyRelation(source='Nicolas-Joseph Cugnot', target='Steam-powered road vehicle', relation_name='built'), OntologyRelation(source='François Isaac de Rivaz', target='Internal combustion-powered automobile', relation_name='designed_and_constructed'), OntologyRelation(source='Carl Benz', target='Benz Patent-Motorwagen', relation_name='invented'), OntologyRelation(source='Commercial cars', target='20th century', relation_name='became_widely_available_in'), OntologyRelation(source='Model T', target='Masses', relation_name='affordable_by'), OntologyRelation(source='Model T', target='Ford Motor Company', relation_name='manufactured_by'), OntologyRelation(source='Cars', target='US', relation_name='adopted_in'), OntologyRelation(source='Cars', target='Horse-drawn carriages', relation_name='replaced'), OntologyRelation(source='Cars', target='World War II', relation_name='demand_increased_after'), OntologyRelation(source='Cars', target='Developed economy', relation_name='considered_essential_part_of'), OntologyRelation(source='Cars', target='Driving', relation_name='have_controls_for'), OntologyRelation(source='Cars', target='Parking', relation_name='have_controls_for'), OntologyRelation(source='Cars', target='Passenger comfort', relation_name='have_controls_for'), OntologyRelation(source='Cars', target='Lamps', relation_name='have_variety_of'), OntologyRelation(source='Cars', target='Vehicles', relation_name='became_more_complex'), OntologyRelation(source='Cars', target='Rear-reversing cameras', relation_name='include'), OntologyRelation(source='Cars', target='Air conditioning', relation_name='include'), OntologyRelation(source='Cars', target='Navigation systems', relation_name='include'), OntologyRelation(source='Cars', target='In-car entertainment', relation_name='include'), OntologyRelation(source='Cars', target='Internal combustion engine', relation_name='propelled_by'), OntologyRelation(source='Cars', target='Fossil fuels', relation_name='fueled_by'), OntologyRelation(source='Electric cars', target='2000s', relation_name='became_commercially_available_in'), OntologyRelation(source='Electric cars', target='Petrol-driven cars', relation_name='predicted_to_cost_less_than_before_2025'), OntologyRelation(source='Electric cars', target='Climate change mitigation', relation_name='features_prominently_in'), OntologyRelation(source='Car use', target='Individual', relation_name='costs_to'), OntologyRelation(source='Car use', target='Society', relation_name='costs_to'), OntologyRelation(source='Individual', target='Vehicle', relation_name='acquiring'), OntologyRelation(source='Individual', target='Interest payments', relation_name='includes'), OntologyRelation(source='Individual', target='Repairs and maintenance', relation_name='includes'), OntologyRelation(source='Individual', target='Fuel', relation_name='includes'), OntologyRelation(source='Individual', target='Depreciation', relation_name='includes'), OntologyRelation(source='Individual', target='Driving time', relation_name='includes'), OntologyRelation(source='Individual', target='Parking fees', relation_name='includes'), OntologyRelation(source='Individual', target='Taxes', relation_name='includes'), OntologyRelation(source='Individual', target='Insurance', relation_name='includes'), OntologyRelation(source='Society', target='Roads', relation_name='maintaining'), OntologyRelation(source='Society', target='Land use', relation_name='includes'), OntologyRelation(source='Society', target='Road congestion', relation_name='includes'), OntologyRelation(source='Society', target='Air pollution', relation_name='includes'), OntologyRelation(source='Society', target='Noise pollution', relation_name='includes'), OntologyRelation(source='Society', target='Public health', relation_name='includes'), OntologyRelation(source='Society', target='Vehicle disposal', relation_name='includes'), OntologyRelation(source='Traffic collisions', target='Injury-related deaths', relation_name='largest_cause_of'), OntologyRelation(source='Car use', target='On-demand transportation', relation_name='provides_personal_benefit'), OntologyRelation(source='Car use', target='Mobility', relation_name='provides_personal_benefit'), OntologyRelation(source='Car use', target='Independence', relation_name='provides_personal_benefit'), OntologyRelation(source='Car use', target='Convenience', relation_name='provides_personal_benefit'), OntologyRelation(source='Car use', target='Economic benefits', relation_name='provides_societal_benefit'), OntologyRelation(source='Car use', target='Transportation provision', relation_name='provides_societal_benefit'), OntologyRelation(source='Car use', target='Societal well-being', relation_name='provides_societal_benefit'), OntologyRelation(source='Car use', target='Revenue generation', relation_name='provides_societal_benefit'), OntologyRelation(source='People', target='Place to place', relation_name='move_flexibly_from'), OntologyRelation(source='Car usage', target='China', relation_name='increasing_rapidly_in'), OntologyRelation(source='Car usage', target='India', relation_name='increasing_rapidly_in'), OntologyRelation(source='Car usage', target='Newly industrialized countries', relation_name='increasing_rapidly_in')]
    G = create_network(lst)
    print(G.nodes)
    path_fig = create_subgraph(G)
    print(path_fig)
    """u_lst = unique_src(lst)
    # print(u_lst)
    src_lst = source_dict(u_lst, lst)
    # print(src_lst)
    
    dict_graphs = subg.find_subgraphs(G)
    print(dict_graphs)
    path_fig = create_subgraph(G)

   

    #H = create_subgraph(G, u_lst, src_lst)
    """options = {
    'node_color':"none",
    'node_size': 100,
    'node_shape':"s",
    'width': 3,
    'arrowstyle': '-|>',
    'arrowsize': 12,
    'arrows' : True,
    'font_size': 8
}
    print(type(G))
    for n in G.neighbors('Car'):
        print(n, type(n))
        """
    for k, v in dict_graphs.items():
        print("in for")
        H = G.subgraph([node.id for node in v])
        nx.draw(H, with_labels=True, **options, bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=1'))
        plt.show()
        nx.draw(
            H,
            with_labels=True,
            **options,
            bbox=dict(facecolor="none", edgecolor="black", boxstyle="round,pad=1"),
        )
"""