import json
from exporters.json_exporter import JSONExporter


def test_json_exporter_writes_json(tmp_path):
    output_file = tmp_path / "out.json"

    data = {
        "a": 1,
        "b": [1, 2, 3],
    }

    exporter = JSONExporter(output_file)
    exporter.export(data)

    assert output_file.exists()

    with open(output_file, encoding="utf-8") as f:
        loaded = json.load(f)

    assert loaded == data
