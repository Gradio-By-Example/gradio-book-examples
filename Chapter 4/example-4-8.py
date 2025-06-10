import gradio as gr

js = """
function createGradioAnimation() {
    // 你的 JavaScript 代码
}
"""

with gr.Blocks(js=js) as demo:
    # 你的代码
    pass

demo.launch()