import os


def my_logger( message: object) -> object:
    print(f'Logs : {message}')


def check_file_exist(filepath):
    return True if os.path.exists(str(filepath)) else False
