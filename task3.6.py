def revers(text):
    return text[::-1]

def is_palindrom(text):
    return text == revers(text)

text = input(" Enter any word: ").lower().strip()
if is_palindrom(text):
    print(' This is a palindrom!')
else:
    print(' This is not a palindrom!')

