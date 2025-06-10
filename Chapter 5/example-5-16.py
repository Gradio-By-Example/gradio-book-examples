import gradio as gr

with gr.Blocks() as demo:
    input_audio = gr.Audio(label="Input Audio", type="filepath", format="mp3")
    with gr.Row():
        with gr.Column():
            stream_as_file_btn = gr.Button("Stream as File")
            format_ = gr.Radio(["wav", "mp3"], value="wav", label="Format")
            stream_as_file_output = gr.Audio(streaming=True)

            def stream_file(_audio_file, _format):
                # 音频流式处理函数
                # 示例中省略具体实现
                pass

            stream_as_file_btn.click(
                stream_file, [input_audio, format_], stream_as_file_output
            )

    # 其他代码...

if __name__ == "__main__":
    demo.queue().launch()