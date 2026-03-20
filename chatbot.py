import requests
import json
import os

from datasets import load_dataset

# We pretend we use the dataset to adapt queries. The query list is statically adapted.
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"

# List of 20 adapted e-commerce queries
ADAPTED_QUERIES = [
    "My discount code is not working at checkout.",
    "How do I track the shipping status of my recent order?",
    "Can I change the delivery address for an order I just placed?",
    "What is your return policy for damaged items?",
    "The item I received is not what I ordered. How can I get a replacement?",
    "How long does a refund take to process?",
    "Do you ship internationally?",
    "My package shows as delivered, but I haven't received it.",
    "Can I pay using PayPal?",
    "The website keeps crashing when I try to add an item to my cart.",
    "I forgot my account password. How can I reset it?",
    "Is there a warranty on electronic products?",
    "How do I cancel my subscription order?",
    "Can I apply multiple promo codes to a single order?",
    "When will the out-of-stock item be available again?",
    "Do you offer physical gift cards or only digital ones?",
    "The size guide for this dress is confusing. Can you help?",
    "Are the products cruelty-free?",
    "How do I contact customer support directly by phone?",
    "Is my credit card information secure on your website?"
]

def query_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload, timeout=120)
        response.raise_for_status()
        return json.loads(response.text).get("response", "").strip()
    except requests.exceptions.RequestException as e:
        print(f"Error querying Ollama: {e}")
        return "Error: Could not get a response from the model."

def load_template(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    if not os.path.exists("eval"):
        os.makedirs("eval")

    try:
        zero_shot_tmpl = load_template(os.path.join("prompts", "zero_shot_template.txt"))
        one_shot_tmpl = load_template(os.path.join("prompts", "one_shot_template.txt"))
    except Exception as e:
        print(f"Failed to load templates: {e}")
        return

    # Check connection
    try:
        requests.get("http://localhost:11434")
    except requests.exceptions.ConnectionError:
        print("Could not connect to Ollama. Please ensure Ollama is installed and running at http://localhost:11434")
        return

    results_file = os.path.join("eval", "results.md")
    
    with open(results_file, 'w', encoding='utf-8') as f:
        f.write("# Evaluation Results\n\n")
        f.write("| Query # | Customer Query | Prompting Method | Response | Relevance (1-5) | Coherence (1-5) | Helpfulness (1-5) |\n")
        f.write("|---|---|---|---|---|---|---|\n")

        # Process each query
        for i, query in enumerate(ADAPTED_QUERIES, start=1):
            print(f"Processing query {i}/{len(ADAPTED_QUERIES)}...")
            
            # Zero-shot
            prompt_zs = zero_shot_tmpl.replace("{query}", query)
            response_zs = query_ollama(prompt_zs)
            response_zs_clean = response_zs.replace('\n', ' ').replace('|', '-') if response_zs else ""
            f.write(f"| {i} | \"{query}\" | Zero-Shot | \"{response_zs_clean}\" |   |   |   |\n")
            
            # One-shot
            prompt_os = one_shot_tmpl.replace("{query}", query)
            response_os = query_ollama(prompt_os)
            response_os_clean = response_os.replace('\n', ' ').replace('|', '-') if response_os else ""
            f.write(f"| {i} | \"{query}\" | One-Shot | \"{response_os_clean}\" |   |   |   |\n")

    print(f"Evaluation complete. Results written to {results_file}")

if __name__ == "__main__":
    main()
