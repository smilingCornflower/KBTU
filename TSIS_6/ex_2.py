import os


def check_access(root):
    print(f"Existance: {os.path.exists(root)}")
    print(f"Readability: {os.access(root, os.R_OK)}")
    print(f"Writability: {os.access(root, os.W_OK)}")
    print(f"Executability: {os.access(root, os.X_OK)}")

check_access(r'C:\Python\Projects\KBTU\TSIS_6\test\Fern.jpeg')
