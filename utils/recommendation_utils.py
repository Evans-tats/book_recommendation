from utils.chroma_utils import load_chroma
import pandas as pd


def load_books():
    """
    Load the books dataset from a CSV file.
    
    Returns:
        pd.DataFrame: DataFrame containing the books data.
    """
    return pd.read_csv("/home/tatsye/Desktop/book_recommendation/books_with_large_thumbnail.csv")
    
def retrieve_semantic_recommendation(
        query: str,
        category: str = None,
        tone: str = None,
        initial_top_k: int = 50,
        final_top_k: int = 16,
) -> pd.DataFrame:
    """
    Retrieve semantic recommendations based on the query and optional filters.
    
    Args:
        query (str): The search query.
        category (str, optional): Category filter for recommendations.
        tone (str, optional): Tone filter for recommendations.
        initial_top_k (int, optional): Initial number of top results to consider. Defaults to 50.
        final_top_k (int, optional): Final number of top results to return. Defaults to 16.
    
    Returns:
        pd.DataFrame: DataFrame containing the recommended books.
    """
    
    vector_store = load_chroma()

    recs = vector_store.similarity_search(
        query,
        k=initial_top_k
    ) 
    books = load_books()
    book_list = [int(rec.page_content.strip('"').split(":")[0]) for rec in recs]
    book_recs = books[books["isbn13"].isin(book_list)].head(initial_top_k)

    if category != "All":
        book_recs = book_recs[book_recs["simple_categories"] == category].head(final_top_k)
    else:
        book_recs = book_recs.head(final_top_k)


    if tone == "happy":
        book_recs = book_recs.sort_values(by="joy", ascending=False, inplace=True)
    elif tone == "sad":
        book_recs = book_recs.sort_values(by="sadness", ascending=False, inplace=True)
    elif tone == "angry":
        book_recs = book_recs.sort_values(by="angry", ascending=False, inplace=True)
    elif tone == "suprising":
        book_recs = book_recs.sort_values(by="surpise", ascending=False, inplace=True)
    elif tone == "suspenseful":
        book_recs = book_recs.sort_values(by="fear", ascending=False, inplace=True)
    
    return book_recs

def recommend_books(
        query: str,
        category: str,
        tone: str,
):
    recommendation = retrieve_semantic_recommendation(
        query,
        category,
        tone
    )
    results = []

    for _, row in recommendation.iterrows():
        description = row["description"]
        truncated_decs_split = description.split()
        truncated_description = " ".join(truncated_decs_split[:30])+ ".........."

        authors_split = row["authors"].split(";")
        if len(authors_split) == 2:
            authors_str = f"{authors_split[0]} and {authors_split[1]}"
        elif len(authors_split) > 2:
            authors_str = f"{', '.join(authors_split[:-1])}, and {authors_split[-1]}"
        else:
            authors_str = row["authors"]

        caption = f"{row['title']} by {authors_str}: {truncated_description}"
        results.append((row["large_thumbnail"], caption))
    return results

def get_categories_and_tones():
    """
    Get the list of categories and tones for the recommendation filters.
    
    Returns:
        tuple: A tuple containing two lists - categories and tones.
    """
    books = load_books()
    categories = ["All"] + sorted(books["simple_categories"].unique())
    tones = ["All"] + ["Happy", "Surprising", "Angry", "Suspenseful", "Sad"]
    return categories, tones
