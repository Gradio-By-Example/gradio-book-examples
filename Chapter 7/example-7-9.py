import gradio as gr

def echo(video):
    return video

with gr.Blocks() as demo:
    video = gr.Video(sources=["upload", "webcam"])
    button = gr.Button("Echo Video")
    outputs = gr.Video()
    button.click(echo, video, outputs)
demo.launch()