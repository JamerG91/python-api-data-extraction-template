import json
from loaders.json_loader import JSONLoader


def test_json_loader_loads_dict(tmp_path):
    data = {
        "a": 1,
        "b": 2,
    }

    file_path = tmp_path / "test.json"
    file_path.write_text(json.dumps(data), encoding="utf-8")

    loader = JSONLoader(file_path)
    result = loader.load()

    assert isinstance(result, dict)
    assert result == data
