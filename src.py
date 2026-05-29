import requests
import pandas as pd
from datetime import datetime

def extract():
    """Extrae datos de una API pública (posts de ejemplo)"""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    response.raise_for_status()
    return response.json()

def transform(data):
    """Transforma: convierte a DataFrame y filtra"""
    df = pd.DataFrame(data)
    # Agrega columna de longitud del título
    df['title_length'] = df['title'].str.len()
    # Filtra posts con título largo (>50 caracteres)
    df_filtered = df[df['title_length'] > 50]
    return df_filtered

def load(df, output_path='output/data.csv'):
    """Carga los datos transformados a CSV"""
    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Datos guardados en {output_path}")
    return output_path

def run_pipeline():
    print(f"Iniciando pipeline ETL - {datetime.now()}")
    raw_data = extract()
    print(f"Extraídos {len(raw_data)} registros")
    transformed_data = transform(raw_data)
    print(f"Transformados: {len(transformed_data)} registros después de filtrar")
    output_file = load(transformed_data)
    print(f"Pipeline completado. Archivo: {output_file}")
    return output_file

if __name__ == "__main__":
    run_pipeline()