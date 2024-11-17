import duckdb 
import os
import pandas as pd

class Load:
    def __init__(self,df) -> None:
        #self.file_path = file_path
        self.df = df

    def save_parquet_table(self,file_name: str):
        print(self.df)
        output_path = f"data/parquet/{file_name}.parquet"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self.df.to_parquet(output_path)
        print(f"DataFrame salvo como Parquet em: {output_path}")

    # def save_xlsx_table(self,file_name: str):
    #     output_path = f"data/excel/{file_name}.xlsx"
    #     os.makedirs(os.path.dirname(output_path), exist_ok=True)
    #     self.df.to_csv(output_path)
    #     print(f"DataFrame salvo como xlsx em: {output_path}")