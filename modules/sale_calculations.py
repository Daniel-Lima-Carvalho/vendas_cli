from typing import List, Dict
from datetime import datetime

def order_sales_dict(sales_by_product: dict, order_by: str) -> dict:
    order_by_options = ['total_sales', 'total_quantity']

    if order_by not in order_by_options:
        raise Exception(f'Invalid value for "order_by". The valid options are: {order_by_options}')

    sales_by_product = dict(sorted(sales_by_product.items(), key=lambda item: item[1][order_by], reverse=True))
    return sales_by_product

def filter_sales_by_date(sales: List[Dict[str, str]], initial_date: str, final_date: str) -> List[Dict[str, str]]:
    date_format = "%Y-%m-%d"
    initial_date = datetime.strptime(initial_date, date_format)
    final_date = datetime.strptime(final_date, date_format)
    filtered_sales = []

    for sale in sales:
        sale_date = datetime.strptime(sale['data'], date_format)
        if sale_date >= initial_date and sale_date <= final_date:
            filtered_sales.append(sale)
    
    return filtered_sales

def calculate_totals_by_product(data: List[Dict[str, str]], order_by) -> dict:
    sales_by_product = {}
    
    for line in data:
        if line['produto'] not in sales_by_product:
            sales_by_product[line['produto']] = {
                'total_sales': float(line['preco_unitario']) * int(line['quantidade']),
                'total_quantity': int(line['quantidade'])
            }
        else:
            sales_by_product[line['produto']]['total_sales'] += float(line['preco_unitario']) * int(line['quantidade']) 
            sales_by_product[line['produto']]['total_quantity'] += int(line['quantidade'])

    sales_by_product = order_sales_dict(sales_by_product, order_by)
    return sales_by_product

def calculate_total_sales(data: List[Dict[str, str]]) -> float:
    total_sale = sum([float(line['preco_unitario']) * int(line['quantidade']) for line in data])
    return total_sale

def calculate_best_selling_products(data: List[Dict[str, str]]) -> dict:
    best_selling_products = calculate_totals_by_product(data, 'total_quantity')
    return best_selling_products