#Prints header of the application
print('Welcome common courses finder application ')
#List of students who are enrolled in Python course
python= "Arvind", "Hari", "Rahul", "Avinash", "Smaran"
#List of students who are enrolled in web application course
web_application = "Arvind", "Hari", "Vivek"

#Prints the list of students who are enrolled in common courses
print('The students enrolled in common courses are:', set(python) & set(web_application))

#Prints the list of students whose courses are not common
print('The students enrolled in different courses are:', set(python) ^ set(web_application))




