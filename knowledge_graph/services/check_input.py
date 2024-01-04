import os
from uuid import uuid4
from knowledge_graph.configuration.config import cfg


def put_into_directory(input_text: str):
    input_path = cfg.graph_input_path
    with open(input_path/f"{uuid4()}.txt") as f:
        f.write(input_text)

def check_if_text_exists(input_text: str):
    graph_input_dir = cfg.graph_input_path
    for root, dirs, files in os.walk(graph_input_dir):
        for folder in files:
            name = root + "\\" + str(folder)
            print(name)
            f = open(name, "r")
            text_file = f.read()
            if text_file == input_text:
                return True
            else:
                continue
    return False