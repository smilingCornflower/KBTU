def copy_content(file_path1, file_path2):
    with open(file_path1, 'r', encoding='utf8') as file_in:
        content = file_in.read()
    with open(file_path2, 'a', encoding='utf8') as file_out:
        file_out.write(content)


path1 = r"C:\Python\Projects\KBTU\TSIS_6\task.txt"
path2 = r"C:\Python\Projects\KBTU\TSIS_6\copyTask.txt"

copy_content(path1, path2)