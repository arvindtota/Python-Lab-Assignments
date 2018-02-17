from collections import defaultdict

contactlist=[{'name':'Vin', 'number':1111111111, 'email':'ab@yz.com'}, { 'name':'Diesel', 'number':2222222222, 'email': 'cd@ef.com'}] #contact details
print('1)Display contact by name \n'
      '2)Display contact by number \n'
      '3)Edit contact by name \n'
      '4)Exit \n','\nContacts:', contactlist)

while True: #to iterate the loop for displaying above options till the user exits.
 op = int(input("\nSelect option:")) #input for above options

 if op==1:
        name= input("Enter name to search in contacts:") #To display contact using name
        for i in contactlist:
            if i["name"].lower() == name.lower(): #if the entered and available name are same, then it prints the contact list
                print(i)

 elif op==2:
        num=int(input("Enter number to search in contacts:"))  #To display contact using number
        for i in contactlist:
            if i["number"] == num:      # if the entered and available numbers are same, then it prints the contact list
                print(i)

 elif op==3:
        inp = input("Enter name to edit contact details:") #asks for name to edit contact list
        for i in contactlist:
         if i["name"].lower() == inp.lower():   #checks if the name entered by the user and the name in contact list are same or not
          print("a.Edit Name \nb.Edit num \nc.Edit email \n") # Edit options
          ch = input('Select option to edit') #input for options
          if ch.lower() == 'a': #Edit name
            name = input("enter new name:")
            i["name"] = name
            print("updated contact list:",contactlist)

          elif ch.lower() == 'b': #Edit number
            num1=int(input("enter new number:"))
            i["number"]=num1
            print("updated contact list:",contactlist)

          elif ch.lower() == 'c': #Edit email
            email= input("enter new email:")
            i["email"]=email
            print("updated contact list:",contactlist)

          else: #error case
            print('Enter proper option')


 elif op==4: #option to exit program
        print("Program exited")
        break
 else: #error case
        print("enter a proper option")
        break