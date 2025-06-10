import gradio as gr
with gr.Blocks() as demo:
    food_box = gr.Number(value=10, label="Food Count")
    status_box = gr.Textbox()
    def eat_return_by_tuple(food):
        if food > 0:
            return food - 1, "full"
        else:
            return food, "hungry"  # 使用tuple返回数据
    gr.Button("EAT").click(
        fn=eat_return_by_tuple,
        inputs=food_box,
        outputs=[food_box, status_box]
    )
demo.launch()