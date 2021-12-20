from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import logging
from twilio.twiml.messaging_response import MessagingResponse
app = Flask(__name__)




logging.error("AMAZON BOT")
@app.route("/bot", methods=["POST"])
def bot():
    resp = MessagingResponse()
    msg = resp.message()
    word = request.values.get("Body", "").lower()
    url = f"https://www.amazon.com/-/es/s?k={word}&language=es"
    headers = {"FUser":"An","user-agent":"an"}
    response = requests.get(url,headers=headers)
    logging.error(f"RESPONSE_STATUS_CODE {response.status_code}")
    if response.status_code == 200:
        try:
            soup = BeautifulSoup(response.content,"html.parser")
            urls = soup.find("div", 
                            attrs={"class":"s-main-slot s-result-list s-search-results sg-row"}
                            ).find_all("a",attrs={"class":"a-link-normal a-text-normal"})
            urls = ["https://www.amazon.com"+ item.get('href') for item in urls[:5] ]
            response_final = "\n\n URL \n".join(urls)
            msg.body(response_final)
            return str(resp)
        except Exception as e:
            msg.body(f"sin resultados para {word}")
            logging.error("Esta es la excepcion")
            logging.error(e)
            logging.error("Contenido de la respuesta")
            logging.error(response.content)
            return str(resp)
    else:
        msg.body('Lo sentimos , su busqueda no ha tenido resultados intente con otro articulo')
        return str(resp)
    

if __name__ == "__main__":
    app.run(port=5000)
