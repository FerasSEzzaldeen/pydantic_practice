from src.models.employee import OutputModel


def transform(data_in: dict) -> dict:
    return OutputModel(**data_in).dict()
