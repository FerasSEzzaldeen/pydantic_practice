# from unittest.mock import Mock, patch
# import pytest


# def myfun():
#     return "abc"


# def test_myfun():
#     with patch("tests.test_test.myfun") as mock:
#         mock.return_value = "cba"
#         mock.side_effect = KeyError
#         with pytest.raises(KeyError):
#             print(myfun())
#         assert mock.assert_called


# @patch("tests.test_test.myfun")
# def test_myfun_patched(mock_myfun):
#     mock_myfun.return_value = "cba"
#     mock_myfun.side_effect = KeyError
#     with pytest.raises(KeyError):
#         print(myfun())
#     assert mock_myfun.assert_called
