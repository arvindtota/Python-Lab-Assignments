class Library(object):
    __name_of_library = "MNL" #Private member

    def __init__(self,name,add,pin): #Constructor
        self.name = name
        self.add = add
        self.pin = pin
        print("Library Name: ", Library.__name_of_library) #Library name

class Person: #Person class
    def __init__(self,name,mail,pno):
        self.name = name
        self.mail = mail
        self.pno = pno
    def display(self):
        print("Name of person: ", self.name)
        print("mail: ", self.mail)
        print("Phone: ", self.pno)

class Student(Person):  #inheritance from person class
    stucount = 0
    def __init__(self,name,mail,stu_id,pno):
        Person.__init__(self,name,mail,pno)
        self.stu_id = stu_id
        Student.stucount +=1
    def displayCount(self):
        print("Total Students:", Student.stucount-2)
    def display(self):
        print("\nStudent Details:")
        Person.display(self)
        print("SSO: ",self.stu_id)
        print("Phone",self.pno)

class Librarian(Person): # inheritance of Person class, contains librarian details
    stucount = 0
    def __init__(self,name,mail,staff_id,pno):
        super().__init__(name,mail,pno)  #super class
        self.staff_id = staff_id
    def display(self):
        print("\nStaff Details:")
        Person.display(self)
        print("Staff Id: ",self.staff_id)

class Book(): #contains book details
    def __init__(self, bname, author, ISBN):
        self.book_name = bname
        self.author = author
        self.ISBN = ISBN
    def display(self):
        print("\nBook Details")
        print("Book_Name: ", self.book_name)
        print("Author: ", self.author)
        print("ISBN: ", self.ISBN)

class lend_book(Student,Book):   #multiple inheritance, lending books
    def __init__(self, name, mail, stu_id, bname, author, ISBN, pno):
        Student.__init__(self,name,mail,pno,stu_id)
        Book.__init__(self, bname, author, ISBN)
    def display(self):
        print("Book loan Details:")
        Student.display(self)
        Book.display(self)

Personlist= [] #contains all the list of students, staff and books
Personlist.append(Student('Harry', 'harry@hog.com',1, 1234567890))
Personlist.append(Student('Potter', 'potter@hog.com',2, 5132546852,))
Personlist.append(Librarian('Dumble', 'dumble@hog.com',11, 9546582123,))
Personlist.append(Librarian('Snape', 'Snape@hog.com',12, 8546257895, ))
Personlist.append(Book('Wizard Arts', 'Hermoine', 51515151))
Personlist.append(Book('Magic', 'Ron', 15884622))
Personlist.append(lend_book('Potter', 'potter@hog.com',5132546852, 'Wizard Arts', 'Hermoine', 51515151, 1))
Personlist.append(lend_book('Harry', 'harry@hog.com',1234567890, 'Magic', 'Ron', 15884622, 2))

for obj, item in enumerate(Personlist):
    item.display()
    print("\n")
    if obj == len(Personlist)-1:
        item.displayCount()