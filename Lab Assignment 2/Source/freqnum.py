import numpy as n

random = n.random.randint(0,20,15) #random int for range 0-20 and maximum size of 15

print('Random list of integers are:', random) #prints the random integers

print('Most freq num in the random list is:', n.bincount(random).argmax()) #prints most frequent numbers in the list