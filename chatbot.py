import streamlit as st
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

# Cargar el modelo preentrenado y el tokenizador
model_name = "gpt2"
model = TFGPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Función para generar texto
def generate_text(prompt, max_length=50):
    inputs = tokenizer.encode(prompt, return_tensors="tf")
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text

# Inicializar la sesión de Streamlit para mantener el historial de mensajes
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Interfaz de chat
st.title("Generative AI Chatbot")
st.write("Simula una conversación con el chatbot generativo de IA.")

# Caja de texto para la entrada del usuario
user_input = st.text_input("Escribe tu mensaje:", "")

# Botón para enviar el mensaje
if st.button("Enviar"):
    if user_input:
        # Guardar el mensaje del usuario
        st.session_state['messages'].append({"role": "user", "content": user_input})
        # Generar respuesta del chatbot
        response = generate_text(user_input)
        # Guardar la respuesta del chatbot
        st.session_state['messages'].append({"role": "bot", "content": response})
        user_input = ""

# Mostrar el historial de mensajes
for message in st.session_state['messages']:
    if message['role'] == 'user':
        st.markdown(f"**Tú:** {message['content']}")
    else:
        st.markdown(f"**Chatbot:** {message['content']}")

# Estilo adicional para mejorar la interfaz
st.markdown("""
<style>
    .css-1aumxhk {
        text-align: center;
    }
    .css-9s5bis.edgvbvh3 {
        background-color: #f0f2f6;
        border: 1px solid #ddd;
        padding: 10px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)
