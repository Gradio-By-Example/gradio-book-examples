import gradio as gr

demo = gr.Interface(
    fn=lambda x: x,
    inputs=gr.Image(type="filepath"),
    outputs=gr.Image()
)

demo.launch()