import duckdb 
import os
import pandas as pd

class Load:
    # def __init__(self,df) -> None:
    #     #self.file_path = file_path
    #     self.df = df

    @staticmethod
    def save_parquet_table(df,file_name: str):
        output_path = f"data/parquet/{file_name}.parquet"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_parquet(output_path)
        print(f"DataFrame salvo como Parquet em: {output_path}")

    @staticmethod
    def save_xlsx_table(df,file_name: str):
        output_path = f"data/excel/{file_name}.xlsx"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        pd.ExcelWriter(df)
        (output_path)
        print(f"DataFrame salvo como xlsx em: {output_path}")

    @staticmethod
    def save_teste(df, path):
        duckdb.register('VW', df)
        duckdb.execute(f"COPY (SELECT * FROM VW) TO '{path}' (FORMAT 'parquet')")                       