# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
test_strings = ["a", "ab", "abb", "abbb", "ac", "b", "bb"]
for line in test_strings:
    if 'a' in line:
        print(f"{line} соответствует")
    else:
        print(f"{line} не соответсвует")
        