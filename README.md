# Create a Generative AI Chatbot with Python, Streamlit, and Transformers

Este proyecto demuestra cómo crear un chatbot de IA generativo utilizando Python, Transformers y TensorFlow. El chatbot utiliza un modelo GPT-2 previamente entrenado para generar respuestas de texto basadas en la entrada del usuario.

## Instrucciones de configuración

### Requisitos previos

- Python 3.7 o superior
- pip (instalador del paquete Python)

### Crear Entorno

```sh
python -m venv env

. env/Scripts/activate

deactivate
```

### Instalar Dependecias

```sh
pip install tensorflow streamlit transformers
```

O

```sh
pip install tensorflow
pip install streamlit
pip install transformers
```

### Guardar en "requirements.txt"

```sh
pip freeze > requirements.txt
pip install -r requirements.txt
```

### Ejecucion del Chatbot

```sh
streamlit run chatbot.py
```
