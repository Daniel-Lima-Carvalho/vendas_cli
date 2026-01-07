import argparse
from modules.log_config import init_logging
init_logging()

from modules.csv_utils import read_csv_file
from modules.output_utils import print_data, print_total_sales
from modules.sale_calculations import calculate_best_selling_products, calculate_total_sales, calculate_totals_by_product, filter_sales_by_date


def run():
    parser = argparse.ArgumentParser(
        prog="vendas-cli",
        description="CLI to analyze sales"
    )
    parser.add_argument("--csv_file_path", type=str, required=True, help="Path to CSV file")
    parser.add_argument("--format", type=str, help="Path to CSV file")
    parser.add_argument("--initial_date", type=str, help="Inital filter date")
    parser.add_argument("--final_date", type=str, help="Final filter date")

    args = parser.parse_args()
    csv_file_path = args.csv_file_path
    print_format = args.format if args.format else 'text'

    data = read_csv_file(csv_file_path)

    if args.initial_date and args.final_date:
        data = filter_sales_by_date(data, args.initial_date, args.final_date)

    total_sales_by_product = calculate_totals_by_product(data, 'total_sales')
    total_sales = calculate_total_sales(data)
    best_selling_products = calculate_best_selling_products(data)

    print_data(total_sales_by_product, 'TOTAL SALES BY PRODUCT', print_format)
    print_total_sales(total_sales, 'TOTAL SALES')
    print_data(best_selling_products, 'BEST SELLING PRODUCTS', print_format)