from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from transformers import pipeline
import torch 

# Load Llama model and tokenizer
model_id = "C:\\Users\\mohit.b.rana\\Downloads\\llama3\\Llama-3.1-8B-Instruct"
pipe = pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={
        "torch_dtype":torch.bfloat16
    },
    device="cpu",
)

 
def classify_query(api_key, query, max_tokens=50):
    """
    Use Llama model to classify user query.
    Args:
        api_key (str): Placeholder for consistency (can be ignored here).
        query (str): The user query.
        max_tokens (int): Max tokens for the response.
    Returns:
        str: Classified response from the Llama model.
    """
    prompt = f"Classify query: {query}"
    # response = generator(prompt, max_length=max_tokens, num_return_sequences=1)
    outputs = pipe(prompt, max_new_tokens=256, do_sample=False)
    return outputs[0]["generated_text"].strip()