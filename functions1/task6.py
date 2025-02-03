#6
def w(sentence):
    return " ".join(sentence.split()[::-1])

user_input = input()
print("#6")
print(w(user_input))
