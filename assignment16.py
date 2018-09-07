#Q.1- Write a python script to create a databse of students named Students.
#Q.2- Take students name and marks(between 0-100) as input from user 10 times using loops.
#Q.3- Add these values in two columns named "Name" and "Marks" with the appropriate data type.
#Q.4- Print the names of all the students who scored more than 80 marks.
''' Creating database '''
import pymongo
client=pymongo.MongoClient()
database=client['Students']
''' Creating collection '''
collection=database['Student_Collection']
''' Taking name and marks from user'''
for i in range (1,11):
    print("Enter information of student no.",i)
    name=input("Enter name ")
    marks=int(input("Enter marks "))
    collection.insert_one({'Name':name,'Marks':marks})
''' Printing names of all the students who scored more than 80 marks '''
data=collection.find({ 'Marks':{"$gt" : 80}})
for d in data:
    print(d)
