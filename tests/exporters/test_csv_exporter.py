import pytest
from exporters.csv_exporter import CSVExporter


def test_csv_exporter_single_dataset(tmp_path):
    output_file = tmp_path / "data.csv"

    data = [
        {"a": 1, "b": 2},
        {"a": 3, "b": 4},
    ]

    exporter = CSVExporter(output_file)
    exporter.export(data)

    assert output_file.exists()



def test_csv_exporter_multiple_datasets(tmp_path):
    output_file = tmp_path / "out.csv"

    data = {
        "Tokyo": [{"a": 1}],
        "New York": [{"a": 2}],
    }

    exporter = CSVExporter(output_file)
    exporter.export(data)

    assert (tmp_path / "Tokyo.csv").exists()
    assert (tmp_path / "New_York.csv").exists()


def test_csv_exporter_rejects_invalid_input(tmp_path):
    exporter = CSVExporter(tmp_path / "out.csv")

    with pytest.raises(TypeError):
        exporter.export("invalid")
