from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    print("entre")
    incoming_msg = request.values.get('Body', '').lower()
    print("ESTE ES EL MENSAJE ENTRANTE DESDE EL CHAT DE WHATSAPP")
    print(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'No puedo responder a esa peticion lo siento'
        msg.body(quote)
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        msg.body('Solo tenemos imagenes de gatos lo sentimos')
    return str(resp)


if __name__ == '__main__':
    app.run(port=5000)