import gradio as gr
from left_side import get_left_side_component
import sqlite3


def reset_profile(request: gr.Request):
    username = request.username
    # 从数据库中获取用户信息
    description = get_user_info(username)
    return username, description, "", ""


def get_user_info(username):
    conn = sqlite3.connect("website_sample.db")
    cursor = conn.cursor()
    cursor.execute("SELECT description FROM users WHERE username=?", (username,))
    record = cursor.fetchone()
    description = record[0]
    cursor.close()
    conn.close()
    return description


def submit_profile(username, description, password, repeat_password, request: gr.Request):
    # 校验用户名是否一致
    if username != request.username:
        raise gr.Error("用户名不一致")
    # 校验密码是否一致
    if password != repeat_password:
        gr.Warning("密码不一致")
        return
    # 写入数据库
    update_db(description, password, username)
    gr.Info("更新成功")


def update_db(description, password, username):
    conn = sqlite3.connect("website_sample.db")
    cursor = conn.cursor()
    if password:
        cursor.execute("UPDATE users SET description=?, password=? WHERE username=?", (description, password, username))
    else:
        cursor.execute("UPDATE users SET description=? WHERE username=?", (description, username))
    conn.commit()
    cursor.close()
    conn.close()


def get_profile_component():
    with gr.Blocks() as profile:
        with gr.Row():
            get_left_side_component()
            with gr.Column(scale=1):
                pass
            with gr.Column(scale=3):
                gr.HTML("<h1>Profile</h1>")
                username = gr.Label(label="User Name")
                description = gr.TextArea(label="Job Description")
                password = gr.Textbox(label="password")
                repeat_password = gr.Textbox(label="repeat_password")
                with gr.Row():
                    reset_button = gr.Button("Reset")
                    submit_button = gr.Button("Submit")

                reset_button.click(reset_profile, inputs=None,
                                   outputs=[username, description, password, repeat_password])
                submit_button.click(submit_profile,
                                    inputs=[username, description, password, repeat_password],
                                    outputs=None)
            with gr.Column(scale=1):
                pass
        profile.load(fn=reset_profile, outputs=[username, description, password, repeat_password])

    return profile