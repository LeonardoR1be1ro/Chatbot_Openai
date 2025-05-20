import os
from datetime import datetime
from dotenv import load_dotenv
import openai

def get_greeting() -> str:
    """Retorna saudação com base na hora atual."""
    hour = datetime.now().hour
    if hour < 12:
        return "Bom dia!"
    elif hour < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"

def load_api_key():
    """Carrega a chave da API do arquivo .env"""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("API key não encontrada. Verifique seu arquivo .env.")
    return api_key

def chat():
    openai.api_key = load_api_key()

    print(get_greeting())
    print("Faça sua pergunta ao ChatGPT (digite 'sair' para encerrar):\n")

    while True:
        user_input = input("Você: ").strip()
        if user_input.lower() in {"sair", "exit", "quit"}:
            print("Encerrando o chat. Até logo!")
            break

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um assistente que responde em português."},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.7,
                max_tokens=1000,
            )
            reply = response['choices'][0]['message']['content']
            print(f"ChatGPT: {reply}\n")
        except Exception as e:
            print(f"Erro ao se comunicar com a API: {e}")

if __name__ == "__main__":
    chat()
