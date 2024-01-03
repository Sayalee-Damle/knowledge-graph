from pathlib import Path
from uuid import uuid4
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import LanceDB

import lancedb
from knowledge_graph.configuration.config import cfg
from lancedb import DBConnection


def create_embeddings(text: str):
    db = lancedb.connect(cfg.db_path)
    table = db.create_table(
        name=f"knowledge_graph_info",
        data=[
            {
                "vector": cfg.emb_func.embed_query("Hello World"),
                "text": "Hello World",
                "id": "1",
            }
        ],
        mode="overwrite",
    )

    text_splitter = CharacterTextSplitter(chunk_size=cfg.chunk_size, chunk_overlap=0)
    documents = text_splitter.split_text(text)
    db = LanceDB.from_texts(documents, cfg.emb_func, connection=table)
    return db


def similarity_search(db: DBConnection, query: str):
    docs = db.similarity_search(query)
    return docs[0].page_content
