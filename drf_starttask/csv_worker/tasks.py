from __future__ import absolute_import, unicode_literals

from celery import shared_task
import csv


extensions_cols = ['"col10"', ""]

@shared_task
def csv_task(filename):
    file_info = open(filename, "r")
    reader = csv.reader(file_info)
    total = 0
    for row in reader:
        column = " ".join(row).split(',')[11]
        if(column not in extensions_cols and len(column)>2):
            column = column.replace('"', '')
            float_col = float(column)
            total += float_col
    return total 