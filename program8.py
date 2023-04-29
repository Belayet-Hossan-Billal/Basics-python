#random function
'''import random
print("Random number 1=>",random.random())
print("Random number 2=>",random.random())'''

'''import random
print(random.randint(3,9))
'''

'''import random
print(random.randrange(5,8))
'''

'''
import random
list= [3, 4, 5, 6, 7, 9]
random.shuffle(list)
print("shuffle list is",list)
'''

import random
numberList = [234, 124, 151, 631, 432, 234, 123]
print(random.choices(numberList, weights = (10, 20, 30, 40, 50, 60, 70),k=5))