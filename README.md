# fb-downloader

Script para descargar videos y streams de Facebook en secciones

## Requisitos

### Python 3.8

Este script se ejecuta correctamente con una versión de (Python)[https://python.org/downloads] arriba de 3.8.

### YT-DLP

Al tener instalado Python 3.8 (o superior) aseguramos de usar una versión más reciente de YT-DLP, ya que por algunos bloqueos de la plataforma (Fb), no podremos descargar los streams.

Para instalar de forma global YT-DLP debemos ejecutar el siguiente comando:

```sh
pip3 install "yt-dlp[default]"
```

Considere que este comando puede ejecutarse como superusuario del sistema.

## Ejecución

Una vez cubiertos los requisitos podemos ejecutar el script de la siguiente forma:

```sh
python3 script.py <url-de-fb>
```

Sustituyendo `<url-de-fb>` con la URL de la que queremos descargar el video o stream.
