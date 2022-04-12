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
        "C:\\Users\\C.verlaan\Winc\Back-End\\Module3_Modules_Packages_Third_Party_Code\\files")
    if os.path.isdir(path):
        shutil.rmtree(path)
        print("Cache Empty")
    os.mkdir("cache")
    print("Cache Made")


clean_cache()

# 2


def cache_zip(zip, path):
    with ZipFile(zip, "r") as zipObj:
        zipObj.extractall(path)
        print("File is unzipped in cache folder")


cache_zip(r"C:\\Users\\C.verlaan\Winc\Back-End\\Module3_Modules_Packages_Third_Party_Code\\files\\data.zip",
          r"C:\\Users\\C.verlaan\Winc\Back-End\\Module3_Modules_Packages_Third_Party_Code\\files\\cache")


# 3

# Absolute pad maken:
directory = os.path.abspath(
    r"C:\\Users\\C.verlaan\Winc\Back-End\\Module3_Modules_Packages_Third_Party_Code\\files\\cache")

# Function die een lijst maakt van de files in "cache"


def cached_files():
    file_list = os.listdir(directory)
    print("List of files made")
    return file_list


cached_files()

# 4


list_of_files = cached_files()


def find_password(list_of_files):
    os.chdir(directory)
    for file in list_of_files:
        with open(file) as f:
            for line in f:
                if "password" in line:
                    print(line)


find_password(list_of_files)
