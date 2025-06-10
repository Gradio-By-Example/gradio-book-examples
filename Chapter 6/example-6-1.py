import gradio as gr
import gradio_calendar as grc  # pip install gradio_calendar

with gr.Blocks(title="example form", ) as demo:
    html_ = gr.HTML("<legend>example form</legend>")
    text_ = gr.Textbox(label="Example input")
    email_ = gr.Textbox(label="Example email",
                        placeholder="test@example.com", type="email")
    number_ = gr.Number(label="Example number")
    slider_ = gr.Slider(label="Example range")
    file_ = gr.UploadButton(label="Example file input")
    dropdown_ = gr.Dropdown(label="Example select",
                            choices=["choice 1", "choice 2", "choice 3"])
    dropdown_.change(lambda x: print(x), inputs=dropdown_)
    checkbox_ = gr.Checkbox(label="Check this checkbox")
    radio = gr.Radio(["Option one",
                      "Option two long long long long long long long long",
                      "Option three"])
    multi_text_ = gr.TextArea(label="Example textarea")

    date_ = grc.Calendar(label="Example date")
    password_ = gr.Textbox(label="Example password", type="password")
    color_ = gr.ColorPicker(label="Example color")
    label_ = gr.Label(value="Example output 100")
    button_ = gr.Button("Button submit")

if __name__ == "__main__":
    demo.launch()