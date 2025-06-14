import gradio as gr


def get_left_side_component():
    with gr.Column(scale=1) as left_side:
        gr.Button("Home", link="/home")
        gr.Button("Members", link="/members")
        gr.Button("Devices", link="/devices")
        gr.Button("Profile", link="/profile")
        gr.Button("About", link="/about")
        gr.Button("Logout", link="/home/logout")
    return left_side
