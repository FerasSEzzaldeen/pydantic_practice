from src.transformers.employee_transformer import transform
import pytest
from tests.transformers.conftest import transform_test_cases


def test_transform(test_age_liss_then_18_case_result, test_age_liss_then_18_case_input):
    actual = transform(test_age_liss_then_18_case_input)
    assert actual == test_age_liss_then_18_case_result


def test_age_bigger_then_18_case(test_age_bigger_then_18_case_result,
                                 test_age_bigger_then_18_case_input):
    actual = transform(test_age_bigger_then_18_case_input)
    assert actual == test_age_bigger_then_18_case_result


def test_salary_between_10_and_20_thousand(test_salary_between_10_and_20_thousand_result,
                                           test_salary_between_10_and_20_thousand_input):
    actual = transform(test_salary_between_10_and_20_thousand_input)
    assert actual == test_salary_between_10_and_20_thousand_result


def test_salary_between_20_and_30_thousand(test_salary_between_20_and_30_thousand_result,
                                           test_salary_between_20_and_30_thousand_input):
    actual = transform(test_salary_between_20_and_30_thousand_input)
    assert actual == test_salary_between_20_and_30_thousand_result


@pytest.mark.parametrize("input, expected",
                         transform_test_cases(),
                         indirect=["input", 'expected'])
def test_fun(input, expected):
    assert transform(input) == expected
