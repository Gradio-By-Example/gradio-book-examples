import gradio as gr

def predict_image(image):
    return "predicted_class"

interface = gr.Interface(fn=predict_image, inputs="image", outputs="label")

interface.launch(mcp_server=True)