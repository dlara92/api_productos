# **Products API service**
# Created on Nov 7, 2020
# @authors: DANIEL LARA (daniel.lara.p92@gmail.com)

Este archivo describe la instalación y el uso del servicio **Products API service**
 
# Instalar Aplicación
Se describe el procedimiento de instalación para Linux y Windows

### Crear Ambiente virtual
```bash
pip3 install virtualenv
python3 -m venv venv
```

### Activar el ambiente virtual
```bash
# linux
source venv/bin/activate
# windows
venv\Scripts\activate.bat
```

### Instala los requerimientos
```
pip install -r requirements.txt
```
 
# Correr Aplicacion
```bash
# linux
source venv/bin/activate
export FLASK_ENV=development
env FLASK_APP=app.py flask run -h 0.0.0.0 -p 5000
 
# windows
venv\Scripts\activate.bat
set FLASK_ENV=development
set FLASK_APP=app.py 
python -m flask run -h 0.0.0.0 -p 5000
```

También están disponibles en este empaquetado los archivos "run.bat" y "run.sh" para la ejecución automática en Windows y
Linux respectivamente.
En Windows: Abrir una ventana del "Símbolo del Sistema". Ubicarse en la carpeta donde instaló el proyecto y escriba: run.bat
En Linux: Abrir una ventana de terminal. Ubicarse en la carpeta donde instaló el proyecto y escriba: bash run.sh
