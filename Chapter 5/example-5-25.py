import gradio as gr


def process_keyup(_input_value, evt: gr.KeyUpData):
    return evt.key + "|" + evt.input_value


with gr.Blocks() as demo:
    keyup_component = gr.Dropdown(choices=['Keyup', "hello", "select"])
    output_component = gr.Textbox()
    keyup_component.key_up(process_keyup, inputs=keyup_component,
                           outputs=output_component)

demo.launch()