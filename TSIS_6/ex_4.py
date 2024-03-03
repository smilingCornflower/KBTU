import os

def count_lines(path: str):
    if path.endswith('.txt'):
        counter = 0
        with open(path, encoding='utf8') as txt_file:
            for line in txt_file:
                counter += 1
        return counter
    else:
        return -1

file_path = r'C:\Python\Projects\KBTU\TSIS_6\task.txt'
print(count_lines(file_path))  