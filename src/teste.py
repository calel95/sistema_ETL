from openai import OpenAI
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY,
                organization="org-A3JkXtHMhCov5RgteRlpCgeK",
                project="proj_lO7EfhSBhcPNC2mRr7eWDviq")

mensagens = [
    {'role': 'system', 'content': 'Você é um especialista na biblioteca do faker("pt_BR") do python, voce precisa usar a funcao mais adequada do faker de acordo com o nome da coluna que usuario digitar. Digite apenas o nome da funcao. Exemplo faker.pyint(), faker.name()'},
    {'role': 'user', 'content': 'endereço'}
]

resposta = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=mensagens,
    max_tokens=50,
    temperature=0.7,
)

mensagem_resp = resposta.choices[0].message.content
print(mensagem_resp)
