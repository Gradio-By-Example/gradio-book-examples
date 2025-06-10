import gradio as gr

interface = gr.Interface(fn=lambda x: x,
                         inputs="textbox", outputs="label")
interface.launch(share=True)