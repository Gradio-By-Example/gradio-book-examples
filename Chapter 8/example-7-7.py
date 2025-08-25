import gradio as gr
import numpy as np

def flip(im):
    return np.flipud(im)

with gr.Blocks() as demo:
    webcam = gr.Image(sources=["upload", "webcam", "clipboard"], streaming=False)
    button = gr.Button("Flip Image")
    output = gr.Image()
    button.click(flip, webcam, output)
demo.launch()