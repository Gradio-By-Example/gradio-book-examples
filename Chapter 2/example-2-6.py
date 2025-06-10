import gradio as gr

def hello_user(hello_text, name):
    return hello_text + " " + name

hello = gr.Textbox(value="Hello")
demo = gr.Interface(fn=hello_user, inputs=[hello, "textbox"], outputs="label")

demo.launch()