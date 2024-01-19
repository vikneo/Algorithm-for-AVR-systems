from firmwares.models import Client
from .slugify import slugify

import re
from csv import DictReader
from io import TextIOWrapper

# class ImportFile():
    
#     def reader_csv(self, file, encoding):
#         csv_file = TextIOWrapper(
#             file,
#             encoding=encoding
#         )
#         reader = DictReader(csv_file)
#         return reader
    
#     def upload_client_csv(self, file, encoding):
#         reader = self.reader_csv(file, encoding)
#         for row in reader:
#             # __client = re.findall(r'\d[0-9]*', row['client'])
#             client = Client(
#                 name=row['client'],
#                 slug=slugify(row['client'])
#             )
#             client.save()


# import_file = ImportFile()

def reader_csv(file, encoding):
    csv_file = TextIOWrapper(
        file,
        encoding=encoding
    )
    reader = DictReader(csv_file)
    return reader

def upload_client_csv(file, encoding):
    reader = reader_csv(file, encoding)
    for row in reader:
        print(row[0])
        client = Client(
            name=row[0],
            slug=slugify(row[0])
        )
        client.save()