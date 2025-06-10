from fastapi import FastAPI
import gradio as gr

app = FastAPI()


@app.get("/")
def fastapi_main():
    return {"message": "This is FastAPI app"}


with gr.Blocks() as hello_app:
    gr.HTML("<a href='/add'>Add Application</a>")
gr.mount_gradio_app(app, hello_app, path="/hello")

add_app = gr.Interface(lambda x, y: x + y, ["number", "number"], "number")
gr.mount_gradio_app(app, add_app, path="/add")