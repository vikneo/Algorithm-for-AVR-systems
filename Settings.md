# Запуск и настройка проекта

Клонируем проект из [репозитория](https://github.com/vikneo/Algorithm-for-AVR-systems.git) на локальный компьютер

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

```
* Активация окружения
```html
source venv/bin/activate
```
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
<hr>

