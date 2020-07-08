from flask import Flask
import requests
from twilio.twiml.messaging_response import MessagingResponse
from requests.api import request
 
app = Flask(__name__)

@app.route('/', methods=["POST"])
def index():
    new_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if 'quote' in new_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random' )
        if r.status_code == 200:
            data = r.json()
            quote = (f'{data["content"]} ({data["author"]})')

        else:
            quote = "I could not find a quote at this time, sorry"   



    if not responded:
        msg.body('I only know about famous quotes, sorry!')
    return str(resp)     

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)        
