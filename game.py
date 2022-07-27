#Game "Guess the number"

import numpy as np
number = np.random.randint(1, 101)
count = 0

while True:
    count += 1
    predict_number = int(input('Please input your number'))
    
    if predict_number > number:
        print('The number is lower')
    elif predict_number < number:
        print('The number is higher')
    else:
        print(f'You are right! the number is {number}. You have made {count} attempts')