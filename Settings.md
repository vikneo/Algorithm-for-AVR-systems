# Запуск и настройка проекта

Клонируем проект из [репозитория](https://github.com/vikneo/Algorithm-for-AVR-systems.git) на локальный компьютер

Назад к файлу [README](README.md)

Описание
* Панель админимтратора -> admin-preview-panel/

## Содержание

* [Виртуальное окружение](#виртуальное-окружение)
* [Установка poetry](#установка-пакета-poetry)
* [Запуск проекта](#запуск-проекта)

## Виртуальное окружение

### Для Windows

* Создать виртуальное окружение
```html
python -m venv name_venv
```
* Активация окружения
```html
venv\Scripts\activate
```

### Для Linux

* Создать виртуальное окружение
```html
python3 -m venv name_venv
```
* Активация окружения
```html
source venv/bin/activate
```

К [содержанию ↑](#содержание)

<hr>

## Установка пакета "poetry"

* Доступная информация по настройке **poetry** [здесь](https://python-poetry.org/docs/cli/)

* что бы установить  ***poetry***  воспользуйтесь командой:
    ```html
    pip install poetry
    ```

### Настройка

* init
    * Эта команда поможет вам создать файл **project.toml** в интерактивном режиме, предложив вам предоставить основную информацию о вашем пакете.
        ```html
        poetry init
        ```
    * Опции
        ```html
        --name: Имя вашего проекта.
        --description: Описание вашего проекта.
        --author: Имя автора проекта.
        --python: совместимые версии Python.
        --dependency: Требуется пакет с ограничением версии. Должен быть в формате foo:1.0.0
        --dev-dependency: Требования к разработке см. --dependency
        ```
* Установка
    * Команда **install** считывает файл **pyproject.toml** из текущего проекта, разрешает зависимости и устанавливает их.
        ```html
        poetry install
        ```
* Добавление
    * Команда **add** добавит новую библиотеку в **pyproject.toml** 
    и произведет установку данного пакета
        ```html
        poetry add Pillow
        ```
    * Можно указывать версию пакета:
        ```html
        poetry add django==4.2
            или
        poetry add django>=4.2
        ```
* Удаление
    * Команда **remove** удалит пакет из файла **pyproject.toml**
        ```html
        poetry remove Pillow
        ```
* Просмотр
    * Команда **show** позволяет просмотреть установленные зависимоти проекта
        ```html
        poetry show
        ```
К [содержанию ↑](#содержание)

<hr>

## Запуск проекта

* Виртуальное окружение активировано
* Установлены все зависимости

### Создаем миграции

* С помощью команды:

```html
python manage.py migrate
```

Создастся база данных (по умолчанию db.sqlite3) и применяются все миграции созданные в папке **migrations**

* Создаем **администратора** для доступа к админ панел проекта:

```html
    python manage.py createsuperuser
    /* пример */
    Вводите login: admin
    Вводите email: admin@qwe.com
    Вводите пароль: 1234
    Вводите повтор: 1234
```

### Запуск приложения:

* Создаем файл **.env**
    
    Заполняем его содержимым

    ПРИМЕР:
    ```html
    DEBUG=True

    SECRET_KEY='django-insecure--flqljj6&bi&c#351e#e@bwd=c#+7-d$!wb#!)lj8h=_z3sw8g'
    
    ALLOWED_HOSTS='*'
    
    IF DEBUG:
        ENGINE='django.db.backends.sqlite3'
        NAME='db.sqlite3'
    ELSE:
        <!-- Здесь настройки для опциональной БД -->
    ```

* Запускаем сервер

    ```html
    python manage.py runserver
    ```
    * Сервер будет запущен по адресу:
        ```html
        http://127.0.0.1:8000/
        ```

* Для перехода в панель адинистратора введите в адресной строке путь:

```html
http://127.0.0.1:8000/admin-preview-panel/
```

* Импорт файлов
    * Проимпортируйте файлы находящиеся в папке **import/json**

        Импорт проектов:
        ![проектов](/related_docs/import_client.PNG)
        Выбираем файл **Client_2024-01-25.json**

        Импорт объектов:
        ![объект](/related_docs/import_object.PNG)
        Выбираем файл **Subject_2024-01-30.json**
        
P.S. В доработке файл для импорта продуктов и **fixtures** проекта

К [содержанию ↑](#содержание)

<hr>