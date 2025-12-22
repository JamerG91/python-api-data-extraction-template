from openpyxl import Workbook
from loaders.excel_loader import ExcelLoader


def test_excel_loader_loads_rows_as_dicts(tmp_path):
    file_path = tmp_path / "test.xlsx"

    # Create a minimal Excel file
    wb = Workbook()
    ws = wb.active
    ws.append(["col1", "col2"])
    ws.append([1, 2])
    ws.append([3, 4])
    wb.save(file_path)

    loader = ExcelLoader(file_path)
    result = loader.load()

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0] == {"col1": 1, "col2": 2}
    assert result[1] == {"col1": 3, "col2": 4}
