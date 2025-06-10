import gradio as gr

def process_uploaded_file(file):
    # 每当用户上传一个文件时，这个函数就会被触发。
    # 'file' 参数包含了上传的文件对象。
    # 这里我们只是简单地打印文件名并返回同样的文件。
    print(f"Uploaded file: {file.name}")
    return file, file

# 创建Gradio界面
with gr.Blocks() as demo:
    # 创建文件上传组件
    file_input = gr.File(label="Upload File")
    # 可以添加下载组件来提供下载上传文件的链接（如果需要的话）
    download_btn = gr.DownloadButton()
    # 文本框可以显示出上传文件的位置
    file_info = gr.Textbox()

    # 为文件上传组件设置上传事件
    file_input.upload(process_uploaded_file,
                     inputs=file_input, outputs=[download_btn, file_info])

demo.launch()