# function for finding middle, longest and reverse words in a sentence
def mlr(str):
# sentence input
 string = input("Enter sentence:")
# Splitting sentence into words using 'space'
 split = string.split(" ")
# length of the  split sentence
 mid = len(split)

# Prints the output if the length is even
 if (mid % 2 == 0):
    print("The middle words in the given sentence are:",split[int(mid / 2)-1], split[int(mid / 2)])
# Prints the output if the length is odd
 else:
    print("The middle word in the given sentence is:", split[int(mid / 2)])

#Prints the longest word in the given sentence
 print("The longest word in the given sentence is:",max(split, key=len))

#Prints the recerse of each word in the given sentence
 print("The reverse of each word in the given sentence is:",' '.join(word[::-1] for word in split))

mlr(str)

