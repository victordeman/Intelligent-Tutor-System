from transformers import pipeline

def generate_synthetic_response(prompt):
    """Generates synthetic learner responses using LLM."""
    generator = pipeline('text-generation', model='gpt2')
    return generator(prompt, max_length=50)[0]['generated_text']
