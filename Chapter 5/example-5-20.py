import gradio as gr
import json


def update_dropdown():
    return gr.Dropdown(["a", "b", "c", "d"])


with gr.Blocks() as demo:
    dropdown = gr.Dropdown(["a", "b", "c"])
    dropdown.change(lambda x: print(x), inputs=dropdown)
    btn = gr.Button("Update Dropdown")
    btn.click(update_dropdown, inputs=None, outputs=dropdown)

demo.launch()