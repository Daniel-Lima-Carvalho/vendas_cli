import json

from modules.output_utils import print_data, print_text_table, print_total_sales

def test_print_text_table(capsys):
    data = {
        "Camiseta": {"total_sales": 199.6, "total_quantity": 4},
        "Calça": {"total_sales": 199.8, "total_quantity": 2},
    }

    print_text_table(data)
    captured = capsys.readouterr()

    assert "Name" in captured.out
    assert "Total sales" in captured.out
    assert "Quantity" in captured.out
    assert "-" * 40 in captured.out

    assert "Camiseta" in captured.out
    assert "199.60" in captured.out
    assert "4" in captured.out
    assert "Calça" in captured.out
    assert "199.80" in captured.out
    assert "2" in captured.out


def test_print_data_json(capsys):
    data = [{"produto": "Camiseta", "quantidade": "4"}]
    title = "Total sales by product"

    print_data(data, title, format="json")
    captured = capsys.readouterr()

    assert '"produto":"Camiseta"' in str(captured.out).replace('\n', '').replace(' ','')
    assert '"quantidade":"4"' in str(captured.out).replace('\n', '').replace(' ','')


def test_print_data_text(capsys):
    data = {
        "Tênis": {"total_sales": 199.9, "total_quantity": 1}
    }
    title = "Sales table"

    print_data(data, title, format="text")
    captured = capsys.readouterr()

    assert title in captured.out
    assert "Tênis" in captured.out
    assert "199.90" in captured.out
    assert "1" in captured.out

def test_print_total_sales(capsys):
    total_sales = 500.0
    title = "Total sale"

    print_total_sales(total_sales, title)
    captured = capsys.readouterr()

    assert f"{title}: {total_sales}" in captured.out
