import os
from File_Extraction import read_file


def print_hi(name):
    code = "CDP"
    year = "1987"
    path = "datafiles"
    for f in os.listdir(path):
        if f == f"{f[0:2]}-{code}-{year}-data.txt":
            file_path = os.path.join(path, f)
            read_file(file_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
