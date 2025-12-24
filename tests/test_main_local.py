import json

import main


def test_main_local_json_to_csv(tmp_path, monkeypatch):
    """
    Minimal integration test for main():

    - Uses local JSON input
    - Skips API
    - Runs parser
    - Exports CSV
    - Verifies output file exists

    This test does NOT validate data correctness,
    only that the pipeline runs end-to-end.
    """

    # 1. Create a fake input JSON file
    input_data = {
        "hourly": {
            "time": [0],
            "temperature_2m": [20.0],
        },
        "hourly_units": {
            "time": "unixtime",
            "temperature_2m": "°C",
        },
    }

    input_file = tmp_path / "input.json"
    input_file.write_text(json.dumps(input_data), encoding="utf-8")

    output_file = tmp_path / "output.csv"

    # 2. Patch config values used by main
    monkeypatch.setattr(main, "USE_API", False)
    monkeypatch.setattr(main, "INPUT_PATH", str(input_file))
    monkeypatch.setattr(main, "OUTPUT_PATH", str(output_file))
    monkeypatch.setattr(main, "SKIP_PARSING", False)
    monkeypatch.setattr(main, "USE_CACHE", False)

    # 3. Run main()
    main.main()

    # 4. Assert output was created
    assert output_file.exists()
