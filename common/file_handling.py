import shutil

from common.common_global import *

# READING FILES
# "r " - read | "w" - overwrite | "a" - append/add | "r+" - read write



def read_in_files(file_name_path):
    my_logger(f'**FILE NAME : {file_name_path}**')
    try:
        if check_file_exist(file_name_path):
            file_name = open(file_name_path, "r")
            list_get_row_file = []
            if file_name.readable():
                for rows in file_name.readlines():
                    list_get_row_file.append(rows.strip())

            file_name.close()
            my_logger(f'READ FILE : {list_get_row_file}')
            return list_get_row_file
        else:
            my_logger(f'{file_name_path} is not exist or can''t find')

    except ValueError:
        my_logger(ValueError)


def write_in_files(file_name_path, row_value, is_create=False ):
    def create_files_checking(ops_value1, ops_value2):
        return ops_value1 if not is_create else ops_value2

    try:
        open_file = open(file_name_path, create_files_checking("a", "w"))
        if open_file.writable():
            if is_create:
                open_file.writelines(f'\n{row_value}'.strip())
            else:
                if check_file_exist(file_name_path):
                    list_get_row_file = read_in_files(file_name_path)
                    if row_value not in list_get_row_file:
                        open_file.writelines(f'\n{row_value}')
                    else:
                        my_logger(f'Row value : {row_value} is already exist')
                else:
                    my_logger(f'{file_name_path} is not exist')
        open_file.close()
        read_in_files(file_name_path)

    except ValueError:
        my_logger(ValueError)


def create_files(file_name, extension, body):
    file_name_path = f'Files\\{file_name}.{extension}'

    print(f'{check_file_exist(file_name_path) } | {not(check_file_exist(file_name_path) )}')
    if not (check_file_exist(file_name_path)):  # check if the files is exist
        write_in_files(file_name_path, body, True)
    else:
        my_logger(f'{file_name_path} is already exist')


def update_value_in_files(file_name_path, row_index, row_value, is_delete=False):
    try:
        if check_file_exist(file_name_path):
            open_file_name = open(file_name_path, 'r').readlines()
            if row_index <= len(open_file_name):
                open_file_name[row_index] = "" if is_delete else row_value
                write_file_name = open(file_name_path, 'w')
                write_file_name.writelines(open_file_name)
                write_file_name.close()
                read_in_files(file_name_path)
            else:
                my_logger(f'{file_name_path} : the Line Index : {row_index} is out of range | Actual Line Index of Files : {len(open_file_name)}')
        else:
            my_logger(f'{file_name_path} is not exist')
    except ValueError:
        my_logger(ValueError)


def delete_value_in_files(file_name_path, row_index):
    update_value_in_files(file_name_path, row_index, "", True)


def copy_file(source_file_name_path, destination_file_name_path, file_name_of_copy):

    try:
        if check_file_exist(source_file_name_path):
            des_copy_file = f'{destination_file_name_path}\\{file_name_of_copy}.{source_file_name_path.split(".")[1]}'
            if not check_file_exist(des_copy_file):
                shutil.copy(source_file_name_path, des_copy_file)
            else:
                my_logger(f'{source_file_name_path} is already exist')
        else:
            my_logger(f'{source_file_name_path} is not exist')
    except ValueError:
        my_logger(ValueError)


def move_file(source_file_name_path, destination_file_name_path):

    try:
        source_file_name_path = source_file_name_path.replace("/", "\\")
        destination_file_name_path = destination_file_name_path.replace("/", "\\") + "\\" + source_file_name_path.split("\\")[-1]
        my_logger(f'Source File Path : {source_file_name_path} | Destination Path : {destination_file_name_path}')

        if check_file_exist(source_file_name_path):
            if not check_file_exist(destination_file_name_path):
                os.replace(source_file_name_path, destination_file_name_path)
                my_logger(f'{source_file_name_path} is was moved')
            else:
                my_logger(f'{source_file_name_path} is already exist')
        else:
            my_logger(f'{source_file_name_path} is not exist')
    except ValueError:
        my_logger(ValueError)


def delete_file(source_file_name_path):
    try:
        if check_file_exist(source_file_name_path):
            os.remove(source_file_name_path)
            my_logger(f'{source_file_name_path} is was deleted')
        else:
            my_logger(f'{source_file_name_path} is not exist')
    except FileNotFoundError:
        my_logger(FileNotFoundError)

