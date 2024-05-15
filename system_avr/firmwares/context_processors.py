from utils.config import get_count_for_id


def product(request):
    """
    Контекстный процессор позволяет воспользоваться переменной "menu"
    для вывода "..." в шаблонах сайта.
    """
    return {
        'menu': 'menu',
    }
