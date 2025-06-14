import secrets

import gradio as gr
from starlette.routing import Mount


def fastapi_app_config(app, mount_path_list, auth):
    for mount_path, mount_app  in mount_path_list.items():
        gr.mount_gradio_app(app, mount_app, path=mount_path, auth=auth)

    _cookie_id = secrets.token_urlsafe(32)
    _tokens = {}

    mount_map = {m.path: m for m in app.routes
                 if isinstance(m, Mount)}
    for mount_path in mount_path_list.keys():
        mount_map[mount_path].app.cookie_id = _cookie_id
        mount_map[mount_path].app.tokens = _tokens
