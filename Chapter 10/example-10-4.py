from fastapi import FastAPI
from starlette.responses import RedirectResponse
from fastapi_app_config import fastapi_app_config
import gradio as gr

app = FastAPI()

def check_up(username, password):
    """鉴权函数"""
    if username == "admin" and password == "admin":
        return True
    return False

with gr.Blocks() as hello_app:
    gr.HTML("<a href='/add'>Add Application</a>")
with gr.Blocks() as add_app:
    add_app = gr.Interface(lambda x, y: x + y, ["number", "number"], "number")

# 挂载gradio应用到fastapi应用上
fastapi_app_config(app, {"/home": hello_app, "/add": add_app}, auth=check_up)

@app.get("/")
async def read_root():
    """根路径"""
    return RedirectResponse(url="/home")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app)