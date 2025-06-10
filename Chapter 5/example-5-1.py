import gradio as gr


def fn_standard(name):
    return "Hello " + name + "."


def fn_output():
    return "Hello world"


def fn_input(name):
    print(name)
    return


def fn_unified(number):
    return str(int(number) + 1)


textbox = gr.Textbox()
output = gr.Textbox()
interface_instance = {"standard": gr.Interface(fn=fn_standard,
                                               inputs=textbox, outputs=output),
                      "output": gr.Interface(fn=fn_output,
                                             inputs=None, outputs="label"),
                      "input": gr.Interface(fn=fn_input,
                                            inputs="text", outputs=None),
                      "unified": gr.Interface(fn=fn_unified,
                                              inputs=textbox, outputs=textbox)}

style = input("Input interface style(standard | input | output | unified):")
if style in interface_instance:
    interface_instance[style].launch()
else:
    print("Input error.")