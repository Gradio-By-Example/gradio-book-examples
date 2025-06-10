import gradio as gr

with gr.Blocks() as demo:
    input_number = gr.Number(label="count", value=0, minimum=0, maximum=6, step=1)

    @gr.render(inputs=input_number)
    def show_split(count):
        number_of_inputs = []
        if count == 0:
            gr.Markdown("## No Input Provided")
        else:
            for n in range(1, count+1):
                number = gr.Number(n)
                number_of_inputs.append(number)

        def fn_sum(*args):
            return sum(args)

        sum_button.click(fn_sum, number_of_inputs, output_sum)

    sum_button = gr.Button("Sum")
    output_sum = gr.Textbox(label="Sum", value="0")

demo.launch()