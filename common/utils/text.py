import random
import string

from django.utils.text import slugify


def unique_slug(s, model, num_chars=24):
    """
    Return slug of num_chars length unique to model

    `s` is the string to trun into a slug
    `model` is the model we need to use to check for uniqueness
    """
    slug = slugify(s)
    slug = slug[:num_chars].strip("-")
    while True:
        dup = model.objects.filter(slug=slug)
        if not dup:
            return slug

        slug = slug[:12] + "-" + random_string(12)


def random_string(num_chars=12):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(num_chars))
