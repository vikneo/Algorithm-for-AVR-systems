from utils.config import get_count_for_id

from .models import Product


def product(request):
    """
    Контекстный процессор позволяет воспользоваться переменной "product"
    для вывода "..." в шаблонах сайта.
    """
    print(request)
    products = Product.objects.all()
    return {
        'products': products,
    }
