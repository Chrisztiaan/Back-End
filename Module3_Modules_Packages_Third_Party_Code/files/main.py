# Do not modify these lines
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Add your code after this line

# Import
import os
import shutil
from zipfile import ZipFile

base_path = os.getcwd()
files_path = os.path.join(base_path, "files")
cache_path = os.path.join(base_path, "files", "cache")
data_path = os.path.join(base_path, "files", "data.zip")

# 1


def clean_cache():
    os.chdir(files_path)
    if os.path.isdir(cache_path):
        shutil.rmtree(cache_path)
    os.mkdir("cache")


clean_cache()

# 2


def cache_zip(zip, cache):
    with ZipFile(zip, "r") as zipObj:
        zipObj.extractall(cache_path)


cache_zip(data_path, cache_path)


# 3

directory = os.path.abspath(cache_path)


def cached_files():
    cached_files_list = []
    for path in os.listdir(directory):
        full_path = os.path.join(directory, path)
        cached_files_list.append(full_path)
    return cached_files_list


cached_files()

# 4


list_of_files = cached_files()


def find_password(list_of_files):
    for file in list_of_files:
        with open(file) as f:
            for line in f:
                if "password" in line:
                    return line.replace("password: ", "").rstrip("\n")


find_password(list_of_files)
