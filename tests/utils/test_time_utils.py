from parsers.parser import unix_to_iso


def test_unix_to_iso_epoch():
    assert unix_to_iso(0) == "1970-01-01T00:00:00+00:00"
