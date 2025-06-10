import gradio as gr

default_theme = gr.themes.Default()
theme = default_theme.set(
    loader_color="#FF0000",
    slider_color="#FF0000")
with gr.Blocks(theme=theme) as demo:
    # 你的代码
    input_type = gr.Radio(label="输入类型", choices=["文本", "数字"])
    pass

demo.launch()