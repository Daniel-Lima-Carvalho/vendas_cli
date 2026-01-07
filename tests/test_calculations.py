
from sale_calculations import calculate_total_sales, calculate_totals_by_product
from pytest import raises

def get_csv_sales_data_mock():
    sales_mock = [
        {'produto': 'Camiseta', 'quantidade': '3', 'preco_unitario': '49.9'}, 
        {'produto': 'Calça', 'quantidade': '2', 'preco_unitario': '99.9'}
    ]
    return sales_mock

def test_calculate_total_sales():
    csv_sales_data_mock = get_csv_sales_data_mock()
    expected_value = 349.5
    returned_value = calculate_total_sales(csv_sales_data_mock)

    assert expected_value == returned_value

def test_calculate_totals_by_product_ordering_by_total_sales():
    csv_sales_data_mock = get_csv_sales_data_mock()
    expected_value = {
        'Calça': {
            'total_sales': 199.8,
            'total_quantity': 2
        },
        'Camiseta': {
            'total_sales': 149.7,
            'total_quantity': 3
        }
    }
    
    returned_value = calculate_totals_by_product(csv_sales_data_mock, 'total_sales')

    assert list(expected_value.items()) == list(returned_value.items())

def test_calculate_totals_by_product_ordering_by_total_quantity():
    csv_sales_data_mock = get_csv_sales_data_mock()
    expected_value = {
        'Camiseta': {
            'total_sales': 149.7,
            'total_quantity': 3
        },
        'Calça': {
            'total_sales': 199.8,
            'total_quantity': 2
        }
    }
    
    returned_value = calculate_totals_by_product(csv_sales_data_mock, 'total_quantity')

    assert list(expected_value.items()) == list(returned_value.items())

def test_calculate_totals_by_product_invalid_order_by_option():
    csv_sales_data_mock = get_csv_sales_data_mock()
    expected_value = 'Invalid value for "order_by". The valid options are: [\'total_sales\', \'total_quantity\']'
    
    with raises(Exception) as exc_info:
        calculate_totals_by_product(csv_sales_data_mock, 'other_field')

    assert expected_value == str(exc_info.value)

