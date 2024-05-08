# Descripción

Este proyecto consiste en un bot para Twitter que se conecta a la API de OpenAI para generar una frase aleatoria. La frase generada se publica diariamente en la cuenta asociada de Twitter y se almacena en una base de datos para su registro. El bot automatiza este proceso, asegurando una publicación regular de contenido inspirador en la plataforma de Twitter.

# Guía de Instalación y Uso

Este proyecto requiere ciertos pasos de configuración y ejecución para su funcionamiento adecuado. A continuación, se detallan los pasos necesarios para su instalación y uso:

## Configuración de Credenciales

Antes de utilizar este proyecto, asegúrate de tener las credenciales necesarias y añadirlas a un archivo `.env`. Las credenciales son requeridas para el correcto funcionamiento de ciertos componentes del sistema.

````plaintext
# Archivo .env
twitter_api_key = 
twitter_api_secret = 
twitter_bearer_token = 
twitter_access_token = 
twitter_access_token_secret = 
openai_token =
save_on_db=true
db_username=postgres
db_password=
db_databa_name=
db_host=
db_engine=
db_port=
````

## Instalación de Dependencias

Para instalar las dependencias requeridas, ejecuta el siguiente comando en tu entorno de desarrollo:

````bash
pip install -r requirements.txt
````

Este comando instalará todas las bibliotecas y paquetes necesarios para ejecutar el proyecto.

## Ejecución del Proyecto

Una vez configuradas las credenciales y instaladas las dependencias, puedes iniciar el proyecto ejecutando el siguiente comando:

````bash
python main.py
````

Este comando lanzará la aplicación y la pondrá en funcionamiento, permitiéndote interactuar con ella según la funcionalidad deseada.

## Uso con Docker

Si prefieres ejecutar este proyecto utilizando Docker, sigue los siguientes pasos:

### 1. Crear archivo stack.env

Primero, crea un archivo llamado `stack.env` en la raíz del proyecto. Este archivo contendrá las variables de entorno necesarias para la configuración del contenedor Docker.

A continuación, agrega las variables de entorno anterior al archivo `stack.env`:

Asegúrate de reemplazar los valores de las credenciales con tus propias claves y tokens.

### 2. Ejecutar Docker Compose

Una vez que hayas configurado las variables de entorno en el archivo `stack.env`, puedes iniciar el contenedor Docker ejecutando el siguiente comando en la terminal:

```bash
docker-compose up
``` 
