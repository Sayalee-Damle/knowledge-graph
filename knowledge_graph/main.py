import knowledge_graph.backend.create_ontology as ontology
import knowledge_graph.backend.create_graph as create_g
import knowledge_graph.backend.read_graph as read_g
from knowledge_graph.configuration.log_factory import logger
import knowledge_graph.backend.qna_service as qna

def get_ontology_from_text(text: str):
    table = ontology.return_ontology(text)
    ontology_relations, ontology_terms = ontology.extract_ontology(table)
    G = create_g.create_network(list(ontology_relations))
    path_description = create_g.create_subgraph(G)
    #read_g.read_all_clusters(path_fig)
    return path_description
    
def qna_bot(text, path_description):
    while True:
        ques = input("Do you have any questions?")
        if ques.lower() in ('y', 'yes'):
            query = input("Question: ")
            ans = qna.return_answer(text, path_description, query)
            print(ans)

        else:
            break




if __name__ == "__main__":
    input_val = """A car, or an automobile, is a motor vehicle with wheels. Most definitions of cars state that they run primarily on roads, seat one to eight people, have four wheels, and mainly transport people, not cargo.[1][2] French inventor Nicolas-Joseph Cugnot built the first steam-powered road vehicle in 1769, while French-born Swiss inventor François Isaac de Rivaz designed and constructed the first internal combustion-powered automobile in 1808.

The modern car—a practical, marketable automobile for everyday use—was invented in 1886, when German inventor Carl Benz patented his Benz Patent-Motorwagen. Commercial cars became widely available during the 20th century. One of the first cars affordable by the masses was the 1908 Model T, an American car manufactured by the Ford Motor Company. Cars were rapidly adopted in the US, where they replaced horse-drawn carriages.[3] In Europe and other parts of the world, demand for automobiles did not increase until after World War II.[4] The car is considered an essential part of the developed economy.

Cars have controls for driving, parking, passenger comfort, and a variety of lamps. Over the decades, additional features and controls have been added to vehicles, making them progressively more complex. These include rear-reversing cameras, air conditioning, navigation systems, and in-car entertainment. Most cars in use in the early 2020s are propelled by an internal combustion engine, fueled by the combustion of fossil fuels. Electric cars, which were invented early in the history of the car, became commercially available in the 2000s and are predicted to cost less to buy than petrol-driven cars before 2025.[5][6] The transition from fossil fuel-powered cars to electric cars features prominently in most climate change mitigation scenarios,[7] such as Project Drawdown's 100 actionable solutions for climate change.[8]

There are costs and benefits to car use. The costs to the individual include acquiring the vehicle, interest payments (if the car is financed), repairs and maintenance, fuel, depreciation, driving time, parking fees, taxes, and insurance.[9] The costs to society include maintaining roads, land use, road congestion, air pollution, noise pollution, public health, and disposing of the vehicle at the end of its life. Traffic collisions are the largest cause of injury-related deaths worldwide.[10] Personal benefits include on-demand transportation, mobility, independence, and convenience.[11] Societal benefits include economic benefits, such as job and wealth creation from the automotive industry, transportation provision, societal well-being from leisure and travel opportunities, and revenue generation from taxes. People's ability to move flexibly from place to place has far-reaching implications for the nature of societies.[12] There are around one billion cars in use worldwide. 
Car usage is increasing rapidly, especially in China, India, and other newly industrialized countries.[13]"""

    #path_desc = get_ontology_from_text(input_val)
    path_desc = r"C:\tmp\graph_desc\graph_desc_da7a5b2c-d182-4afa-b480-e86e347ab0b4.txt"
    print(qna_bot(input_val, path_desc))
    
