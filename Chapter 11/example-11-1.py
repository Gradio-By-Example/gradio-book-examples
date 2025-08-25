import gradio as gr


def hello_world():
    gr.Info('This is some info.', visible=False)
    return "hello world"
with gr.Blocks() as demo:
    md = gr.Markdown()
    demo.load(hello_world, inputs=None, outputs=[md])

demo.enable_queue = False
demo.config["enable_queue"] = False
demo.launch()
