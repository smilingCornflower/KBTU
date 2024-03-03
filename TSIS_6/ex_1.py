import os


def list_dir_files(root, show_all=False):
    if os.path.exists(root):
        res_dirs = []
        res_files = []
        if show_all:
            for dirname, subdirs, filenames in os.walk(root):
                res_dirs.append(dirname)
                for i in filenames:
                    full_path = os.path.join(root, i)
                    res_files.append(full_path)
        else:
            for path in os.listdir(root):
                full_path = os.path.join(root, path)
                if os.path.isdir(full_path):
                    res_dirs.append(full_path)
                elif os.path.isfile(full_path):
                    res_files.append(full_path)
        return res_dirs, res_files
                
    else:
        return None

path = r'C:\Python\Projects\KBTU\TSIS_6\test'

dirs, files = list_dir_files(path, show_all=False)

print('=' * 50)
for i in dirs:
    print(i)
print()
for i in files:
    print(i)