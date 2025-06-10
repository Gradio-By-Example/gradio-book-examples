import gradio as gr

with gr.Blocks() as demo:
     input_number = gr.Number(label="count", value=0, minimum=0, maximum=6, step=1)

     @gr.render(inputs=input_number)
     def show_split(count):
         if count == 0:
             gr.Markdown("## No Textbox")
         else:
             for n in range(1, count+1):
                 gr.Textbox(str(n))

demo.launch()