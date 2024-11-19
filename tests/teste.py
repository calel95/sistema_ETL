from openai import OpenAI
import os




def definir_tipo_campo():
    dicionario = {}
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=OPENAI_API_KEY,
                organization="org-A3JkXtHMhCov5RgteRlpCgeK",
                project="proj_lO7EfhSBhcPNC2mRr7eWDviq")
    
    while True:       
        campo = input("Digite o nome do campo (ou 'sair' para encerrar): ")
        if campo.lower() == 'sair':
            print(dicionario)
            break
        try:
            mensagens = [
            {'role': 'system', 'content': 'Você é um especialista na biblioteca do faker("pt_BR") do python, voce precisa usar a funcao mais adequada do faker de acordo com o nome da coluna que usuario digitar. Digite apenas o nome da funcao. Exemplo faker.pyint(), faker.name()'},
            {'role': 'user', 'content': campo}
            ]

            response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=mensagens,
            max_tokens=50,
            temperature=0.7,
            )

            type_column = response.choices[0].message.content
            print(f"O campo '{campo}' provavelmente deve ser do tipo: {type_column}")
            dicionario[f"{campo}"] = f"{type_column}"
        except Exception as e:
            print(f"Ocorreu um erro ao processar o campo: {e}")
            #print(type_column)
            return dicionario


dicionario = definir_tipo_campo()

print(type(dicionario))

# while True:
#     campo = input("Digite o nome do campo (ou 'sair' para encerrar): ")
#     if campo.lower() == 'sair':
#         print(dicionario)
#         break
#     try:
#         tipo = definir_tipo_campo(campo)
#         print(f"O campo '{campo}' provavelmente deve ser do tipo: {tipo}")
#         dicionario[f"{campo}"] = f"{tipo}"
#     except Exception as e:
#         print(f"Ocorreu um erro ao processar o campo: {e}")
