#10
def ue(lst):
    ul = []
    for item in lst:
        if item not in ul:
            ul.append(item)
    return ul
il= list(map(int, input().split()))
print("#10")
print( ue(il))
