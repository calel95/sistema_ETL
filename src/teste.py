import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()

mensagens = [
    {'role': 'system', 'content': 'Você precisa classificar o tipo da funcao da biblioteca Faker da palavra que for passada. Diga apenas o tipo em uma palavra, e nada mais'},
    {'role': 'user', 'content': 'nome'}
]

resposta = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=mensagens,
    max_tokens=50,
    temperature=0.7,
)

mensagem_resp = resposta.choices[0].message.content
print(mensagem_resp)