import gradio as gr
import ollama
import io


def get_describe(image_data, question):
    buffered = io.BytesIO()
    image_data.save(buffered, format="JPEG")
    image_bytes = buffered.getvalue()

    question = question or "图中的是什么"

    res = ollama.chat(
        model="moondream",
        messages=[
            {
                'role': 'user',
                'content': question,
                'images': [image_bytes]
            }
        ]
    )
    return res['message']['content']


demo = gr.Interface(
    get_describe,
    [gr.Image(type="pil", label="Upload Image"), "textbox"],
    "textbox",
    live=False
)
demo.launch()