import gradio as gr
with gr.Blocks() as demo:
    food_box = gr.Number(value=10, label="Food Count")
    status_box = gr.Textbox()
    def eat_return_by_dict(food):
        if food > 0:
            return {food_box: food - 1, status_box: "full"}
        else:
            return {status_box: "hungry"}  # 使用dict返回数据
    gr.Button("EAT").click(
        fn=eat_return_by_dict,
        inputs=food_box,
        outputs=[food_box, status_box]
    )
demo.launch()