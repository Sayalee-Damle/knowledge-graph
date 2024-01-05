from pathlib import Path
import knowledge_graph.backend.create_ontology as ontology
import knowledge_graph.backend.create_graph as create_g
import knowledge_graph.backend.read_graph as read_g
from knowledge_graph.configuration.log_factory import logger
import knowledge_graph.backend.qna_service as qna
import knowledge_graph.services.vector_db as v_db
import knowledge_graph.frontend.text_finder as chk_inp


def get_ontology_from_text(text: str):
    """give knowledge graphs of given text. Build ontologies. write summary and save to file
    Returns: path of the text file containing summary"""
    if not chk_inp.check_if_text_exists(text):
        table = ontology.return_ontology(text)
        ontology_relations, ontology_terms = ontology.extract_ontology(table)
        G = create_g.create_network(list(ontology_relations))
        path_description = create_g.create_subgraph(G)
        # read_g.read_all_clusters(path_fig)
        chk_inp.put_into_directory(text)
        db_text = v_db.create_embeddings_text(text)
        db_summary = v_db.create_embeddings_summary(Path(path_description))
    
    qna_bot()



async def qna_bot():
    """Input: input text and the path of the .txt file of the summary
    Returns: Answer to user question"""
    while True:
        ques = input("Do you have any questions?[yes/no]: ")
        if ques.lower() in ("y", "yes"):
            query = input("Question: ")
            ans = await qna.return_answer(query)
            print(ans)

        else:
            break


if __name__ == "__main__":
    input_val = """Animals are the most adorable and loving creatures existing on Earth. They might not be able to speak, but they can understand. They have a unique mode of interaction which is beyond human understanding. There are two types of animals: domestic and wild animals.

Domestic Animals | Domestic animals such as dogs, cows, cats, donkeys, mules and elephants are the ones which are used for the purpose of domestication. Wild animals refer to animals that are not normally domesticated and generally live in forests. They are important for their economic, survival, beauty, and scientific value.

Wild Animals | Wild animals provide various useful substances and animal products such as honey, leather, ivory, tusk, etc. They are of cultural asset and aesthetic value to humankind. Human life largely depends on wild animals for elementary requirements like the medicines we consume and the clothes we wear daily.

Nature and wildlife are largely associated with humans for several reasons, such as emotional and social issues. The balanced functioning of the biosphere depends on endless interactions among microorganisms, plants and animals. This has led to countless efforts by humans for the conservation of animals and to protect them from extinction. Animals have occupied a special place of preservation and veneration in various cultures worldwide."""
    
    input_val_2 = """Pollution affects the quality of life more than one can imagine. It works in mysterious ways, sometimes which cannot be seen by the naked eye. However, it is very much present in the environment. For instance, you might not be able to see the natural gases present in the air, but they are still there. Similarly, the pollutants which are messing up the air and increasing the levels of carbon dioxide is very dangerous for humans. Increased level of carbon dioxide will lead to global warming.

Further, the water is polluted in the name of industrial development, religious practices and more will cause a shortage of drinking water. Without water, human life is not possible. Moreover, the way waste is dumped on the land eventually ends up in the soil and turns toxic. If land pollution keeps on happening at this rate, we won’t have fertile soil to grow our crops on. Therefore, serious measures must be taken to reduce pollution to the core."""
    path_desc = get_ontology_from_text(input_val_2)
    #path_desc = r"C:\tmp\graph_desc\graph_desc_da7a5b2c-d182-4afa-b480-e86e347ab0b4.txt"
