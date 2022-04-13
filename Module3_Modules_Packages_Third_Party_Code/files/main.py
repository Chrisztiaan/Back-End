# Do not modify these lines
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Add your code after this line

# Import
import os
import shutil
from zipfile import ZipFile

# 1


path = r"C:\\Users\\C.verlaan\Winc\Back-End\\Module3_Modules_Packages_Third_Party_Code\\files\\cache"


def clean_cache():
    os.chdir(
        "C:\\Users\\C.verlaan\Winc\Back-End\\Module3_Modules_Packages_Third_Party_Code\\files"
    )
    if os.path.isdir(path):
        shutil.rmtree(path)
    os.mkdir("cache")


clean_cache()

# 2


def cache_zip(zip, path):
    with ZipFile(zip, "r") as zipObj:
        zipObj.extractall(path)


cache_zip(
    r"C:\\Users\\C.verlaan\Winc\Back-End\\Module3_Modules_Packages_Third_Party_Code\\files\\data.zip",
    r"C:\\Users\\C.verlaan\Winc\Back-End\\Module3_Modules_Packages_Third_Party_Code\\files\\cache",
)


# 3

directory = os.path.abspath(
    r"C:\\Users\\C.verlaan\Winc\Back-End\\Module3_Modules_Packages_Third_Party_Code\\files\\cache"
)


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
    os.chdir(directory)
    for file in list_of_files:
        with open(file) as f:
            for line in f:
                if "password" in line:
                    split_password = line.split(" ", 1)
                    print(split_password[1])


find_password(list_of_files)
