import gradio as gr

head = """
<script async src="https://www.googletagmanager.com/gtag/js?\
id={google_analytics_tracking_id}"></script>
<script>
    // 你的 Google Analytics 代码
</script>
"""

with gr.Blocks(head=head) as demo:
    # 你的代码
    pass

demo.launch()