import time

import gradio as gr


def btn_click():
    gr.Info("# Hello")
    time.sleep(10)
    gr.Info("# World")


with gr.Blocks(title="example form", ) as demo:
    gr.HTML("<legend>example form</legend>")
    gr.Button("Button").click(btn_click)


if __name__ == "__main__":
    demo.queue(default_concurrency_limit=2, max_size=3)
    demo.launch(server_name="0.0.0.0")