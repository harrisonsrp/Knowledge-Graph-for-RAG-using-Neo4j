from langchain_community.graphs import Neo4jGraph
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import GraphCypherQAChain
from neo4j_env import graph
import textwrap

retrieval_qa_chat_prompt = """
Task:Generate Cypher statement to 
query a graph database.
Instructions:
Use only the provided relationship types and properties in the 
schema. Do not use any other relationship types or properties that
are not provided.
Remember the relationships are like Schema:
{schema}
if question say Talleyrand it menas Charles-Maurice de Talleyrand 
and if say Napoleon means Napoleon Bonaparte and if say waterloo is Battle of Waterloo.

Note: Do not include any explanations or apologies in your responses.
Do not include any text except the generated Cypher statement. Remember to correct the typo in names

Example 1: What was the story of napoleon in the battle of waterloo?
MATCH (Napoleon:Person)-[:RELATED_TO]->(waterloo:Event)-[:HAS_General_INFO]->(info:General_info)-[:HAS_Chunk_INFO]->(ChunkInfo:Waterloo_Chunk)
RETURN p, e, info, ChunkInfo.text

Example 2: What was the story of the battle of waterloo?
MATCH (waterloo:Event)-[:HAS_General_INFO]->(info:General_info)-[:HAS_Chunk_INFO]->(ChunkInfo:Waterloo_Chunk)
RETURN p, e, info, ChunkInfo.text

Example 3: tell me about Talleyrand and napoleon in 5 lines
MATCH (Talleyrand:Person)-[:RELATED_TO]->(Napoleon:Person)-[:HAS_Career_INFO]->(info:Career_info)-[:HAS_Chunk_INFO]->(ChunkInfo:Napoleon_Chunk)
RETURN Talleyrand, Napoleon

The question is:
{question}

"""


class GraphRAG:
    def __init__(self):
        self.cypher_prompt = PromptTemplate(
            input_variables=["schema", "question"],
            template= retrieval_qa_chat_prompt
        )
        self.cypher_chain = GraphCypherQAChain.from_llm(
            ChatOpenAI(temperature=0),
            graph=graph,
            verbose=True,
            cypher_prompt=self.cypher_prompt,
        )

    def generate_cypher_query(self, question: str) -> str:
        response = self.cypher_chain.run(question)
        return textwrap.fill(response, 60)