from __future__ import absolute_import, unicode_literals
import boto3
import botocore
from celery import shared_task
import pandas as pd

from drf_starttask.settings import LOCAL_FOLDER, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME



@shared_task
def csv_task(filepath):
    '''Проверяем есть ли файл и если есть - передаём таску в очередь. Если нет - отдаём ошибку'''
    filename = filepath.split('/')[-1]
    '''Проверка взята из https://www.stackvidhya.com/check-if-a-key-exists-in-an-s3-bucket-using-boto3-python/'''
    if AWS_ACCESS_KEY_ID is not None:
        session = boto3.Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        s3 = session.resource('s3')
        try:
            s3.Object(AWS_STORAGE_BUCKET_NAME, filename).load()
            '''Если предыдущая строка не вывела в ошибку - значит файл есть в s3 и будем его скачивать'''
            s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name='eu-north-1')
            bucket_name = AWS_STORAGE_BUCKET_NAME
            s3.download_file(bucket_name, filename, filepath)
        except botocore.exceptions.ClientError as e:
            pass
    return summer(filepath,filename)


def summer(filepath,filename):
    try:
        resp = {}
        # считываем данные из csv
        df = pd.read_csv(filepath, quoting=3)
        df.columns = df.columns.str.replace('\"', '')
        for n in range(len(df.columns.tolist()) - 1):
            if (n % 10 == 0):
                total = pd.to_numeric(df[f'col{n}'].str.replace('"','')).sum()
                resp[f"col{n}"] = total
        return(resp)
    except FileNotFoundError:
        return({"fail": f"'{filename}' not found"})