import gradio as gr
from left_side import get_left_side_component


def get_about_component():
    with gr.Blocks() as about:
        with gr.Row():
            get_left_side_component()
            with gr.Column(scale=3):
                gr.HTML("<h1>About</h1>")
                gr.HTML("This is a sample website.")
    return about