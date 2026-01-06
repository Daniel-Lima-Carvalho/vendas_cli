import csv
from typing import List, Dict

def read_csv_file(file_path: str) -> List[Dict[str, str]]:
    with open(file_path) as sale_file:
        reader = csv.DictReader(sale_file)
        data = [line for line in reader]
        
    return data