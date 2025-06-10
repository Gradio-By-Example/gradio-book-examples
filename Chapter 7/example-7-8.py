import gradio as gr

def echo(audio):
    return audio

with gr.Blocks() as demo:
    audio = gr.Audio(sources=["upload", "microphone"], type="numpy")
    button = gr.Button("Echo Audio")
    outputs = gr.Audio()
    button.click(echo, audio, outputs)
demo.launch()