import gradio as gr


def dropdown_keyup(last_value, data: gr.KeyUpData):
    return f"{last_value}, {data.input_value}"


with gr.Blocks() as demo:
    dropdown = gr.Dropdown(interactive=True, allow_custom_value=True)
    output = gr.Textbox()
    dropdown.key_up(dropdown_keyup, dropdown, output)

demo.launch()