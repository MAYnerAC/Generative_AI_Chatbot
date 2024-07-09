import streamlit as st
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

model_name = "gpt2"
model = TFGPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def generate_text(prompt, max_length=50, temperature=0.7, no_repeat_ngram_size=2):
    inputs = tokenizer.encode(prompt, return_tensors="tf")
    outputs = model.generate(
        inputs, 
        max_length=max_length, 
        num_return_sequences=1, 
        temperature=temperature,
        no_repeat_ngram_size=no_repeat_ngram_size
    )
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text


if 'messages' not in st.session_state:
    st.session_state['messages'] = []

st.title("Generative AI Chatbot")
st.write("Simula una conversación con el chatbot generativo de IA.")

user_input = st.text_input("Escribe tu mensaje:", "")

if st.button("Enviar"):
    if user_input:
        st.session_state['messages'].append({"role": "user", "content": user_input})
        response = generate_text(user_input)
        st.session_state['messages'].append({"role": "bot", "content": response})
        user_input = ""

for message in st.session_state['messages']:
    if message['role'] == 'user':
        st.markdown(f"**Tú:** {message['content']}")
    else:
        st.markdown(f"**Chatbot:** {message['content']}")

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
