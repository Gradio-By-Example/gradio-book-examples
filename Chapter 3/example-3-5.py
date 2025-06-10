import gradio as gr

with gr.Blocks() as demo:
    with gr.Accordion("Open for More!", open=False):
       gr.Markdown("Look at me...")
       temp_slider = gr.Slider(
          minimum=0.0,
          maximum=1.0,
          value=0.1,
          step=0.1,
          interactive=True,
          label="Slide me",
       )
demo.launch()