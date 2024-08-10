from graphRAG_generation import GraphRAG
from vectorRAG_generation import VectorRAG


def query_graph_or_vector_rag(use_graph: bool, question: str) -> str:
    if use_graph:
        # GraphRAG
        query_generator = GraphRAG()
        cypher_query = query_generator.generate_cypher_query(question)
        return f"Cypher Query: {cypher_query}"

    else:
        # VectorRAG
        retrieval_qa = VectorRAG()
        answer = retrieval_qa.query(question)
        return f"Answer: {answer}"


# query
question = "Who was leading the Battle of Waterloo?"

# Use GraphRAG -> True
# Use VectorRAG -> False
result_relationship = query_graph_or_vector_rag(True, question)
print(result_relationship)

