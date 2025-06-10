import gradio as gr


TIME_INPUT_ID = "time_input"

demo_head = (f"function(){{document.querySelector('#{TIME_INPUT_ID}"
             + f" input').type = 'time'}}")
with gr.Blocks() as demo:
    # 创建一个类型为时间的 Textbox 组件用于输入时间
    time_input = gr.Textbox(label="Select Time", type="email",
                            elem_id=TIME_INPUT_ID)
    demo.load(fn=lambda: True, js=demo_head)

    output = gr.Textbox()
    time_input.input(lambda x: x, time_input, output)


demo.launch()