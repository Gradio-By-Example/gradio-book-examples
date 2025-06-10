import gradio as gr

with open("python_code_sample.py", "r", encoding="utf-8") as file:
    code_content = file.read()
with gr.Blocks() as demo:
    gr.Code(label="Code example",
            value=code_content,
            language="python")
demo.launch()