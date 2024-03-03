import os
import string


def create_files(out_dir):
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    for letter in string.ascii_uppercase:
        full_path = os.path.join(out_dir, letter + '.txt')
        with open(full_path, 'a', encoding='utf8') as newfile:
            pass       

path = r'C:\Python\Projects\KBTU\TSIS_6\output'
create_files(path)