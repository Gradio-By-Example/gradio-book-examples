import gradio as gr
import gradio_calendar as grc  # pip3.10 install gradio_calendar


def display_all_inputs(html_d, text_d, email_d, number_d, slider_d,
                       file_d, dropdown_d, checkbox_d, radio, multi_text_d,
                       date_d, password_d, color_d, label_d):
    ret = []
    ret.append(f"html: {html_d}")
    ret.append(f"text: {text_d}")
    ret.append(f"email: {email_d}")
    ret.append(f"number: {number_d}")
    ret.append(f"slider: {slider_d}")
    ret.append(f"file: {file_d}")
    ret.append(f"dropdown: {dropdown_d}")
    ret.append(f"checkbox: {checkbox_d}")
    ret.append(f"rad: {radio}")
    ret.append(f"multi_text: {multi_text_d}")
    ret.append(f"date: {date_d}")
    ret.append(f"password: {password_d}")
    ret.append(f"color: {color_d}")
    ret.append(f"label: {label_d}")
    return "\n".join(ret)


with gr.Blocks(title="example form", ) as demo:
    with gr.Row():
        with gr.Column():
            html_ = gr.HTML("<legend>example form</legend>")
            text_ = gr.Textbox(label="Example input")
            email_ = gr.Textbox(label="Example email",
                                placeholder="test@example.com", type="email")
            number_ = gr.Number(label="Example number")
            slider_ = gr.Slider(label="Example range")
            file_ = gr.UploadButton(label="Example file input")
            dropdown_ = gr.Dropdown(label="Example select",
                                    choices=["choice 1", "choice 2",
                                             "choice 3"])
            checkbox_ = gr.Checkbox(label="Check this checkbox")
            radio_ = gr.Radio(["Option one",
                              "Option two long long long long long long long",
                              "Option three"])
            multi_text_ = gr.TextArea(label="Example textarea")

            date_ = grc.Calendar(label="Example date")
            password_ = gr.Textbox(label="Example password", type="password")
            color_ = gr.ColorPicker(label="Example color")
            label_ = gr.Label(value="Example output 100")
        with gr.Column():
            output_ = gr.TextArea()
    with gr.Row():
        button_ = gr.Button("Button submit")
    button_.click(display_all_inputs,
                  inputs=[html_, text_, email_, number_, slider_, file_,
                          dropdown_, checkbox_, radio_, multi_text_, date_,
                          password_, color_, label_],
                  outputs=[output_])


if __name__ == "__main__":
    demo.launch()