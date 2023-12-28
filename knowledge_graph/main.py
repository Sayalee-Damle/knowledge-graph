import knowledge_graph.backend.create_ontology as ontology
import knowledge_graph.backend.create_graph as create_g
import knowledge_graph.backend.read_graph as read_g

def get_ontology_from_text(text: str):
    table = ontology.return_ontology(text)
    ontology_relations, ontology_terms = ontology.extract_ontology(table)
    G = create_g.create_network(ontology_relations)
    path_fig = create_g.create_subgraph(G)
    read_g.read_all_clusters(path_fig)




    
