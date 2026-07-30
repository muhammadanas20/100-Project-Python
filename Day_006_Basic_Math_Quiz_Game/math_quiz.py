import random 

score = 0

for questions in range(1,6):
    left = random.randint(1,12)
    right = random.randint(1,12)
    answer =  int(input(f"{questions}. {left} + {right} :").strip())  
    if answer == left + right:
        print("Correct!")
        score += 1
    else:
        print(f"Not quite! right answer is {left + right}")

print(f"Your Final Score is: {score}")