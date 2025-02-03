#13
def gn():
    print("Hello! What is your name?")
    name = input()
    
    print(f"Well, {name}, think of a number between 1 and 20 (only you know it).")
    snumber = int(input("Enter the number you thought of (1-20) for the game to work: "))  
    
    gt = 0  
    while True:
        print("Take a guess.")
        gq = int(input()) 
        gt += 1  
        
        if gq < snumber:
            print("Your guess is too low.")
        elif gq > snumber:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed the number in {gt} guesses!")
            break  


gn()