📱 WhatsApp LLM Chatbot using Groq + Flask + Twilio

A simple WhatsApp AI Assistant that responds to messages using Groq Llama 3.1.
Built using Python, Flask, Twilio Sandbox & Ngrok, allowing real-time WhatsApp conversations with an AI model.

🚀 Features

Chat with AI directly inside WhatsApp

Uses Groq Llama 3.1 (Fast inference)

Built with Flask backend

Works via Twilio WhatsApp Sandbox

Ngrok exposes local server publicly for testing

Clean & minimal code structure

🏗 Tech Stack
Layer	Technology
Backend	Python + Flask
AI Model	Groq Llama 3.1
Messaging API	Twilio WhatsApp Sandbox
Tunnel	Ngrok
Secrets	.env (ignored by GitHub)
📂 Project Structure
whatsapp-llm-bot/
│── whatsapp_bot.py       # Main backend server
│── .env                  # API keys (NOT committed)
│── ngrok.exe             # Tunnel for public access
└── README.md             # Documentation

🔧 Setup Instructions
1️⃣ Clone repository
git clone https://github.com/shravyaz/whatsapp_llm_bot.git
cd whatsapp-llm-bot

2️⃣ Install dependencies
pip install flask groq python-dotenv

3️⃣ Create .env file and add your key
GROQ_API_KEY=your_groq_api_key

4️⃣ Run the backend
python whatsapp_bot.py

5️⃣ Start Ngrok tunnel
./ngrok.exe http 5000


Copy the https URL ngrok gives you.

6️⃣ Configure Twilio Webhook

Go to 👉 Twilio Console → Messaging Sandbox → Webhook URL field

https://<your-ngrok-url>/whatsapp


Save it.

🧪 Usage

Open WhatsApp

Send any message to your Twilio sandbox number

You will receive AI-generated replies instantly 🎉

⚠ Server must be running (python whatsapp_bot.py)
⚠ Ngrok must stay open for public access

🌱 Future Upgrades
Feature	Level
Chat memory	⭐⭐
Multi-user conversation	⭐⭐⭐
Deploy permanently to Render / AWS	⭐⭐⭐⭐
Convert to WhatsApp Business Cloud API	⭐⭐⭐⭐
📌 What I Learned

Connecting LLM with real-time messaging apps

Handling API requests & responses

Using environment variables securely

Working with Twilio webhooks & ngrok tunnels

If you like this project ⭐ Star the repo!
Want to deploy permanently? Just ask "Help me deploy WhatsApp bot to cloud" 🚀