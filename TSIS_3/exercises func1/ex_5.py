# Write a function that accepts string from user,
# return a sentence with the words reversed.
# We are ready -> ready are We

def rev_words(text):
    result = ''
    for word in text.split():
        result +=  " " + str(word[::-1])
    return result
    

text = input()

print(rev_words(text)[1:])