import json
from typing import List, Dict

def print_text_table(data):
    print(f"{'Name':<10} | {'Total sales':<12} | {'Quantity':<10}")
    print("-" * 40)

    for produto, valores in data.items():
        print(f"{produto:<10} | {valores['total_sales']:<12.2f} | {valores['total_quantity']:<10}")
    
    print()

def print_data(data: List[Dict[str, str]], title: str, format: str):
    print(title)
    if format == 'json':
        print(json.dumps(data, ensure_ascii=False, indent=4), end="\n\n")
    elif format == 'text':
        print_text_table(data)

def print_total_sales(total_sales: float, title: str):
    print(f'{title}: {total_sales}', end="\n\n")
