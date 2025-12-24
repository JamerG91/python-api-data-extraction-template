def test_main_api_mode_with_mocked_fetch(tmp_path, monkeypatch):
    """
    Integration-style test for main() in API mode,
    mocking fetch_data so no real HTTP requests are made.
    """

    import main  # import inside test so monkeypatch works cleanly

    # --- 1. Fake fetch_data implementation ---
    def fake_fetch_data(url, params=None, headers=None):
        return {
            "ok": True,
            "data": {
                "hourly": {
                    "time": [0],
                    "temperature_2m": [20.0],
                },
                "hourly_units": {
                    "time": "unixtime",
                    "temperature_2m": "°C",
                },
            },
        }

    # --- 2. Patch fetch_data in main ---
    monkeypatch.setattr(main, "fetch_data", fake_fetch_data)

    # --- 3. Patch config values ---
    output_file = tmp_path / "out.json"

    monkeypatch.setattr(main, "USE_API", True)
    monkeypatch.setattr(main, "USE_CACHE", False)
    monkeypatch.setattr(main, "OUTPUT_PATH", str(output_file))
    monkeypatch.setattr(
        main,
        "CITY_COORDINATES",
        {"TestCity": (0.0, 0.0)},
    )

    # --- 4. Run main ---
    main.main()

    # --- 5. Assert output exists ---
    assert output_file.exists()
