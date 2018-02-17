bookstore = {"DAA":60, "Network":30, "Big Data":50} #list of available books

mini = int(input("Enter the minimum price")) #minimum price
maxi = int(input("Enter the maximum price")) #maximum price

dummy = True #dummy for printing the availble books statement only once in loop

for (key,value) in bookstore.items(): #for  key,value pairs in the book list
    if mini <= value <= maxi:
     if dummy:
         print('Available books for the the price range', mini, 'and', maxi,'are:')
         dummy = False
     print(key) #Prints the price of books in the available range
    else:
     exit(print('No books available')) #No books are available in the given price range
