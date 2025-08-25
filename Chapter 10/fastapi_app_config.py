import secrets

import gradio as gr
from starlette.routing import Mount


def fastapi_app_config(app, mount_path_list, auth):
    """ 将gradio应用挂载到fastapi应用上，实现会话状态共享
    :param app: fastapi应用
    :param mount_path_list: 挂载路径和gradio应用的映射
    :param auth: 鉴权函数
    """
    for mount_path, mount_app  in mount_path_list.items():
        gr.mount_gradio_app(app, mount_app, path=mount_path, auth=auth)

    _cookie_id = secrets.token_urlsafe(32)
    _tokens = {}

    mount_map = {m.path: m for m in app.routes
                 if isinstance(m, Mount)}
    for mount_path in mount_path_list.keys():
        mount_map[mount_path].app.cookie_id = _cookie_id
        mount_map[mount_path].app.tokens = _tokens