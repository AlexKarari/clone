from django.core.exceptions import ValidationError


# Setting validations to fields in a model
# You can set restrictions to profanity in a tweet here as well 

def validate_content(value):  # Content is a field in the models below
    content = value
    if content == "":
        raise ValidationError("Content cannot be blank")
    return value
