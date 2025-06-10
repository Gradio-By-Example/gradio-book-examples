import gradio as gr


with gr.Blocks() as demo:
    input_component = gr.Textbox()
    output_component = gr.TextArea()

# 启动应用
demo.launch(auth=[("admin", "admin"), ("Tom", "jerry")])