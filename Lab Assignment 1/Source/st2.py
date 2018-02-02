'inp is a list variable'
inp = list()
# n1 is assigned the number of elements the user wants to add to the list
n1= input("How many numbers would you like to enter:")
# Asks the user to enter the numbers in to the list
print ('Enter the numbers for which you want to find sum of triplets equal to zero  ')
# for loop to enter all the elements given by the user into the inp
for i in range(int(n1)):
# n2 takes each elements and each element is appended to inp from n2
  n2 = input(":")
  inp.append(int(n2))
# Prints the numbers given by the user
print('The numbers entered are',inp)
# funtion to print the sum of triplets equal to zero in the list of numbers
def sumtriplets(x):
  result = []
  x.sort()
  for i in range(len(x)-2):
    if i> 0 and x[i] == x[i-1]:
      continue
    j, k = i+1, len(x)-1
    while j < k:
      sum = x[i] + x[j] + x[k]
      if sum > 0:
        k -= 1
      elif sum < 0:
          j += 1
      else:
         result.append((x[i], x[j], x[k]))
         print('The triplet whose sum is equal to zero in the given list is', result)
         exit()
      print('There are no triplets whose sum is equal to zero')
sumtriplets(inp)

