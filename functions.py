import datetime
import re
import os


def write_csv(dataframe, file_name, output_directory):
    try:
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        dataframe.to_csv('extracted_csv/hebdo_32_0_' + file_name, header=True, index=False, sep=';')
        print('File created ! ')
    except FileNotFoundError:
        print('Error writing file')


def add_week(weeks):
    dates = weeks.split('-')
    next_start = datetime.datetime(int(dates[0]), int(dates[1]), int(dates[2]))
    next_ending = datetime.datetime(int(dates[3]), int(dates[4]), int(dates[5]))
    next_start = next_start + datetime.timedelta(days=7)
    next_ending = next_ending + datetime.timedelta(days=7)
    new_date = next_start.strftime("%Y") + '-' + next_start.strftime(
        "%m") + '-' + next_start.strftime("%d") + '-' + next_ending.strftime(
        "%Y") + '-' + next_ending.strftime("%m") + '-' + next_ending.strftime("%d")
    return new_date


def verify_format_regex(regex, dates):
    if re.search(regex, dates):
        return True
    else:
        return False


def replace_dot_by_coma(string):
    return string.replace('.', ',')
