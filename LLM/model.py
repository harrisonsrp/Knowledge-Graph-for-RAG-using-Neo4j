from transformers import AutoTokenizer, pipeline, AutoModelForCausalLM
from langchain_huggingface.llms import HuggingFacePipeline
from transformers import T5Tokenizer, T5ForConditionalGeneration, pipeline
from langchain_huggingface import HuggingFaceEmbeddings


class t5_model:

    def __init__(self, model_id="google/flan-t5-base"):
        self.model_id = model_id
        self.tokenizer = T5Tokenizer.from_pretrained(self.model_id)

    def load_model(self, max_new_tokens=1000):
        model = T5ForConditionalGeneration.from_pretrained(self.model_id)
        pipe = pipeline("text2text-generation", model=model, tokenizer=self.tokenizer, max_new_tokens=max_new_tokens,)
        hf = HuggingFacePipeline(pipeline=pipe)
        return hf
    
    def embedding_model(self):
        embeddings = HuggingFaceEmbeddings(model_name="t5-base")
        return embeddings


