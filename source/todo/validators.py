from django.core.exceptions import ValidationError


def validate_title(value):
    if len(value)<6:
        raise ValidationError("Слишком коротко минимум 6 символов")
    elif "@" in value:
        raise ValidationError("Название не должен сожержать символ '@' ")


