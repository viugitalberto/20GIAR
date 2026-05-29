import requests
import pandas as pd
from datetime import datetime

def extract():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    return response.json()

def transform(data):
    df = pd.DataFrame(data)
    df['title_length'] = df['title'].str.len()
    df_filtered = df[df['title_length'] > 50]
    return df_filtered

def load(df):
    import os
    os.makedirs('output', exist_ok=True)
    df.to_csv('output/data.csv', index=False)
    print("Datos guardados en output/data.csv")

def run_pipeline():
    print("Iniciando pipeline...")
    raw = extract()
    transformed = transform(raw)
    load(transformed)
    print("Pipeline finalizado!")

if __name__ == "__main__":
    run_pipeline()
