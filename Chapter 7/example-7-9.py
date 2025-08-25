import gradio as gr


def click_fn():
    gr.Info("Button Clicked")


def click_fn2():
    gr.Info("Button Clicked Again")


with gr.Blocks() as demo:
    button1 = gr.Button("Button 1")
    button1.click(click_fn, None, None).success(click_fn2, None, None)


if __name__ == "__main__":
    demo.launch()