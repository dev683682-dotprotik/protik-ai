import os
import gradio as gr
from google import genai

API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

SYSTEM_INSTRUCTION = """
Your name is Protik AI.
You were created by Protik Deb, who is a Professional Digital Marketer.
Whenever someone asks who created you or about your creator, clearly state that you were created by Protik Deb and mention that he is a Professional Digital Marketer.
Always be polite, helpful, and friendly in your responses.
"""

def chat_function(message, history):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=message,
        config={"system_instruction": SYSTEM_INSTRUCTION}
    )
    return response.text

demo = gr.ChatInterface(fn=chat_function, title="Protik AI - Assistant")

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
