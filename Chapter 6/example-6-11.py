import gradio as gr


def failure():
    raise gr.Error("This should fail!")


def exception():
    raise ValueError("Something went wrong")


def warning_fn():
    gr.Warning("This is a warning!")


def info_fn():
    gr.Info("This is some info")


with gr.Blocks() as demo:
    with gr.Row():
        result = gr.Textbox(label="Result")
        result_2 = gr.Textbox(label="Consecutive Event")
    with gr.Row():
        failure_btn = gr.Button(value="Trigger Failure")
        failure_exception = gr.Button(value="Trigger Failure With ValueError")
    with gr.Row():
        trigger_warning = gr.Button(value="Trigger Warning")
        trigger_info = gr.Button(value="Trigger Info")

    failure_btn.click(failure, None, None)\
       .success(lambda: "Should not be triggered", inputs=None, outputs=result)
    failure_exception.click(exception, None, None)\
       .success(lambda: "Should not be triggered", inputs=None, outputs=result)
    trigger_warning.click(warning_fn, None, result)\
       .success(lambda: "Should be triggered", inputs=None, outputs=result)
    trigger_info.click(info_fn, None, None)\
       .success(lambda: "Should be triggered", inputs=None, outputs=result)


if __name__ == "__main__":
    demo.launch(show_error=True)