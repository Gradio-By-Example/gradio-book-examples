import gradio as gr


def on_select(evt: gr.SelectData):  # SelectData is a subclass of EventData
    return f"You selected {evt.value} at {evt.index} from {evt.target}"


with gr.Blocks() as demo:
    table = gr.Dataframe([[1, 2, 3], [4, 5, 6]])
    textbox = gr.Textbox("Hello World!")

    statement = gr.Textbox()

    table.select(on_select, None, statement)
    textbox.select(on_select, None, statement)

demo.launch()