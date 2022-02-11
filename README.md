# Pokeapi
Una aplicacion de prueba para consumir recursos de pokeapi.co

## Instalacion

### Paso 1: Gt clone al proyecto en la carpeta deseada
    git clone https://github.com/hilario-wh/pokeapi.git
### Paso 2: Creacion del entorno en la carpeta deseada
    mkvirtualenv envpokeapi -p=2.7
#### Confirmar que sea en python 2.7
    python -V
### Paso 3: Iniciar el entorno

#### Con virtualenvwrapper
    workon envpokeapi
#### ó con virtualenv
    source bin/activate
### Paso 4: instalamos dependencias en el entorno virtual
    pip install  -r requeriments.txt
### Paso 5: Iniciar el proyecto:
    ./manage.py runserver