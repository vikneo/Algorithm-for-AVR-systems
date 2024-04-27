from utils.config import get_count_for_id


def product(request):
    """
    Контекстный процессор позволяет воспользоваться переменной "product_id"
    для вывода "ID Продукта" в шаблонах сайта.
    """
    return {
        'menu': 'menu',
    }
