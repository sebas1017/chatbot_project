
## EJECUTAR EN PRODUCCION (AWS EC2)

docker-compose up

aqui es clave que anote la direccion ip publica de su maquina aws hacia el puerto 5000 y debera dirigirse  a la configuracion de twilio en el 
sandbox de whatsapp para lo cual debio haberse logeado con una cuenta gratuita , y poner esa ip y puerto en la configuracion de twilio para mensajes entrantes
para esto se recomienda que en su instancia de aws ec2 configure una direccion ip elastica
 ![alt text](https://github.com/sebas1017/chatbot_project/blob/main/sandbox_configuration_whatsapp.png/?raw=true)


luego de tener el contenedor corriendo en su instancia de AWS EC2 en el puerto 5000 

# +1 415 5238886


una vez agregado a whatsapp escribir como mensaje este codigo

# join town-map

y luego de esto podra escribir cualquier mensaje desde whatsapp e inmediatamente en los logs de la consola de 
Flask debera poder visualizar el mensaje que ha sido enviado desde whatsapp


actualmente el chatbot retorna imagenes aleatorias de gatos escribiendo la palabra cat
y tambien retornara datos a whatsapp si escribe la palabra quote


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







