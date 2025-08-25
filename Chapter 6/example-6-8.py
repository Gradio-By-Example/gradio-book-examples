import gradio as gr

with gr.Blocks() as demo:
    a = gr.Number(label="a")
    b = gr.Number(label="b")
    with gr.Row():
        add_btn = gr.Button("Add")
        sub_btn = gr.Button("Subtract")
    c = gr.Number(label="add")
    d = gr.Number(label="sub")

    # 使用list传递函数入参，与click事件中inputs参数对应
    def add(num1, num2):
        return num1 + num2
    add_btn.click(add, inputs=[a, b], outputs=c)

    # 使用dict传递函数入参，与click事件中inputs参数对应
    def sub(data):
        return data[a] - data[b]
    sub_btn.click(sub, inputs={a, b}, outputs=d)

demo.launch()