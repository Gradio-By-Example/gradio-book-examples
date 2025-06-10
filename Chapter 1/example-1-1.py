import gradio as gr


# 定义一个预测函数，这个函数接受一个图片输入，返回模型的预测结果
def predict_image(_image):
    # 这里应该是调用机器学习模型的代码，返回预测结果
    # 例如: return model.predict(image)
    return "predicted_class"


# 使用 Gradio 的 Interface 函数创建一个界面
# fn 参数是上面定义的预测函数
# inputs 参数定义了界面的输入类型，这里是 "image"
# outputs 参数定义了界面的输出类型，这里是 "label"
demo = gr.Interface(fn=predict_image,
                    inputs="image", outputs="label")

# 启动界面
demo.launch()