from faker import Faker
import json
from tqdm import tqdm 
import csv
import os
import re
from multiprocessing import Pool

faker = Faker()
#Faker.seed(0)

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


    def output_csv_overwrite(self, file_name: str):
        file_path_old = os.getcwd()
        file_path = file_path_old.replace("src","data/csv/").replace('\\','/')
        file_path_new = file_path+file_name+".csv"
        with open (file_path_new, "w", newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["ID", "Name", "created_at", "Salary"], delimiter=";")
            writer.writeheader()
            for row in self.lista:
                writer.writerow(row)

        print(f"Archive genetored in {file_path_new}")

    def output_json_overwrite(self, file_name: str):
        file_path_old = os.getcwd()
        file_path = file_path_old.replace("src","data/json/").replace('\\','/')
        file_path_new = file_path+file_name+".json"
        with open (file_path_new, "w") as json_file:
            json.dump(self.lista,json_file, indent=4, ensure_ascii=False)

        print(f"Archive genetored in {file_path_new}")

    def output_csv_append(self, file_name: str):
        file_path_old = os.getcwd()
        file_path = file_path_old.replace("src","data/csv/").replace('\\','/')
        file_path_new = file_path+file_name+".csv"
        with open (file_path_new, "a", newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["ID", "Name", "created_at", "Salary"], delimiter=";")
            writer.writerows(self.lista)
            # for row in self.lista:
            #     writer.writerow(row)
        print(f"Archive genetored in {file_path_new}")

    def output_json_append(self, file_name: str):
        file_path_old = os.getcwd()
        file_path = file_path_old.replace("src","data/json/").replace('\\','/')
        file_path_new = file_path+file_name+".json"
        with open(file_path_new, "r") as json_file:
            existing_data = json.load(json_file)
            existing_data.extend(self.lista)
            self.lista = existing_data

        with open(file_path_new, "w") as json_file:
            json.dump(self.lista, json_file, indent=4, ensure_ascii=False)

        print(f"Archive genetored in {file_path_new}")