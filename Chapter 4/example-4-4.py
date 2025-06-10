import gradio as gr
with gr.Blocks(theme=gr.themes.Default(primary_hue="red", secondary_hue="blue")) as demo:
    # 你的代码
    input_type = gr.Radio(label="输入类型", choices=["文本", "数字"])
    pass

demo.launch()