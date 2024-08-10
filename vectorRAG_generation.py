from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Neo4jVector
import textwrap
from langchain_openai import ChatOpenAI
from neo4j_env import *

class VectorRAG:
    def __init__(self):
        self.vector_store = Neo4jVector.from_existing_graph(
            embedding=OpenAIEmbeddings(),
            url=NEO4J_URI,
            username=NEO4J_USERNAME,
            password=NEO4J_PASSWORD,
            index_name=VECTOR_INDEX_NAME,
            node_label=VECTOR_NODE_LABEL,
            text_node_properties=[VECTOR_SOURCE_PROPERTY],
            embedding_node_property=VECTOR_EMBEDDING_PROPERTY,
        )

        self.retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
        self.combine_docs_chain = create_stuff_documents_chain(ChatOpenAI(temperature=0), self.retrieval_qa_chat_prompt)
        self.retrieval_chain = create_retrieval_chain(
            retriever=self.vector_store.as_retriever(),
            combine_docs_chain=self.combine_docs_chain
        )

    def query(self, question: str) -> str:
        result = self.retrieval_chain.invoke(input={"input": question})
        return textwrap.fill(result['answer'], 60)


