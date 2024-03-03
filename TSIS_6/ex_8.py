import os
import time


def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            os.remove(file_path)
        else:
            print('Permission denied')
            return False
    else:
        print('File does not exist')
        return False

file_path = 'Testing_newfile.txt'
with open(file_path, 'w', encoding='utf8') as newfile:
    time.sleep(5)

delete_file(file_path)