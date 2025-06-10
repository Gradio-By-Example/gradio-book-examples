import gradio as gr
import gradio_modal as grm  # pip install gradio_modal


with gr.Blocks() as demo:
    show_btn = gr.Button("Show Modal")

    with grm.Modal(visible=False) as modal:
        gr.Label(value="Modal title", show_label=False)
        gr.Markdown(value="# H1\n## H2\nSomthing...")
        with gr.Row():
            gr.Column(scale=10)
            with gr.Column():
                with gr.Row():
                    modal_ok = gr.Button("OK", variant="primary", size="sm")
                    modal_cancel = gr.Button("Cancel", size="sm")

    show_btn.click(lambda: grm.Modal(visible=True), None, modal)
    gr_text = gr.Textbox()

    modal_ok.click(lambda: (grm.Modal(visible=False), "Yes"),
                   None, [modal, gr_text])
    modal_cancel.click(lambda: (grm.Modal(visible=False), "No"),
                       None, [modal, gr_text])

if __name__ == "__main__":
    demo.launch()