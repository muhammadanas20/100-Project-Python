import time

seconds = int(input("How many seconds couter?"))

if seconds < 0:
    print("Again run program and enter positive number!")
else:
    for remaining in range(seconds,0,-1): #(start, stop, step) step = -1 backward 
        print(f"{remaining}...",flush=True) #flush clear this line after printing
        time.sleep(1)
    print("Times Up!")