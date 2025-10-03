# Multi-Business WhatsApp Enquiry Bot (4U Gym & International Karate Center)

This project provides a flexible WhatsApp enquiry bot you can deploy on Render and connect to Twilio.
It supports multiple business configs (4U Gym and International Karate Center). Use the BUSINESS_KEY env var to select which business this instance will serve.

## What's included
- app.py: Flask webhook that handles incoming WhatsApp messages from Twilio
- config.py: business data for 4U Gym and International Karate Center
- templates/: simple index page
- requirements.txt, Procfile, .env.example

## Features
- Sends a numbered "menu" (table-like) to users. Users reply with a number to choose.
- Keyword matching for common queries.
- "Talk to a Human" option which displays contact numbers / emails.
- Ready to deploy on Render. Replace env vars with your Twilio credentials.

---
## Deployment - Step by step (detailed)

### 1) Prepare code locally
1. Download and extract this project.
2. Copy `.env.example` to `.env` and fill in the values:
   - `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` from Twilio Console.
   - `TWILIO_WHATSAPP_FROM` is your Twilio WhatsApp number (format: whatsapp:+<countrycode><number>).
   - `BUSINESS_KEY` - either `4U_Gym` or `Karate_Center` (choose which bot this instance will serve).
   - `FLASK_SECRET` - random secret for Flask sessions.

### 2) Local test (optional, recommended)
1. Create and activate a Python virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # mac/linux
   .venv\\Scripts\\activate     # windows powershell
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Use `ngrok` to expose local server to the internet for Twilio testing:
   ```bash
   ngrok http 5000
   ```
   Note the `https://...` forwarding URL from ngrok.

5. In Twilio Console (Messaging > Try it Out > Send a WhatsApp message / or Sandbox):
   - For Sandbox, configure the "WHEN A MESSAGE COMES IN" webhook to: `https://<ngrok-url>/webhook`
   - For a production Twilio WhatsApp number, set the webhook for incoming messages to: `https://<ngrok-url>/webhook`

6. Send a WhatsApp message to the Twilio number from your phone to test. Type `hi` or `menu` to get started.

### 3) Deploy to Render (recommended for 24/7 uptime)
1. Push this project to a GitHub repository.
2. Create a new Web Service on Render and connect your GitHub repo.
3. In Render settings:
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
4. Add Environment Variables in Render Dashboard (Environment > Environment Variables):
   - `TWILIO_ACCOUNT_SID` = your SID
   - `TWILIO_AUTH_TOKEN` = your Auth Token
   - `TWILIO_WHATSAPP_FROM` = your Twilio WhatsApp number (e.g. whatsapp:+1415...)
   - `BUSINESS_KEY` = 4U_Gym  (or Karate_Center)
   - `FLASK_SECRET` = replace_with_random_string
5. Deploy the service. Once live, copy the service URL (e.g. `https://your-app.onrender.com`)

6. In Twilio Console, set the webhook for your number to:
   `https://<your-render-service-url>/webhook`

7. Test from your phone by sending `hi` to your Twilio WhatsApp number.

---
## Notes about interactive buttons / list messages
- This starter uses a *numbered menu* which is simple and works reliably with Twilio's incoming webhook and replies.
- Twilio supports richer **interactive messages (List, Buttons)** via WhatsApp templates and the Twilio API. If you'd like a clickable list menu (native UI inside WhatsApp), we can add that later — it requires additional Twilio template configuration or using the Twilio API to send interactive payloads. This starter is robust and works in all accounts immediately.

## Customization
- Edit `config.py` to change menu items, wording, phone numbers, hours, and other business info.
- To run two bots simultaneously, deploy two instances to Render and set `BUSINESS_KEY` to different values for each.

---
If you want, I can now:
- Create two separate Render services (one for each business) and give exact Render + Twilio setup commands,
- Or walk you step-by-step through deploying the first bot to Render and connecting Twilio.

