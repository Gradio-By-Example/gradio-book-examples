import gradio as gr
import random


def greet():
    return str(random.randint(1, 100))


with gr.Blocks() as demo:
    random_text = gr.Textbox(label="随机数")
    output = gr.Textbox(label="最终选择")
    start_btn = gr.Button("开始")
    stop_btn = gr.Button("停止")

    t = gr.Timer(value=1, active=False)
    t.tick(fn=greet, inputs=None, outputs=random_text)

    start_btn.click(lambda: gr.Timer(active=True), inputs=None, outputs=[t])
    stop_btn.click(lambda x: (gr.Timer(active=False), x), inputs=random_text, outputs=[t, output])

    demo.queue().launch()