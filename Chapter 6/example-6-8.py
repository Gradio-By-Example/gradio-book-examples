import gradio as gr


def raise_other_exception():
    raise ValueError("ValueError")


with gr.Blocks(title="example form", ) as demo:
    gr.Button("Info").click(lambda: gr.Info("gr.Info"))
    gr.Button("Warning").click(lambda: gr.Warning("gr.Warning"))
    gr.Button("Error").click(raise_other_exception)


if __name__ == "__main__":
    demo.launch(show_error=True)