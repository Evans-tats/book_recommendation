# book_recommendation
This is a semantic-powered book recommendation system built using LLMs, vector search, and sentiment analysis. Users can search for books in natural language, filter by genre and emotion, and get meaningful recommendations—all via a Gradio-powered web interface.

## Features
Feature	Description
Text Data Cleaning	Performed in data-exploration.ipynb. Ensures book metadata is clean and ready for semantic processing.
Semantic Search (Vector DB)	Implemented in vector-search.ipynb. Uses vector embeddings to find the most similar books to a query like "a story of revenge in medieval times."
Zero-shot Text Classification	Found in text-classification.ipynb. Automatically labels books as Fiction or Non-Fiction using LLMs.
Sentiment & Emotion Analysis	Implemented in sentiment-analysis.ipynb. Extracts emotions such as joy, fear, sadness to help users explore books by tone.
Interactive Web App	Created in gradio-dashboard.py. Users can search, filter, and get personalized recommendations.

  🛠️ Tech Stack
Python 3.11

LangChain

Gradio

Transformers (HuggingFace)

ChromaDB (Vector DB)

Pandas / Seaborn / Matplotlib

Jupyter Notebooks

📦 Installation
1. Clone the repo
bash
Copy
Edit
git clone https://github.com/your-username/book-recommendation.git
cd book-recommendation
2. Set up virtual environment (recommended)
bash
Copy
Edit
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
🔑 Environment Setup
Create a .env file in the root directory with your OpenAI API key:

ini
Copy
Edit
OPENAI_API_KEY=your-openai-key
📚 Dataset
The book metadata is sourced from Kaggle. Download instructions are provided in the repo (typically via kagglehub).

Make sure the data is placed in the appropriate directory as referenced by the notebooks.

💻 Run the App
After preprocessing and vector database setup:

bash
Copy
Edit
python UI/gradio-dashboard.py
This will start a local Gradio server:

nginx
Copy
Edit
Running on http://127.0.0.1:7860
Set share=True in the launch() function if you'd like to share it publicly.
🧠 How It Works
Text data is cleaned and vectorized using Sentence Transformers.

A vector database is built with ChromaDB to enable similarity search.

LLMs classify books by genre and sentiment/emotion using zero-shot classification.

Gradio provides an interactive interface for querying and filtering recommendations.

🙋‍♀️ Future Work
Add collaborative filtering for personalized recommendations

Enhance emotion modeling with custom fine-tuned models

Support multi-language book search

👤 Author
Evans Kipsang
Nairobi, Kenya
