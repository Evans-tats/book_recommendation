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

## How It Works

Text data is cleaned and vectorized using Sentence Transformers.

A vector database is built with ChromaDB to enable similarity search.

LLMs classify books by genre and sentiment/emotion using zero-shot classification.

Gradio provides an interactive interface for querying and filtering recommendations.

 ## Future Work
Add collaborative filtering for personalized recommendations

Enhance emotion modeling with custom fine-tuned models

Support multi-language book search

👤 Author
Evans Kipsang
Nairobi, Kenya
