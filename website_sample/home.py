import gradio as gr
from left_side import get_left_side_component


def on_load(request: gr.Request):
    return request.username


def get_home_component():
    with gr.Blocks() as home:
        with gr.Row():
            get_left_side_component()
            with gr.Column(scale=3):
                gr.HTML("<h1>Home</h1>")
                gr.HTML("这是一个网站的示例。")
                txt = gr.Textbox()
        home.load(fn=on_load, outputs=[txt])
    return home