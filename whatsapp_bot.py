from flask import Flask, request
from groq import Groq
import os
from dotenv import load_dotenv


load_dotenv()


app = Flask(__name__)

# Load Groq key (we will set env var later)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_llm(prompt):
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful WhatsApp assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return completion.choices[0].message.content.strip()

@app.route("/whatsapp", methods=["POST"])
def reply_whatsapp():
    incoming_msg = request.form.get("Body")

    reply = ask_llm(incoming_msg)

    # Twilio XML Response
    return f"""
        <Response>
            <Message>{reply}</Message>
        </Response>
    """

if __name__ == "__main__":
    app.run(port=5000)
