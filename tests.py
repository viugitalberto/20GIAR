import pytest
from src.etl import extract, transform, load
import pandas as pd
import tempfile
import os

def test_extract_returns_list():
    data = extract()
    assert isinstance(data, list)
    assert len(data) > 0

def test_transform_filters_long_titles():
    # Datos de prueba
    test_data = [
        {'title': 'short', 'body': 'test', 'userId': 1, 'id': 1},
        {'title': 'x' * 60, 'body': 'test', 'userId': 1, 'id': 2}
    ]
    result = transform(test_data)
    assert len(result) == 1
    assert result.iloc[0]['title_length'] > 50

def test_load_creates_csv():
    df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'test.csv')
        result_path = load(df, path)
        assert os.path.exists(result_path)
        loaded = pd.read_csv(result_path)
        assert len(loaded) == 2