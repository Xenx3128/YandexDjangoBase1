from django.forms import ValidationError
from functools import wraps


def validate_words(*words):
    @wraps(validate_words)
    def validate(value):
        temp_value = set(value.lower().split())
        temp_words = set(map(lambda x: x.lower(), words))
        if len(temp_words - temp_value) == len(temp_words):
            raise ValidationError(
                f'Обязательно используйте слова: {", ".join(words)}')
    return validate
