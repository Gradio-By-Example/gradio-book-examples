import gradio as gr
import sqlite3
from left_side import get_left_side_component
import gradio_modal as grm


def get_members():
    # 从数据库中获取用户列表
    conn = sqlite3.connect("website_sample.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username, description FROM users")
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    records = [list(record) for record in records]
    return records


def create_member(username, description, password):
    # 向数据库中插入用户
    conn = sqlite3.connect("website_sample.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, description, password)"
                   " VALUES (?, ?, ?)",
                   (username, description, password))
    conn.commit()
    cursor.close()
    conn.close()

    gr.Info("创建用户成功!")
    return grm.Modal(visible=False)


def update_dataframes():
    return gr.update(samples=get_members())


def remove_member(username):
    # 不能删除admin用户
    if username == "admin":
        raise gr.Error("不能删除admin用户!")
    # 从数据库中删除用户
    conn = sqlite3.connect("website_sample.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE username=?", (username,))
    conn.commit()
    cursor.close()
    conn.close()

    gr.Info("删除用户成功!")


def select_member(record):
    username = record[0]
    gr.Info(f"选择用户: {username}")
    return username


def get_members_component():
    with gr.Blocks() as members:
        with grm.Modal(visible=False) as modal:
            with gr.Column(scale=1):
                pass
            with gr.Column(scale=1):
                username = gr.Textbox(label="Username")
                description = gr.TextArea(label="Description")
                password = gr.Textbox(label="Password", type="password")
                with gr.Row():
                    gr.Column()
                    with gr.Column():
                        with gr.Row():
                            modal_ok = gr.Button("OK", variant="primary",
                                                 size="sm")
                            modal_cancel = gr.Button("Cancel", size="sm")
                with gr.Row():
                    modal_ok_click = modal_ok.click(create_member,
                                                    [username,
                                                     description,
                                                     password],
                                                    [modal])
                    modal_cancel.click(lambda: grm.Modal(visible=False),
                                       None, [modal])
            with gr.Column(scale=1):
                pass

        with gr.Row():
            get_left_side_component()
            with gr.Column(scale=3):
                gr.HTML("<h1>Members</h1>")
                data_frame = gr.Dataset(headers=["username", "description"],
                                        components=["textbox", "textbox"])
                with gr.Row():
                    btn_refresh = gr.Button("Refresh")
                    btn_create_account = gr.Button("New Member")
                    btn_remove_account = gr.Button("Remove Member")

                btn_refresh.click(update_dataframes, outputs=[data_frame])
                btn_create_account.click(lambda: grm.Modal(visible=True),
                                         None, modal)
                modal_ok_click.success(update_dataframes,
                                       outputs=[data_frame])

                select_user = gr.State("")
                data_frame.click(fn=select_member, inputs=[data_frame],
                                 outputs=[select_user])
                btn_remove_account.click(remove_member, inputs=[select_user]) \
                    .success(update_dataframes, outputs=[data_frame])
        members.load(update_dataframes, outputs=[data_frame])

    return members


if __name__ == "__main__":
    get_members_component().launch()
