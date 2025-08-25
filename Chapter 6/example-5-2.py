import gradio as gr


def on_click():
    return "Button clicked."


with gr.Blocks() as demo:
    button = gr.Button("Click me")
    output = gr.Textbox()
    button.click(on_click, outputs=output)

demo.launch()