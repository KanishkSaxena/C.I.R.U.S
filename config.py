from langchain.globals import set_llm_cache
from langchain.cache import InMemoryCache
from transformers import pipeline

set_llm_cache(InMemoryCache())


def send_to_openai_gpt(prompts, model_name="gpt2", max_length=100):
    """
    Helper function for sending prompts to an open-source model (e.g., GPT-2).

    Args:
        prompts: List of text prompts
        model_name: Name of the pre-trained model (e.g., "gpt2")
        max_length: Maximum length of the generated response

    Returns:
        List of generated responses corresponding to the prompts
    """
    # Load the pre-trained model
    model = pipeline("text-generation", model=model_name)

    # Generate responses for each prompt
    responses = []
    for prompt in prompts:
        response = model(prompt, max_length=max_length, num_return_sequences=1)[0]['generated_text']
        responses.append(response)

    return responses
