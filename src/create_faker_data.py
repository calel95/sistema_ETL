from faker import Faker
import json
from tqdm import tqdm 
import csv
import os
import re

faker = Faker()
Faker.seed(0)

class Gerador:
    def __init__(self) -> None:
        self.lista = []


    def generator_of_registers(self,register_number: int):
        for _ in tqdm(range(register_number), desc="Generating registers"):
            number_float = faker.pyfloat(left_digits=4,right_digits=2,positive=True)
            register = faker.json(data_columns={"ID": "uuid4",
                                        "Name": "name",
                                        "created_at": "iso8601",
                                        "Salary": number_float}
                                        ,num_rows=1) #por padrao ele grava o dicionario como string
            
            register = json.loads(register) #converte a string json em um dicionario python

            self.lista.append(register)

    def output_csv(self, file_name: str):
        file_path_old = os.getcwd()
        file_path = file_path_old.replace("src","data/csv/").replace('\\','/')
        file_path_new = file_path+file_name+".csv"
        with open (file_path_new, "w", newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["ID", "Name", "created_at", "Salary"], delimiter=";")
            writer.writeheader()
            for row in self.lista:
                writer.writerow(row)

        print(f"Archive genetored in {file_path_new}")

    def output_json(self, file_name: str):
        file_path_old = os.getcwd()
        file_path = file_path_old.replace("src","data/json/").replace('\\','/')
        file_path_new = file_path+file_name+".json"
        with open (file_path_new, "w") as json_file:
            json.dump(self.lista,json_file, indent=4, ensure_ascii=False)

        print(f"Archive genetored in {file_path_new}")






# lista = []""
# faker = Faker()
# Faker.seed(0)
# number_register = 100
# for _ in range(number_register):
#     #faker.json(data_columns={"produto": "name","preco": 50, "created_at": "2024-09-15T19:33:06.675Z", "id": faker.uuid4()}, num_rows=2)
#     number_float = faker.pyfloat(left_digits=4,right_digits=2,positive=True)
#     x = faker.json(data_columns={"ID": "uuid4","Name": "name", "created_at": "iso8601", "salario": number_float}, num_rows=1) #por padrao ele grava o dicionario como string
#     x = json.loads(x) #converte a string json em um dicionario python

#     # x = {
#     #         "ID": str(faker.uuid4()),  # Gera um UUID
#     #         "Name": faker.name(),      # Gera um nome
#     #         "created_at": faker.iso8601(),  # Gera uma data ISO 8601
#     #         "salario": number_float     # Adiciona o salário gerado
#     #     }
    

#     lista.append(x)

#     #faker.uid

# #print(lista)
# print(lista)
# #faker.random_company_product

# #lista = json(lista)
# file_name = "arquivo_teste1"
# file_path = f"C:/Users/Calel/OneDrive/Área de Trabalho/Python/sistema_ETL/data/json/{file_name}.json"
# print(file_path)

# with open (file_path, "w") as json_file:
#     json.dump(lista,json_file, indent=4, ensure_ascii=False)

# print(f"Arquivo gerado em {file_path}")