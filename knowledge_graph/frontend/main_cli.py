from pathlib import Path
import knowledge_graph.backend.create_ontology as ontology
import knowledge_graph.backend.create_graph as create_g
import knowledge_graph.backend.read_graph as read_g
from knowledge_graph.configuration.log_factory import logger
import knowledge_graph.backend.qna_service as qna


def get_ontology_from_text(text: str):
    """give knowledge graphs of given text. Build ontologies. write summary and save to file
    Returns: path of the text file containing summary"""

    table = ontology.return_ontology(text)
    ontology_relations, ontology_terms = ontology.extract_ontology(table)
    G = create_g.create_network(list(ontology_relations))
    path_description = create_g.create_subgraph(G)
    # read_g.read_all_clusters(path_fig)
    return Path(path_description)


def qna_bot(text: str, path_description: Path):
    """Input: input text and the path of the .txt file of the summary
    Returns: Answer to user question"""
    while True:
        ques = input("Do you have any questions?[yes/no]: ")
        if ques.lower() in ("y", "yes"):
            query = input("Question: ")
            ans = qna.return_answer(text, path_description, query)
            print(ans)

        else:
            break


if __name__ == "__main__":
    input_val = """Animals are the most adorable and loving creatures existing on Earth. They might not be able to speak, but they can understand. They have a unique mode of interaction which is beyond human understanding. There are two types of animals: domestic and wild animals.

Domestic Animals | Domestic animals such as dogs, cows, cats, donkeys, mules and elephants are the ones which are used for the purpose of domestication. Wild animals refer to animals that are not normally domesticated and generally live in forests. They are important for their economic, survival, beauty, and scientific value.

Wild Animals | Wild animals provide various useful substances and animal products such as honey, leather, ivory, tusk, etc. They are of cultural asset and aesthetic value to humankind. Human life largely depends on wild animals for elementary requirements like the medicines we consume and the clothes we wear daily.

Nature and wildlife are largely associated with humans for several reasons, such as emotional and social issues. The balanced functioning of the biosphere depends on endless interactions among microorganisms, plants and animals. This has led to countless efforts by humans for the conservation of animals and to protect them from extinction. Animals have occupied a special place of preservation and veneration in various cultures worldwide."""
    path_desc = get_ontology_from_text(input_val)
    #path_desc = r"C:\tmp\graph_desc\graph_desc_da7a5b2c-d182-4afa-b480-e86e347ab0b4.txt"
    print(qna_bot(input_val, path_desc))
