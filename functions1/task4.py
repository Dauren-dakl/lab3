#4
def prime(n):
    if n < 2 :
        return False 
    for i in range(2 , int(n ** 0.5)+1):
        if n % 2 == 0:
            return False
    return True
def f(numbers):
    return [num for num in numbers if prime(num)]
numbers = list(map(int, input().split()))
p = f(numbers)

print("#4 {p}")