from parsers.parser import WeatherHourlyParser


def test_parser_returns_list_of_dicts(minimal_weather_api_response):
    parser = WeatherHourlyParser()
    result = parser.parse(minimal_weather_api_response)

    assert isinstance(result, list)
    assert isinstance(result[0], dict)


# Add other parser tests as needed
def test_parser_creates_one_row_per_timestamp(minimal_weather_api_response):
    parser = WeatherHourlyParser()
    result = parser.parse(minimal_weather_api_response)

    assert len(result) == 2


def test_parser_adds_unit_suffixes(minimal_weather_api_response):
    parser = WeatherHourlyParser()
    row = parser.parse(minimal_weather_api_response)[0]

    assert "temperature_2m_c" in row
    assert "windspeed_10m_kmh" in row


def test_parser_converts_time_to_iso(minimal_weather_api_response):
    parser = WeatherHourlyParser()
    row = parser.parse(minimal_weather_api_response)[0]

    assert row["time_iso"].endswith("+00:00")
