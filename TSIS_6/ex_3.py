import os

def test_path_exists(path):
    if os.path.exists(path):
        print(f"Directory: {os.path.dirname(path)}")
        print(f"Filename: {os.path.basename(path)}")
    else:
        print('File does not exist')
        
        
path = r'C:\Python\Projects\KBTU\TSIS_6\test\Fern.jpeg'
test_path_exists(path)
