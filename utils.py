import json

def cargar_configuracion(path):
    with open(path, 'r') as f:
        return json.load(f)
