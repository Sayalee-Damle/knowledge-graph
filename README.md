## Description

This tool will create knowledge graphs
## Installation instructions


```
conda create -n knowledge_graph python=3.12
conda activate knowledge_graph
pip install poetry if this doesn't work use : pip install poetry --user
poetry install
```
This creates a specific environment with all the libraries in need!



## to start the chatbot





## Configuration
configure the .env file might like this:
To specify configurations use .env file

```
OPENAI_API_KEY= openai key
OPENAI_MODEL = gpt-4-1106-preview
CHUNK_SIZE = 1000
REQUEST_TIMEOUT = 300
SEED = 42
TEMPERATURE = 0
MAX_AUTO_REPLY = 4
CODE_DIR = /tmp/graph_desc
SAVE_FIG = /tmp/subgraphs
LLM_CACHE = False
LANGCHAIN_DEBUG = True

```
