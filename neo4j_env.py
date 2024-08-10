from dotenv import load_dotenv
import os
from langchain_community.graphs import Neo4jGraph
load_dotenv('.env', override=True)
# Warning control
import warnings
warnings.filterwarnings("ignore")

NEO4J_URI = os.getenv('NEO4J_URI')
NEO4J_USERNAME = os.getenv('NEO4J_USERNAME')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')
NEO4J_DATABASE = os.getenv('NEO4J_DATABASE')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_ENDPOINT = os.getenv('OPENAI_BASE_URL') + '/embeddings'



# Global constants
VECTOR_INDEX_NAME = 'NapoleonOpenAI'
VECTOR_NODE_LABEL = 'Napoleon_Chunk'
VECTOR_SOURCE_PROPERTY = 'text'
VECTOR_EMBEDDING_PROPERTY = 'textEmbeddingOpenAI'


graph = Neo4jGraph(
    url=NEO4J_URI, username=NEO4J_USERNAME, password=NEO4J_PASSWORD, database=NEO4J_DATABASE
)