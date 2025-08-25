import gradio as gr
import random

def update_dropdown():
    data = [random.randint(0, 100) for _ in range(10)]
    return gr.Dropdown(data)

with gr.Blocks() as demo:
    with gr.Row():
        dropdown = gr.Dropdown(["a", "b", "c"])
        textbox = gr.Textbox()
    btn = gr.Button("Update Dropdown")
    btn.click(update_dropdown, inputs=None, outputs=dropdown)
    dropdown.change(fn=lambda x: x, inputs=dropdown, outputs=textbox)

    demo.load(update_dropdown, inputs=None, outputs=dropdown)

demo.launch()