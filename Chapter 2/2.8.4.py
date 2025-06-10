import gradio as gr

def button_click():
    return "Button clicked!"

with gr.Blocks() as demo:
    button = gr.Button("Click me!")
    button.click(button_click, None, gr.Textbox())

if __name__ == "__main__":
    demo.launch()