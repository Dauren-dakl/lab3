#3
def solve(numheads , numlegs):
    for chickens in range(numheads + 1 ):
        rabbits = numheads - chickens
        if 4 * rabbits + 2 * chickens == numlegs:
            return chickens , rabbits 
        
    return None 
        
    
numheads = 35 
numlegs = 94

r = solve(numheads , numlegs)
if r:
    chickens , rabbits  = r 
    print(f" #3 chickens = {chickens} and rabbits = {rabbits}"  )
else :
    print("#3 None")
    