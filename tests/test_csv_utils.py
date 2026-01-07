import csv

from modules.csv_utils import read_csv_file

def test_read_csv_file(tmp_path, caplog):
    file_path = tmp_path / "vendas.csv"
    with open(file_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["produto", "quantidade", "preco_unitario"])
        writer.writeheader()
        writer.writerow({"produto": "Camiseta", "quantidade": "4", "preco_unitario": "199.6"})
        writer.writerow({"produto": "Calça", "quantidade": "2", "preco_unitario": "199.8"})

    caplog.set_level("INFO")
    result = read_csv_file(str(file_path))

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["produto"] == "Camiseta"
    assert result[1]["produto"] == "Calça"

    assert "Reading csv file" in caplog.text
    assert "File read!" in caplog.text
