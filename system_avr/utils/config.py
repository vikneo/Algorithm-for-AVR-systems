from firmwares.models import Product


# константа для среза фраз
LENGTH = 25

# константа для определения кол-ва символов в ID продукта
COUNT_SYMBOL = 4


def get_count_for_id(product_id) -> str:
    """
    Возращает строку с количеством символов для ID.
    Максимальная длина хранится в константе COUNT_SYMBOL.

    Например:
        ID = 23 то значение вернется  0023
        ID = 123 то значение вернется  0123
    """
    return '0' * (COUNT_SYMBOL - len(product_id)) + product_id if len(product_id) < COUNT_SYMBOL else product_id
