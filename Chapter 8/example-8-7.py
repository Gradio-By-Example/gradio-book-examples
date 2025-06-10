from gradio_client import Client
client = Client(src="http://127.0.0.1:7860/")

ret = client.predict("gradio", api_name="/greet_1")
print(ret)