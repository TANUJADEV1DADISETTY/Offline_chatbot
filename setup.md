# Setup Instructions

## Requirements
* Python 3.8+
* Ollama installed locally

## Installation
1. Install Ollama from [ollama.com](https://ollama.com).
2. Open a terminal and pull the Llama 3.2 model:
   ```bash
   ollama pull llama3.2:3b
   ```
3. Set up the Python virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
4. Install exactly required dependencies:
   ```bash
   pip install requests datasets
   ```

## Running the Chatbot
To run the evaluation script:
```bash
python chatbot.py
```
This will read prompts from the `prompts/` directory, query the Ollama server, and write results to `eval/results.md`.
