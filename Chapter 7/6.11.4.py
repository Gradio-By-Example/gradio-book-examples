import gradio as gr
def hello_world():
    gr.Warning('This is a warning message.')
    return "hello world"
with gr.Blocks() as demo:
    md = gr.Markdown()
    demo.load(hello_world, inputs=None, outputs=[md])
demo.queue().launch()