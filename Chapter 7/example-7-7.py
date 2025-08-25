import gradio as gr


def raise_error():
    raise gr.Error("gr.Error")


with gr.Blocks(title="example form", ) as demo:
    gr.Button("Info").click(lambda: gr.Info("gr.Info"))
    gr.Button("Warning").click(lambda: gr.Warning("gr.Warning"))
    gr.Button("Error").click(raise_error)


if __name__ == "__main__":
    demo.launch()