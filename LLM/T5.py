from transformers import AutoTokenizer, pipeline, AutoModelForCausalLM
from langchain_huggingface.llms import HuggingFacePipeline
from transformers import T5Tokenizer, T5ForConditionalGeneration, pipeline, T5Model
from langchain_huggingface import HuggingFaceEmbeddings
import torch

class t5_model:

    def __init__(self, model_id="t5-base"):
        self.model_id = model_id
        self.tokenizer = T5Tokenizer.from_pretrained(self.model_id)

    def load_model(self, max_new_tokens=1000):
        model = T5ForConditionalGeneration.from_pretrained(self.model_id)
        pipe = pipeline("text2text-generation", model=model, tokenizer=self.tokenizer, max_new_tokens=max_new_tokens,)
        hf = HuggingFacePipeline(pipeline=pipe)
        return hf
    
    def embed(self,text):
        model_name = "t5-base"
        tokenizer = T5Tokenizer.from_pretrained(model_name)
        model = T5Model.from_pretrained(model_name)
        # Tokenize the input text
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        
        # Get the encoder's outputs
        with torch.no_grad():
            outputs = model.encoder(**inputs)

        embeddings = outputs.last_hidden_state.mean(dim=1)
        return embeddings.squeeze().numpy()
