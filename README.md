# 🛍️ Offline Customer Support Chatbot using Ollama & Llama 3.2

## 📌 Project Overview

This project implements an **offline customer support chatbot** for a fictional e-commerce store **"Chic Boutique"** using **Ollama** and the **Llama 3.2 (3B)** language model.

The chatbot runs **entirely on a local machine**, ensuring:

- 🔒 Complete data privacy (no external APIs)
- 💰 No API costs
- ⚡ Offline functionality

Additionally, this project compares:

- **Zero-Shot Prompting**
- **One-Shot Prompting**

to evaluate which produces better responses.

---

## 🎯 Objectives

- Build a fully functional offline chatbot
- Integrate Python with Ollama API
- Apply prompt engineering techniques
- Evaluate model performance manually
- Analyze zero-shot vs one-shot results

---

## 🧠 Tech Stack

- Python
- Ollama
- Llama 3.2 (3B model)
- Requests library
- HuggingFace Datasets (optional)

---

## 🏗️ Project Structure

offline-chatbot/
│
├── chatbot.py
├── README.md
├── setup.md
├── report.md
│
├── prompts/
│ ├── zero_shot_template.txt
│ └── one_shot_template.txt
│
└── eval/
└── results.md

---

## ⚙️ How the System Works

1. Predefined customer queries are stored in chatbot.py
2. Prompt templates are loaded from the prompts/ folder
3. Queries are inserted into:
   - Zero-shot prompt
   - One-shot prompt
4. HTTP POST request is sent to:
   http://localhost:11434/api/generate
5. Ollama processes the request using Llama 3.2
6. Responses are returned and saved
7. Results are logged in eval/results.md
8. Manual scoring is added

---

## 🔄 System Architecture

chatbot.py → HTTP Request → Ollama Server → Llama 3.2 → Response → results.md

---

## 💬 Sample Queries

- How can I track my order?
- My discount code is not working at checkout
- I want to return a product
- My payment failed but money was deducted
- Can I change my delivery address?
- I received a damaged product
- How do I cancel my order?
- Are there any ongoing offers?

(20 total queries are used in the project)

---

## 🧾 Prompt Engineering

### 🔹 Zero-Shot Prompt

- No examples provided
- Only instructions + query
- Relies on model’s general knowledge

### 🔹 One-Shot Prompt

- Includes one example
- Helps model understand format and tone
- Produces more structured responses

---

## 📊 Evaluation Methodology

Each response is evaluated using:

- Relevance (1–5)
- Coherence (1–5)
- Helpfulness (1–5)

All results are stored in eval/results.md

---

## 📈 Key Findings

- One-shot prompting produced more **consistent and helpful responses**
- Zero-shot responses were sometimes **generic or incomplete**
- Llama 3.2 performs well for basic customer support tasks

---

## ⚠️ Limitations

- No real-time order or database integration
- Possible hallucinations (incorrect answers)
- Slower performance on CPU systems
- Limited reasoning compared to larger models

---

## 🚀 Future Improvements

- Integrate database (order tracking, user data)
- Add multi-turn conversation memory
- Use larger models (7B / 13B)
- Build frontend UI (React / React Native)
- Add voice-based interaction

---

## ▶️ How to Run

1. Install Ollama
2. Pull model:
   ollama pull llama3.2:3b

3. Start Ollama server

4. Install dependencies:
   pip install requests datasets

5. Run chatbot:
   python chatbot.py

6. Check results:
   eval/results.md

---

## 📄 Files Included

- chatbot.py → Main script
- prompts/ → Prompt templates
- eval/results.md → Responses + evaluation
- setup.md → Setup instructions
- report.md → Analysis report
- README.md → Documentation

---

## 📌 Conclusion

This project demonstrates that **offline LLMs can be effectively used for customer support systems** while maintaining privacy and reducing costs.

One-shot prompting significantly improves response quality compared to zero-shot prompting, making it a better choice for real-world applications.
