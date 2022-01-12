from unittest.mock import patch
from src.main import migrate


@patch('src.main.select_all')
def test_migrate(mock_select_all):
    mock_select_all.return_value = [{"id": "123", "first_name": "Belal",
                                     "last_name": "Ali",
                                     "age": 15,
                                     "department": "IT",
                                     "salary": 35000}]
    
    result = migrate()
    
    mock_select_all.assert_called()
    assert result == [{'emp_id': '123',
                          'full_name': 'Belal Ali',
                          'adult': False,
                          'domain': 'it-services.com',
                          'tax_percent': 0.3, 'after_tax': 24500.0}]
