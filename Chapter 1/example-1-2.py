import gradio as gr

# 定义一个Chatbot函数，接受用户输入的文本，返回Chatbot的回复
def chatbot(text):
    # 这里应该是调用Chatbot模型的代码，返回Chatbot的回复
    # 例如: return chatbot_model.reply(text)
    return "Chatbot reply"

# 使用 Gradio 的 Interface 函数创建一个界面
# fn 参数是上面定义的Chatbot函数
# inputs 参数定义了界面的输入类型，这里是 "textbox"
# outputs 参数定义了界面的输出类型，这里是 "textbox"
demo = gr.Interface(fn=chatbot,
                        inputs="textbox", outputs="textbox")


# 启动界面
demo.launch()