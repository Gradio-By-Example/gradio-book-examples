import gradio as gr


with gr.Blocks() as demo:
    with gr.Tabs() as tabs:
        with gr.Tab(label="Login", id=1):
            username = gr.Textbox()
            password = gr.Textbox(type="password")
            login_button = gr.Button("Submit")
        with gr.Tab(label="Confirm", id=2):
            gr.Label("Login OK")
    login_button.click(lambda: gr.update(selected=2), outputs=tabs)


if __name__ == "__main__":
    demo.launch()