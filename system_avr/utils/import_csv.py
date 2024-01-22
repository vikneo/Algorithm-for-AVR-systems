from firmwares.models import Client
from .slugify import slugify

from csv import DictReader
from io import TextIOWrapper

class ImportFile():
    """
    Загрузка файла "csv" в базу данных.
    """
    def reader_csv(self, file, encoding):
        """
        Чтение csv файла и преобразование в список словарей.
        """
        csv_file = TextIOWrapper(
            file,
            encoding=encoding
        )
        reader = DictReader(csv_file)
        return reader
    
    def upload_client_csv(self, file, encoding):
        """
        Итерация по словарю и занесение занных клююча 'clent' в БД.
        """
        reader = self.reader_csv(file, encoding)
        for row in reader:
            try:
                client = Client(
                    name=row['client'],
                    slug=slugify(row['client'])
                )
                client.save()
            except Exception as err:
                print(f'Поле "slug" должно быть уникальным. Описание ошибки: {err}')


import_file = ImportFile()
