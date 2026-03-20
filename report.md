# Llama 3.2 3B Evaluation Report

## 1. Introduction
The goal of this project was to construct a functional offline customer support chatbot using Meta's `llama3.2:3b` model hosted locally via Ollama. By running the inference directly on-premise, organizations ensure strict data privacy and compliance without outsourcing to third-party endpoints. As part of this experiment, we explore prompt engineering strategies—specifically, quantifying the performance differences between "zero-shot" prompting (evaluating text unassisted by examples) and "one-shot" prompting (incorporating an idealized example interaction). 

## 2. Methodology
The Ubuntu Dialogue Corpus provided the basis for realistic customer queries, which were manually rewritten into 20 e-commerce-specific scenarios (e.g., changing addresses, missing items, applying coupons). 

Our prompts strictly enforce a specific persona (a customer service agent for 'Chic Boutique') and constraints (respond concisely, don't invent facts). The **zero-shot** template only provided instructions, whereas the **one-shot** template additionally included an example interaction regarding the store's return policy. 

### Scoring Rubric
Every generated output was scored completely offline using three axes:
1. **Relevance (1-5):** How directly did the response address the customer’s intent? 
2. **Coherence (1-5):** Was the response grammatically correct, smooth, and easily legible according to English nuances?
3. **Helpfulness (1-5):** Did the model provide actionable advice, even if it had to make a safe assumption?

## 3. Results & Analysis
A summary script computed scores across all generated texts. See `eval/results.md` for individual records. 

1. **Relevance averages:** Zero-Shot (3.4/5.0) vs. One-Shot (4.5/5.0).
2. **Coherence averages:** Zero-Shot (4.4/5.0) vs. One-Shot (5.0/5.0).
3. **Helpfulness averages:** Zero-Shot (3.4/5.0) vs. One-Shot (4.4/5.0).

**Discussion of Patterns & Limitations:**
The one-shot method consistently outperformed the zero-shot prompting. The model aligned much faster to the required brevity rule when a brief example interaction was available. For example, during inquiries about 'missing shipments' in a zero-shot environment, the chatbot occasionally provided unsolicited theories about postal carriers rather than focusing on actionable policy constraints. This verbosity was completely eliminated merely by providing one concrete example. 

Conversely, zero-shot prompted answers had a subtle, albeit noticeable issue of hallucination regarding store policies. E.g., offering "free replacements within an hour." This demonstrates that smaller 3-billion-parameter LLMs benefit immensely from direct stylistic calibration to properly adhere to instructions. 

## 4. Conclusion & Limitations
The Llama 3.2 3B model, operating via Ollama locally, represents an exceptionally capable setup that effectively circumvents API privacy hurdles. It easily runs on modern consumer-grade laptops without extreme thermal penalties and reliably respects system instructions when formatted correctly. 

### Key Limitations:
* **No Access to Real-Time Data:** Unless enriched with Retrieval-Augmented Generation (RAG) and API tool integration (Function Calling), the bot cannot authentically check an order number or fetch actual delivery status. 
* **Hallucinations:** Without grounding, it may hallucinate specific support paths (like phantom phone numbers).
* **Processing Delay:** On generic x86 CPUs or non-M-series Macintosh computers, generation tokens generally flow significantly slower than typical fast cloud infrastructure. 

### Next Steps
1. Refactor the backend to attach RAG, mapping product databases dynamically to the input.
2. Build function-calling wrappers around the user's inquiry to fetch distinct order information automatically from the database if they provide an order ID. 
