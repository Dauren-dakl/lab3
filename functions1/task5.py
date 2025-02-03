#5
def g(s, step=0):
    if step == len(s):
        print("#5".join(s))
    for i in range(step, len(s)):
        s1 = [c for c in s]
        s1[step], s1[i] = s1[i], s1[step]
        g(s1, step + 1)

u = list(input())
g(u)

