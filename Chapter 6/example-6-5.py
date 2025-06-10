import gradio as gr

def get_set_input_function(elem_id, _input_type):
    set_input_time = (f"function(){{document.querySelector('#{elem_id} "
                      + f" input').type = '{_input_type}'}}")
    return set_input_time

with gr.Blocks() as demo:
    datetime_local_ = gr.Textbox(label="Select datetime-local", type="email",
                                 elem_id="datetime-local_")
    demo.load(fn=lambda: True,
              js=get_set_input_function(datetime_local_.elem_id,
                                        "datetime-local"))

    month_ = gr.Textbox(label="Select month", type="email", elem_id="month_")
    demo.load(fn=lambda: True, js=get_set_input_function(month_.elem_id,
                                                         "month"))

    search_ = gr.Textbox(label="Input search", type="email", elem_id="search_")
    demo.load(fn=lambda: True, js=get_set_input_function(search_.elem_id,
                                                         "search"))

    tel_ = gr.Textbox(label="Input tel", type="email", elem_id="tel_")
    demo.load(fn=lambda: True, js=get_set_input_function(tel_.elem_id, "tel"))

    time_ = gr.Textbox(label="Select time", type="email", elem_id="time_")
    demo.load(fn=lambda: True,
              js=get_set_input_function(time_.elem_id, "time"))

    url_ = gr.Textbox(label="Input url", type="email", elem_id="url_")
    demo.load(fn=lambda: True, js=get_set_input_function(url_.elem_id, "url"))

    week_ = gr.Textbox(label="Select week", type="email", elem_id="week_")
    demo.load(fn=lambda: True,
              js=get_set_input_function(week_.elem_id, "week"))

    output = gr.Textbox(label="Receive time")
    time_.input(lambda x: x, time_, output)


demo.launch()