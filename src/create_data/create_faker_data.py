from faker import Faker
import json
from tqdm import tqdm 
import csv
import os
import re
from multiprocessing import Pool
from openai import OpenAI
from typing import Literal

faker = Faker()
#Faker.seed(0)

class Gerador:
    def __init__(self) -> None:
        self.lista = []
        self.dicionario = {}
    
    def definir_tipo_campo(self):
        self.dicionario = {}
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        client = OpenAI(api_key=OPENAI_API_KEY,
                    organization="org-A3JkXtHMhCov5RgteRlpCgeK",
                    project="proj_lO7EfhSBhcPNC2mRr7eWDviq")
        
        while True:       
            campo = input("Digite o nome do campo (ou 'sair' para encerrar): ")
            if campo.lower() == 'sair':
                print(self.dicionario)
                break
            try:
                mensagens = [
                {'role': 'system', 'content': 'Você é um especialista na biblioteca do faker("pt_BR") do python, voce precisa usar a funcao mais adequada do faker de acordo com o nome da coluna que usuario digitar, se necessario pode adicionar parametros. Digite apenas o nome da funcao. Exemplo faker.pyint(), faker.name()'},
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
                self.dicionario[f"{campo}"] = f"{type_column}"
            except Exception as e:
                print(f"Ocorreu um erro ao processar o campo: {e}")
                #print(type_column)
            print(self.dicionario)
        return self.dicionario
            
    def generator_teste(self,register_number: int,format: Literal["Dict","List"]):
        #self.lista.append([i for i in self.dicionario.keys()])
        #self.lista.append(list(self.dicionario.keys()))  
        if format == "Dict":
            for _ in tqdm(range(register_number), desc="Generating registers"):
                registro = {}
                # register = {"id": faker.sha1(),
                #             "name": faker.name(),
                #             "created_at": faker.iso8601(),
                #             "salary": faker.pyfloat(left_digits=4,right_digits=2,positive=True),
                #             "active": faker.pybool()}          
                for coluna, funcao in self.dicionario.items():
                # Avalia a função faker armazenada como string e atribui o valor ao registro
                    #print("AA=",self.dicionario[coluna])
                    #print("BB=", list(self.dicionario[coluna])[0])
                #    self.dicionario[coluna] = funcao
                #print(list(self.dicionario.values()))
                    registro[coluna] = eval(funcao)
                self.lista.append(registro)

            print(self.lista)
        else:
            self.lista.append(list(self.dicionario.keys())) 
            for _ in tqdm(range(register_number), desc="Generating registers"):
                registro = []
                # register = {"id": faker.sha1(),
                #             "name": faker.name(),
                #             "created_at": faker.iso8601(),
                #             "salary": faker.pyfloat(left_digits=4,right_digits=2,positive=True),
                #             "active": faker.pybool()}          
                for coluna, funcao in self.dicionario.items():
                # Avalia a função faker armazenada como string e atribui o valor ao registro
                    #print("AA=",self.dicionario[coluna])
                    #print("BB=", list(self.dicionario[coluna])[0])
                #    self.dicionario[coluna] = funcao
                #print(list(self.dicionario.values()))
                    registro.append(eval(funcao))
                self.lista.append(registro)

            print(self.lista)
        return self.lista

    def generator_of_registers_dict(self,register_number: int):
        for _ in tqdm(range(register_number), desc="Generating registers"):
            register = {"id": faker.sha1(),
                        "name": faker.name(),
                        "created_at": faker.iso8601(),
                        "salary": faker.pyfloat(left_digits=4,right_digits=2,positive=True),
                        "active": faker.pybool()}          
            self.lista.append(register)

    def generator_of_registers_list(self,register_number: int):
        self.lista.append(["Id","Nome","Salario","created_at"])
        for _ in tqdm(range(register_number), desc="Generating registers"):
            register = [faker.pyint(),
                        faker.name(),
                        faker.pyfloat(left_digits=4,right_digits=2,positive=True),
                        faker.iso8601()] #por padrao ele grava o dicionario como string           
            self.lista.append(register)

    def output_csv_ovwewrite(self, file_name: str):        
        file_path_old = os.getcwd()
        file_path = file_path_old.replace("src","data/csv/").replace('\\','/')
        file_path_new = file_path+file_name+".csv"
        os.makedirs(os.path.dirname(file_path_new), exist_ok=True)
        with open (file_path_new, "w", newline='') as csv_file:
            writer = csv.writer(csv_file)
            for row in self.lista:
                writer.writerow(row)
        print(f"Archive genetored in {file_path_new}")

    def output_json_overwrite(self, file_name: str):
        file_path_old = os.getcwd()
        file_path = file_path_old.replace("src","data/json/").replace('\\','/')
        file_path_new = file_path+file_name+".json"
        os.makedirs(os.path.dirname(file_path_new), exist_ok=True)
        with open (file_path_new, "w") as json_file:
            json.dump(self.lista,json_file, indent=4, ensure_ascii=False)
        print(f"Archive genetored in {file_path_new}")

    def output_csv_append(self, file_name: str):
        file_path_old = os.getcwd()
        file_path = file_path_old.replace("src","data/csv/").replace('\\','/')
        file_path_new = file_path+file_name+".csv"
        os.makedirs(os.path.dirname(file_path_new), exist_ok=True)
        with open(file_path_new, "a", newline='') as csv_file:
            writer = csv.writer(csv_file)
            for row in self.lista[1:]:
                writer.writerow(row)       
        print(f"Archive genetored in {file_path_new}")

    def output_json_append(self, file_name: str):
        file_path_old = os.getcwd()
        file_path = file_path_old.replace("src","data/json/").replace('\\','/')
        file_path_new = file_path+file_name+".json"
        os.makedirs(os.path.dirname(file_path_new), exist_ok=True)
        with open(file_path_new, "r") as json_file:
            existing_data = json.load(json_file)
            existing_data.extend(self.lista)
            self.lista = existing_data
        with open(file_path_new, "w") as json_file:
            json.dump(self.lista, json_file, indent=4, ensure_ascii=False)
        print(f"Archive genetored in {file_path_new}")