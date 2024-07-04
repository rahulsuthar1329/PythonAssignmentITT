import random
import string
import pandas as pd


def extract_date(date_string):
    return date_string.split("T", 1)[0]


def reverse_date(date):
    return '-'.join(date.split('-')[::-1])


def generate_random_id(user_id):
    return f"{user_id}-{''.join(random.choices(string.ascii_letters + string.digits, k=4))}"


def convert_to_dataframe(data):
    return pd.DataFrame(data)


def replace_empty_values(dataframe, replacement='N.A.'):
    dataframe.fillna(replacement, inplace=True)
    dataframe.replace('', replacement, inplace=True)
    return dataframe


def sort_values(dataframe, column, ascending=False):
    dataframe.sort_values(by=column, ascending=ascending, inplace=True)
    return dataframe


def apply_function(dataframe, column, operation):
    return dataframe[column].apply(operation)


def dataframe_to_csv(dataframe, file_name):
    dataframe.to_csv(file_name, index=False)


def drop_column(dataframe, column):
    dataframe.drop(column, axis=1, inplace=True)
    return dataframe
