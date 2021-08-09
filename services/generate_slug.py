from time import time
from transliterate import slugify

def gen_slug(text: str) -> str:
    """
    Генерирование url путем транслита.
    При добавлении флага к url добавляется время.
    """

    slug = slugify(text, language_code='ru') + '-' + str(int(time()))
    return slug
