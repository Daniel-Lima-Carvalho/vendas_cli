import csv
from typing import List, Dict
import logging

def read_csv_file(file_path: str) -> List[Dict[str, str]]:
    logging.info(f"Reading csv file at path: {file_path}...")
    with open(file_path, encoding='utf-8') as sale_file:
        reader = csv.DictReader(sale_file)
        data = [line for line in reader]
    logging.info(f"File read!")
    return data