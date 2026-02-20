from src.extract import extract_csv

def test_csv_not_empty():
    df = extract_csv("data/input.csv")
    assert len(df) > 0