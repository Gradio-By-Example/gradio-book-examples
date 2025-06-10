import gradio as gr


# 定义一个处理输入并返回结果的函数
def process_input(input_value, request: gr.Request):
    if request:
        ret = [f"Request headers dictionary: {request.headers}",
               f"Username: {request.username}",
               f"IP address: {request.client.host}",
               f"Query parameters: {request.query_params}",
               f"Session hash: {request.session_hash}"]
        return "\n".join(ret)
    else:
        return input_value

with gr.Blocks() as demo:
    input_component = gr.Textbox()
    output_component = gr.TextArea()
    input_component.input(process_input, inputs=input_component,
                          outputs=output_component)

# 启动应用
demo.launch(auth=[("admin", "admin"), ("Tom", "jerry")])