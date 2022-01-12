import pytest

from src.models.employee import Department


def transform_test_cases():
    """
    (input, output)    
    """
    return [
        ('age<18', 'age<18'),
        ('age>18', 'age>18'),
        ('10k<salary<20k', '10k<salary<20k'),
        ('20k<salary<30k', '20k<salary<30k')
    ]


@pytest.fixture
def test_age_liss_then_18_case_result():
    return {
        'emp_id': '123',
        'full_name': 'Belal Ali',
        'adult': False,
        'domain': Department.IT,
        'tax_percent': 0.3,
        'after_tax': 24500.0
    }


@pytest.fixture
def test_age_bigger_then_18_case_result():
    return {
        'emp_id': '123',
        'full_name': 'Belal Ali',
        'adult': True,
        'domain': Department.IT,
        'tax_percent': 0.3,
        'after_tax': 24500.0
    }


@pytest.fixture
def test_salary_between_10_and_20_thousand_result():
    return {
        'emp_id': '123',
        'full_name': 'Belal Ali',
        'adult': True,
        'domain': Department.IT,
        'tax_percent': 0.1,
        'after_tax': 13500.0
    }


@pytest.fixture
def test_salary_between_20_and_30_thousand_result():
    return {
        'emp_id': '123',
        'full_name': 'Belal Ali',
        'adult': True,
        'domain': Department.IT,
        'tax_percent': 0.2,
        'after_tax': 20000
    }


@pytest.fixture
def test_age_liss_then_18_case_input():
    return {
        'id': '123',
        'first_name': 'Belal',
        'last_name': 'Ali',
        'age': 15,
        'department': 'IT',
        'salary': 35000
    }


@pytest.fixture
def test_age_bigger_then_18_case_input():
    return {
        'id': '123',
        'first_name': 'Belal',
        'last_name': 'Ali',
        'age': 28,
        'department': 'IT',
        'salary': 35000
    }


@pytest.fixture
def test_salary_between_10_and_20_thousand_input():
    return {
        'id': '123',
        'first_name': 'Belal',
        'last_name': 'Ali',
        'age': 28,
        'department': 'IT',
        'salary': 15000
    }


@pytest.fixture
def test_salary_between_20_and_30_thousand_input():
    return {
        'id': '123',
        'first_name': 'Belal',
        'last_name': 'Ali',
        'age': 28,
        'department': 'IT',
        'salary': 25000
    }


@pytest.fixture
def input(request):
    m = {
        'age<18': {
            'id': '123',
            'first_name': 'Belal',
            'last_name': 'Ali',
            'age': 15,
            'department': 'IT',
            'salary': 35000
        },
        'age>18': {
            'id': '123',
            'first_name': 'Belal',
            'last_name': 'Ali',
            'age': 28,
            'department': 'IT',
            'salary': 35000
        },
        '10k<salary<20k': {
            'id': '123',
            'first_name': 'Belal',
            'last_name': 'Ali',
            'age': 28,
            'department': 'IT',
            'salary': 15000
        },
        '20k<salary<30k': {
            'id': '123',
            'first_name': 'Belal',
            'last_name': 'Ali',
            'age': 28,
            'department': 'IT',
            'salary': 25000
        }
    }
    return m[request.param]


@pytest.fixture
def expected(request):
    m = {
        'age<18': {
            'emp_id': '123',
            'full_name': 'Belal Ali',
            'adult': False,
            'domain': Department.IT,
            'tax_percent': 0.3,
            'after_tax': 24500.0
        },
        'age>18': {
            'emp_id': '123',
            'full_name': 'Belal Ali',
            'adult': True,
            'domain': Department.IT,
            'tax_percent': 0.3,
            'after_tax': 24500.0
        },
        '10k<salary<20k': {
            'emp_id': '123',
            'full_name': 'Belal Ali',
            'adult': True,
            'domain': Department.IT,
            'tax_percent': 0.1,
            'after_tax': 13500.0
        },
        '20k<salary<30k': {
            'emp_id': '123',
            'full_name': 'Belal Ali',
            'adult': True,
            'domain': Department.IT,
            'tax_percent': 0.2,
            'after_tax': 20000
        }
    }
    return m[request.param]
