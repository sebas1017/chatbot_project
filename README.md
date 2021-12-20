# chatbot_project


ejecutar en la raiz 
# ./ngrok authtoken 22N8lcUc5fryVtkCeMrm47W4krl_3WCavMaM7Qa6h9BTq1kLa

luego ejecutar 
# ./ngrok http 5000

luego crear entorno virtual del proyecto ( ubuntu)

# python3 -m venv venv

activar el entorno

# source venv/bin/activate


luego instalar dependencias

# pip install -r requirements.txt


luego correr el script

# python3 bot.py

Una vez realizado todo esto debe ir a whatsapp en su telefono movil y escribir al siguiente telefono



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
de nuestra maquina , todo esto por estar en la fase de desarrollo






## EJECUTAR EN PRODUCCION (AWS EC2)

docker-compose up

y repetir los pasos de escribir al whatsapp el codigo de autenticacion y la palabra a buscar en el chat (pueden ser cualquier palabra ya que esto filtra y raspa los datos de amazon)
