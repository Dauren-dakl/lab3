#12
def hm(items1):
    for item2 in items1:
        print('*' * item2)
        
user_input = input("#12 : ")
num12 = list(map(int, user_input.split()))  
hm(num12)
    