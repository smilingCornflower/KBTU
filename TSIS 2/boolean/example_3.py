items = ["Hello", 0, 1, '0', '1', None, '', [], [1, 2]]
# [True, False, True, True, True, False, False, False, True]
# Any not empty value will return True
# None, 0, '', [], (), {}, set() - are will give False
print([bool(i) for i in items])