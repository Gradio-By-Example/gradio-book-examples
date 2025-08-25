import gradio as gr


def process_input(input_value, request: gr.Request):
    if not request:
        raise gr.Error("没有登录或者登录超时")

    username = request.username

    # 检查用户权限，这里代码只进行简单的用户名称判断
    if username != "admin":
        raise gr.Error("您没有操作权限")

    return "Hello " + input_value


with gr.Blocks() as demo:
    input_component = gr.Textbox()
    output_component = gr.TextArea()
    input_component.input(process_input, inputs=input_component,
                          outputs=output_component)

# 启动应用
demo.launch(auth=[("admin", "admin"), ("Tom", "jerry")])