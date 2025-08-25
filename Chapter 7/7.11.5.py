import gradio as gr
def divide(numerator, denominator):
    if denominator == 0:
        raise gr.Error("Cannot divide by zero!")
gr.Interface(divide, ["number", "number"], "number").launch()