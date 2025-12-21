from loaders.csv_loader import CSVLoader


def test_csv_loader_returns_list_of_dicts(tmp_path):
    file = tmp_path / "data.csv"
    file.write_text("a,b\n1,2\n")

    loader = CSVLoader(file)
    data = loader.load()

    assert isinstance(data, list)
    assert isinstance(data[0], dict)
