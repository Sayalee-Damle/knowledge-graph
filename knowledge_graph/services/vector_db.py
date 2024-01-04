from pathlib import Path
from uuid import uuid4
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import LanceDB

import lancedb
from knowledge_graph.configuration.config import cfg
from lancedb import DBConnection

def check_if_embedding_exists(text: str):
    db = lancedb.connect(cfg.db_path)
    tbl_text = db.open_table("knowledge_graph_text")
    df = tbl_text.search(text).to_pandas(flatten=True)
    print(df.text)
    if text in df.text.values.astype(str):
        return True
    else:
        return False

def create_embeddings_text(text: str):
    db = lancedb.connect(cfg.db_path)
    table_text = db.create_table(
        name=f"knowledge_graph_text",
        data=[
            {
                "vector": cfg.emb_func.embed_query("Placeholder"),
                "text": "Placeholder",
                "id": "1",
            }
        ],
        mode="overwrite",
    )
    
    text_splitter = CharacterTextSplitter(chunk_size=cfg.chunk_size, chunk_overlap=0)
    documents = text_splitter.split_text(text)
    db_text = LanceDB.from_texts(documents, cfg.emb_func, connection=table_text)
    return db_text
    

def create_embeddings_summary(summary_path: Path):
    db = lancedb.connect(cfg.db_path)
   
    table_summary = db.create_table(
        name=f"knowledge_graph_summary",
        data=[
            {
                "vector": cfg.emb_func.embed_query("Placeholder"),
                "text": "Placeholder",
                "id": "1",
            }
        ],
        mode="overwrite",
    )

    loader = TextLoader(summary_path.as_posix())
    docs_summary = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=cfg.chunk_size, chunk_overlap=0)
    doc = text_splitter.split_documents(docs_summary)
    db_summary = LanceDB.from_documents(doc, cfg.emb_func, connection=table_summary)
    return db_summary




def similarity_search(query: str):
    db = lancedb.connect(cfg.db_path)
    tbl_text = db.open_table("knowledge_graph_text")
    tbl_summary = db.open_table("knowledge_graph_summary")

    vectorstore_text = LanceDB(tbl_text, cfg.emb_func)
    result_text = vectorstore_text.similarity_search(query)
    ans_text = result_text[0].page_content
 
    vectorstore_summary = LanceDB(tbl_summary, cfg.emb_func)
    result_summary = vectorstore_summary.similarity_search(query)
    ans_summary = result_summary[0].page_content

    return ans_text, ans_summary


if __name__ == "__main__":
    input_val = """Animals are the most adorable and loving creatures existing on Earth. They might not be able to speak, but they can understand. They have a unique mode of interaction which is beyond human understanding. There are two types of animals: domestic and wild animals.

Domestic Animals | Domestic animals such as dogs, cows, cats, donkeys, mules and elephants are the ones which are used for the purpose of domestication. Wild animals refer to animals that are not normally domesticated and generally live in forests. They are important for their economic, survival, beauty, and scientific value.

Wild Animals | Wild animals provide various useful substances and animal products such as honey, leather, ivory, tusk, etc. They are of cultural asset and aesthetic value to humankind. Human life largely depends on wild animals for elementary requirements like the medicines we consume and the clothes we wear daily.

Nature and wildlife are largely associated with humans for several reasons, such as emotional and social issues. The balanced functioning of the biosphere depends on endless interactions among microorganisms, plants and animals. This has led to countless efforts by humans for the conservation of animals and to protect them from extinction. Animals have occupied a special place of preservation and veneration in various cultures worldwide."""

    print(check_if_embedding_exists(input_val))
    #path = Path(r"C:\tmp\graph_desc\graph_desc_310150f8-a4a8-4ba9-b1c7-07bc5b4944d1.txt")
    #db = create_embeddings_summary(path)
    #print(db)
