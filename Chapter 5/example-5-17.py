import gradio as gr
import time

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        chat_history.append({"role": "user", "content": message})
        chat_history.append({"role": "assistant", "content": "..."})
        yield "", chat_history

        for response_message in ["How are you?", "I love you", "I'm very hungry"]:
            time.sleep(2)
            if chat_history[-1]["role"] == "assistant" and chat_history[-1]["content"] == "...":
                chat_history[-1]["content"] = f"{response_message} {message}."
            else:
                chat_history[-1]["content"] += f"\n{response_message} {message}."
            yield "", chat_history
    msg.submit(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch()