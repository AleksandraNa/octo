"game guess a number"

import numpy as np

number = np.random.randint(1, 100) #imagine the number

#number of attempts

count = 0

while True:
    count +=1
    predict_number = int(input('Guess a number from 1 to 100'))
    
    if predict_number > number:
        print('Number is smaller')
    elif predict_number < number:
        print('Number is bigger')
    else:
        print(f"You are right! it is a number {number}, you made {count} attempts")
        break