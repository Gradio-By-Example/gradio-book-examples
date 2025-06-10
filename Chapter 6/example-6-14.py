import pandas as pd
import gradio as gr

with gr.Blocks() as demo:
    plot_value = pd.DataFrame(data={"x": [1, 2, 3, 4, 5],
                                    "y": [1, 3, 7, 5, 6]})
    with gr.Row():
        gr.LinePlot(value=plot_value, x="x", y="y", label="LinePlot")
        gr.ScatterPlot(value=plot_value, x="x", y="y", label="ScatterPlot")
        gr.BarPlot(value=plot_value, x="x", y="y", label="BarPlot")

if __name__ == "__main__":
    demo.launch()