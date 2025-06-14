import gradio as gr
import platform
from left_side import get_left_side_component


def get_devices():
    return (platform.system(),
            platform.version(),
            platform.processor(),
            platform.architecture(),
            platform.python_version(),
            platform.python_compiler())


def get_devices_component():
    with gr.Blocks() as devices:
        with gr.Row():
            get_left_side_component()
            with gr.Column(scale=3):
                gr.HTML("<h1>Devices</h1>")
                with gr.Group():  # 操作系统信息
                    system = gr.Textbox(label="操作系统名称")
                    version = gr.Textbox(label="操作系统版本")
                with gr.Group():  # 硬件信息
                    processor = gr.Textbox(label="处理器名称")
                    architecture = gr.Textbox(label="处理器架构")
                with gr.Group():  # python信息
                    python_version = gr.Textbox(label="Python版本")
                    python_compiler = gr.Textbox(label="Python编译器")
        devices.load(get_devices, inputs=None,
                     outputs=[system,
                              version,
                              processor,
                              architecture,
                              python_version,
                              python_compiler])
    return devices