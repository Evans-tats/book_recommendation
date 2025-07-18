import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.recommendation_utils import recommend_books, get_categories_and_tones

import gradio as gr
categories, tone = get_categories_and_tones()

with gr.Blocks(theme= gr.themes.Glass()) as dashboard:
    gr.Markdown("# Gardio Dashboard")

    with gr.Row():
        user_query = gr.Textbox(
            label = "please enter a description of the book you want",
            placeholder="eg A story about a dog who goes on an adventure",
        )
        category_dropdown = gr.Dropdown(
            choices =["ALL"] + categories, label="select a category:", value="All",
        )
        tone_dropdown = gr.Dropdown(
            choices = ["ALL"]+ tone, label="select a tone:", value="ALL",
        )

        submit_button = gr.Button("Get Recommendations")
    
    gr.Markdown("## recommendations")

    output = gr.Gallery(
        label="Recommended Books",
        show_label=True,
        columns=5,
        rows=2,
    )
    submit_button.click(
        fn = recommend_books,
        inputs = [user_query, category_dropdown, tone_dropdown],
        outputs = output, 
    )
    print("Dashboard is ready")

if __name__ == "__main__":
    dashboard.launch()