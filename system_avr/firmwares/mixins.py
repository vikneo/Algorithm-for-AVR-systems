from django.contrib import admin

from .models import Client


class ChangeListMixin:
    """
    Класс ChangeListMixin миксуется для отображения "sidebar" и навигации в "header" в шаблоне настроек
    """

    def get_change_list_admin(self, **kwargs):
        model = Client
        context = kwargs
        context = dict(
            list(context.items()) + list(admin.site.each_context(self.request).items())
        )
        context.update(
            opts=model._meta,
        )

        return context


class MenuMixin:
    """
    Класс подмешивается для отображения меню в header & footer
    """

    @staticmethod
    def __menu__() -> list:
        """
        magic method with a menu list.

        :return: list of dictionaries with an available menu.
        :rtype: list
        """
        menu = [
            {
                "name": "Главная",
                "links": [
                    {"link": "Клиенты", "url": "product:clients"},
                    {"link": "Объекты", "url": "product:subjects"},
                    {"link": "Продукты", "url": "product:product_list"},
                ],
            },
            {
                "name": "Заявка",
                "links": [
                    {"link": "Смотреть", "url": "product:orders"},
                    {"link": "Создать", "url": "product:created"},
                ],
            },
            {
                "name": "Монтэл",
                "links": [
                    {"link": "Bitrix", "url": "https://rinecogroup.bitrix24.ru/stream/"},
                    {"link": "Производство", "url": "product:clients"},
                ],
            },
        ]
        return menu
    
    def get_menu(self, **kwargs) -> dict:
        """
        The method returns the main menu and today's date.

        :param kwargs: accepts the received dictionary.
        :rtype: dict.
        :return: returns the updated dictionary.
        :rtype: dict.
        """

        context = kwargs
        context.update(
            menu=self.__menu__(),
        )
        return context
