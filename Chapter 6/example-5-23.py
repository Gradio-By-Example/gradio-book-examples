import gradio as gr


# 定义一个处理输入并返回结果的函数
def process_input(input_value, evt: gr.EventData):
    print(evt)
    # 对输入值进行处理，然后返回结果
    return input_value.upper()  # 这里简单地将文本转换为大写作为示例


with gr.Blocks() as demo:
    # 创建一个文本输入组件
    input_component = gr.Textbox()
    # 创建一个文本输出组件，用于显示输入事件处理函数的结果
    output_component = gr.Textbox()

    # 使用input事件监听器，当用户在文本框中输入时触发process_input函数
    input_component.input(process_input, inputs=input_component,
                          outputs=output_component)

# 启动应用
demo.launch()