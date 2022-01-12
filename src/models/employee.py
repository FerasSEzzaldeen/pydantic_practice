from enum import Enum

from pydantic import BaseModel, Field, root_validator


class Department(str, Enum):
    IT = 'it-services.com'
    SALES = 'sales-dep.com'
    PRESALES = 'pre-sales.com'
    FULFILLMENT = 'fulfillment.com'
    SUPPORT = 'customer-support.com'


class OutputModel(BaseModel):
    emp_id: str = Field(..., alias="id")
    full_name: str
    adult: bool
    domain: Department
    tax_percent: float
    after_tax: float

    @root_validator(pre=True)
    def transform_data(cls, values):
        cls.full_name_constructor(values)
        cls.map_domain(values)
        cls.adult_recognizer(values)
        cls.tax_calcolater(values)
        cls.salary_calcolater(values)
        return values

    def full_name_constructor(values):
        values["full_name"] = values['first_name']+' '+values['last_name']

    def map_domain(values):
        values['domain'] = Department[values['department']]

    def adult_recognizer(values):
        values['adult'] = values['age'] > 18

    def tax_calcolater(values):
        if int(values['salary']) < 10000:
            values['tax_percent'] = 0
        elif int(values['salary']) >= 10000 and int(values['salary']) < 20000:
            values['tax_percent'] = .1
        elif int(values['salary']) >= 20000 and int(values['salary']) < 30000:
            values['tax_percent'] = .2
        elif int(values['salary']) >= 30000 and int(values['salary']) < 40000:
            values['tax_percent'] = .3

    def salary_calcolater(values):
        values['after_tax'] = float(
            values['salary'])-float(values['salary'])*values['tax_percent']
