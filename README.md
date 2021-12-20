
## EJECUTAR EN PRODUCCION (AWS EC2)

docker-compose up

aqui es clave que anote la direccion ip publica de su maquina aws hacia el puerto 5000 y debera dirigirse  a la configuracion de twilio en el 
sandbox de whatsapp para lo cual debio haberse logeado con una cuenta gratuita , y poner esa ip y puerto en la configuracion de twilio para mensajes entrantes
para esto se recomienda que en su instancia de aws ec2 configure una direccion ip elastica
 ![alt text](https://github.com/sebas1017/chatbot_project/blob/main/sandbox_configuration_whatsapp.png/?raw=true)
 
 en este caso el endpoint de flask que hace el raspado de datos hacia amazon es http://ip:5000/bot  y esta va en la configuracion de twilio como 
 se ve en la siguiente imagen
 en mi caso he configurado una direccion ip elastica para que la direccion ip no cambie cada vez que reiniciemos la maquina aws 


luego de tener el contenedor corriendo en su instancia de AWS EC2 en el puerto 5000 y haber agregado la ip a la configuracion  de twilio
debera escribir atraves de whatsapp a este numero

# +1 415 5238886


una vez agregado a whatsapp escribir como mensaje este codigo

# join town-map

y luego de esto podra escribir la palabra del producto que desea obtener el link de referencia en amazon
por ejemplo:
televisor


actualmente retorna la lista de 5 urls referentes al producto que busco en amazon de acuerdo a los resultados de amazon


Nota:
ngrok y python deben correr en el mismo puerto 5000 , esto no causara error ya que ngrok
realizar una redireccion del trafico http atraves del tunel de twilio  hacia nuestro puerto local
de nuestra maquina , todo esto por estar en la fase de desarrollo, ESTO SOLO PARA EL CASO DE EJECUTARLO LOCALMENTE

## EJECUCION LOCAL
./ngrok http 5000 
y en otra terminal 
python3 -m venv venv
source /venv/bin/activate
pip install -r requirements.txt
python3 bot.py

y en la configuracion de twilio debera pegar la salida del comando ./ngrok http 5000 en el parametro url forwarding , debera copiar
ese url en la configuracion de twilio ya que esto debe redirigir el trafico del chat de whatsapp entrante a su puerto local
(todo esto solo en caso de tener que ejecutarlo localmente)







