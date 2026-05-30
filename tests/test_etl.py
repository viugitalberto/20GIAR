import pytest
from src.etl import extract, transform

def test_extract_returns_data():
    data = extract()
    assert len(data) > 0

def test_transform_filters():
    posts = [
        {'title': 'corto', 'userId': 1, 'id': 1, 'body': ''},
        {'title': 'x' * 60, 'userId': 1, 'id': 2, 'body': ''}
    ]
    result = transform(posts)
    assert len(result) == 1
