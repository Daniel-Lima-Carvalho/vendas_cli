from csv_utils import read_csv_file
from sale_calculations import calculate_best_selling_products, calculate_total_sales, calculate_totals_by_product

data = read_csv_file("docs/vendas_exemplo.csv")
total_sales_by_product = calculate_totals_by_product(data, 'total_sales')
total_sales = calculate_total_sales(data)
best_selling_products = calculate_best_selling_products(data)
print(best_selling_products)
