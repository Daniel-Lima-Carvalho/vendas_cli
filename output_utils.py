import json
from typing import List, Dict

def print_text_table(data):
    print(f"{'Produto':<10} | {'Total Vendas':<12} | {'Quantidade':<10}")
    print("-" * 40)

    for produto, valores in data.items():
        print(f"{produto:<10} | {valores['total_sales']:<12.2f} | {valores['total_quantity']:<10}")

def print_data(data: List[Dict[str, str]], title: str, format: str):
    print(title)
    if format == 'json':
        print(json.dumps(data, ensure_ascii=False))
    elif format == 'text':
        print_text_table(data)