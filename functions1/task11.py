#11
def ip(word):

    cw = ''.join(char.lower() for char in word if char.isalnum())
    return cw == cw[::-1]


us = input()
if ip(us):
    print("#11 palindrome")
else:
    print("#11 not a palindrome")