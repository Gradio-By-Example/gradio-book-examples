import gradio as gr
import random

def encode(text, key):
    """凯撒加密"""
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_text += char
    return encrypted_text

def on_click(input_text, operator_type, key):
    """处理按钮点击事件"""
    if operator_type == "加密":
        return encode(input_text, key)
    else:
        return encode(input_text, -key)

with gr.Blocks() as demo:
    with gr.Sidebar(position="left"):
        gr.Markdown("# 凯撒密码")
        operator_type = gr.Dropdown(
            choices=["加密", "解密"],
            label="选择操作类型",
            value="加密"
        )
        key = gr.Number(
            label="密钥",
            value=3
        )
    input_text = gr.Textbox(label="原始文本")
    generate_btn = gr.Button("加密", variant="primary")
    output_text = gr.Textbox(label="处理结果")
    generate_btn.click(fn=on_click, inputs=[input_text, operator_type, key], outputs=output_text)

demo.launch()