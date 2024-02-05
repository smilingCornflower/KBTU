def reverse_str_ver1(line: str) -> str:
    return line[::-1]


def reverse_str_ver2(line: str) -> str:
    result = ''
    # start length - 1
    # end = -1
    # step = -1
    
    # for i in range(10, -1, -1)
    # from 10 to 0
    
    for i in range(len(line) - 1, -1, -1):
        result += line[i]
        
    return result

def reverse_str_ver3(line: str) -> str:
    result = ''
    line_len = len(line) - 1
    for i in range(len(line)):
        result += line[line_len - i]
        
    return result


message = "All Hail Lelouch"