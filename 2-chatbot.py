import openai
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()

# Lê a chave da API do ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")

def geracao_texto(mensagens):
    resposta = openai.ChatCompletion.create(
        messages=mensagens,
        model="gpt-3.5-turbo-0125",
        temperature=0,
        max_tokens=1000,
        stream=True
    )
    print("Bot:", end=" ")
    texto_completo = ""
    for resposta_stream in resposta:
        delta = resposta_stream.choices[0].delta
        if 'content' in delta:
            texto = delta.content
            print(texto, end="")
            texto_completo += texto
    print()
    mensagens.append({"role": "assistant", "content": texto_completo})
    return mensagens

if __name__ == "__main__":
    print("Bem-vindo ao Chatbot!")
    mensagens = []
    while True:
        in_user = input("User: ")
        if in_user.lower() in ["sair", "exit", "quit"]:
            break
        mensagens.append({"role": "user", "content": in_user})
        mensagens = geracao_texto(mensagens)
