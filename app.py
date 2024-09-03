import os
from flask import Flask, request, redirect, url_for, render_template
from twilio.rest import Client

app = Flask(__name__)

# Fetch Twilio credentials from environment variables
account_sid_on = os.getenv('TWILIO_ACCOUNT_SID_ON')
auth_token_on = os.getenv('TWILIO_AUTH_TOKEN_ON')
account_sid_off = os.getenv('TWILIO_ACCOUNT_SID_OFF')
auth_token_off = os.getenv('TWILIO_AUTH_TOKEN_OFF')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    action = request.form.get('action')
    if action == 'on':
        client = Client(account_sid_on, auth_token_on)
        function = '0n'
        message = client.messages.create(
            body=f'Dear Customer, Click www.jio.com/r/{function}h0t5p0t to tell us how we can make your experience on Jio network even better. Thank you, Team Jio',
            from_='+12566661972',
            to='+917723022755'
        )
    elif action == 'off':
        client = Client(account_sid_off, auth_token_off)
        function = '0ff'
        message = client.messages.create(
            body=f'Dear Customer, Click www.jio.com/r/{function}h0t5p0t to tell us how we can make your experience on Jio network even better. Thank you, Team Jio',
            from_='+12568294648',
            to='+917723022755'
        )
    else:
        return redirect(url_for('index'))

    print(message.sid)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
