from faker import Faker
import json


lista = []
faker = Faker()
Faker.seed(0)
for _ in range(5):
    #faker.json(data_columns={"produto": "name","preco": 50, "created_at": "2024-09-15T19:33:06.675Z", "id": faker.uuid4()}, num_rows=2)
    number_float = faker.pyfloat(left_digits=4,right_digits=2,positive=True)
    #x = faker.json(data_columns={"ID": "uuid4","Name": "name", "created_at": "iso8601", "salario": number_float}, num_rows=1)

    x = {
            "ID": str(faker.uuid4()),  # Gera um UUID
            "Name": faker.name(),      # Gera um nome
            "created_at": faker.iso8601(),  # Gera uma data ISO 8601
            "salario": number_float     # Adiciona o salário gerado
        }


    lista.append(x[0])

    #faker.uid

#print(lista)
print(lista)
#faker.random_company_product

#lista = json(lista)

file_path = "C:/Users/Calel/OneDrive/Área de Trabalho/Python/sistema_ETL/data/json/weste.json"

with open (file_path, "w") as json_file:
    json.dump(lista,json_file, indent=4, ensure_ascii=False)

print(f"Arquivo gerado em {file_path}")