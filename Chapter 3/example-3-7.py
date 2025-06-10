import gradio as gr

def input_type_change(type):
    if type == "文本":
        return gr.Textbox(visible=True), gr.Number(visible=False)
    else:
        return gr.Textbox(visible=False), gr.Number(visible=True)

with gr.Blocks() as demo:
    input_type = gr.Radio(label="输入类型", choices=["文本", "数字"])
    input_text = gr.Textbox(label="输入文本", visible=False)
    input_number = gr.Number(label="输入数字", visible=False)
    input_type.change(input_type_change,
                      inputs=input_type,
                      outputs=[input_text, input_number])

demo.launch()