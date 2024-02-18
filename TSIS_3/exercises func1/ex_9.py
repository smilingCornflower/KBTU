def unique_els(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
        