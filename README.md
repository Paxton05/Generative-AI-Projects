# Generative AI Projects

A collection of hands-on Generative AI projects built using Python, LangChain, Hugging Face, Groq LLMs, embeddings, and Streamlit.

This repository contains practical projects exploring Large Language Models (LLMs), text embeddings, prompt engineering, structured output generation, and AI-powered applications.

## Projects

### 1. Embedding Models Lab
**Folder:** `embeddingmodels_Lab`

- Explored text embedding models.
- Experimented with Hugging Face embeddings.
- Learned how text can be converted into numerical vector representations.
- Worked with embedding generation using LangChain.

### 2. LLM-Based Movie Information Extractor
**Folder:** `Movie_Information_Extractor`

- Developed an LLM-powered application to extract movie information from user-provided paragraphs.
- Used LangChain Prompt Templates for information extraction.
- Implemented Pydantic models and PydanticOutputParser for structured and validated output.
- Extracts movie title, release year, genre, director, cast, rating, and summary.
- Includes a Streamlit interface.

### 3. Mood-Based AI Chatbot
**Folder:** `Mood_Based_Chatbot`

- Developed an interactive AI chatbot using Groq LLM and LangChain.
- Implemented three chatbot personalities: Angry, Funny, and Sad.
- Used system prompts to control chatbot behavior.
- Maintained conversational history.
- Built an interactive Streamlit interface.

### 4. Hugging Face Model Inference
**Folder:** `Huggingface_model_inference`

- Explored hosted Hugging Face model inference.
- Experimented with local language model inference.
- Used LangChain integrations to interact with Hugging Face models.
- Worked with models such as DeepSeek-R1 and TinyLlama.

## Technologies Used

- Python
- Generative AI
- Large Language Models (LLMs)
- LangChain
- Hugging Face
- Groq API
- Streamlit
- Pydantic
- Text Embeddings
- Prompt Engineering

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Generative-AI-Projects.git
```

### 2. Navigate to the project directory

```bash
cd Generative-AI-Projects
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure API keys

Create a `.env` file in the root directory and add your required API keys.

Refer to `.env.example` for the required environment variable names.

**Note:** Never upload your actual API keys or `.env` file
