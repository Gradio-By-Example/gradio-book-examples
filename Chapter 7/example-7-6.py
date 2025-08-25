import gradio as gr

with gr.Blocks(title="example form", ) as demo:
    gr.DataFrame(value=[["Table cell", "Table cell", "Table cell"],
                        ["Table cell", "Table cell", "Table cell"],
                        ["Table cell", "Table cell", "Table cell"]],
                 headers=["Table heading"] * 3,
                 label="This is an example table,"
                       " and this is its caption to describe the contents.")


if __name__ == "__main__":
    demo.launch()