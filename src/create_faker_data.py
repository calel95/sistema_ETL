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