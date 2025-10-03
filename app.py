import os
from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
from config import BUSINESSES, DEFAULT_BUSINESS_KEY
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Which business this instance will serve. Change BUSINESS_KEY env var to switch.
BUSINESS_KEY = os.getenv("BUSINESS_KEY", DEFAULT_BUSINESS_KEY)
BUSINESS = BUSINESSES.get(BUSINESS_KEY)
if not BUSINESS:
    raise RuntimeError(f"Business config for '{BUSINESS_KEY}' not found in config.py")

def render_menu_text(biz):
    # Create a table-like menu with numbers (users can tap the number to reply)
    lines = []
    lines.append(f"*Welcome to {biz['name']}* \n")
    lines.append("Please choose an option by replying with the number (e.g. '1'):\n")
    menu = biz.get('menu', [])
    for i, item in enumerate(menu, start=1):
        lines.append(f"{i}. {item}")
    lines.append("\nReply with the number of your choice, or type your question.")
    return "\n".join(lines)

def handle_choice(choice_idx, biz):
    idx = int(choice_idx) - 1
    menu = biz.get('menu', [])
    if idx < 0 or idx >= len(menu):
        return "Sorry, that's not a valid option. Reply 'menu' to see the options again."
    key = menu[idx]
    responses = biz.get('responses', {})
    resp = responses.get(key, "Sorry, no info available.")
    # After certain responses we may prompt with quick next actions (simulated reply buttons)
    follow = biz.get('followups', {}).get(key)
    if follow:
        resp = resp + "\n\n" + follow
    return resp

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', business=BUSINESS)

@app.route('/webhook', methods=['POST'])
def webhook():
    """Main webhook endpoint for Twilio WhatsApp messages."""
    incoming = request.values.get('Body', '').strip()
    sender = request.values.get('From', 'unknown')
    app.logger.info(f"Incoming message from {sender}: {incoming}")

    resp = MessagingResponse()
    msg = resp.message()

    if not incoming:
        msg.body(render_menu_text(BUSINESS))
        return str(resp)

    text = incoming.lower()
    # shortcuts
    if text in ('menu', 'start', 'hi', 'hello', 'hey'):
        msg.body(render_menu_text(BUSINESS))
        return str(resp)

    # If user replied with a single number like '1', '2', etc. handle it
    if text.isdigit():
        try:
            reply = handle_choice(text, BUSINESS)
            msg.body(reply)
            return str(resp)
        except Exception as e:
            app.logger.exception('Error handling numeric choice')
            msg.body("Sorry, something went wrong. Reply 'menu' to see options.")
            return str(resp)

    # Try to match keywords (e.g., 'membership', 'plans', 'facilities')
    for k, keywords in BUSINESS.get('keywords', {}).items():
        for kw in keywords:
            if kw in text:
                reply = BUSINESS['responses'].get(k, None)
                if reply:
                    msg.body(reply)
                    return str(resp)

    # Fallback
    msg.body(BUSINESS.get('fallback', "I didn't quite get that. Reply 'menu' to see options."))
    return str(resp)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
