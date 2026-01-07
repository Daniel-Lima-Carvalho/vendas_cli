from modules.log_config import init_logging
init_logging()
import logging

from modules.csv_utils import read_csv_file
from modules.output_utils import print_data
from modules.sale_calculations import calculate_best_selling_products, calculate_total_sales, calculate_totals_by_product


data = read_csv_file("docs/vendas_exemplo.csv")
logging.info('Calculating data...')
total_sales_by_product = calculate_totals_by_product(data, 'total_sales')
total_sales = calculate_total_sales(data)
best_selling_products = calculate_best_selling_products(data)
logging.info('Data calculated!')

print_data(best_selling_products, 'Best Selling products', 'text')
