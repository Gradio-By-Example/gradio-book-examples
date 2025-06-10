import gradio as gr


def greet(name_1, name_2):
    return name_1 + " " + name_2 + "!"


with gr.Blocks() as demo:
    t1 = gr.Textbox(label="t1")
    t2 = gr.Textbox(label="t2")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=[t1, t2], outputs=output, api_name="greet")

    examples = gr.Examples(
        examples=[["Hello", "Gradio"],
                  ["Hello", "world"],
                  ["Hi", "Tome"]],
        inputs=[t1, t2],
    )

demo.launch()