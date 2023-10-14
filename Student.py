# File: Student.py
# Student: Michael-Aidan Suarez
# UT EID: Mjs7275
# Course Name: CS303E
# 
# Date:10/10/2023
# Description of Program: Define a Student class and give the name and grades
# to calculate the average.


class Student:

    def __init__(self, name, exam1 = None, exam2 = None):
        self.__name = name      #initialize the student name
        self.__exam1 = exam1    #initialize the first exam
        self.__exam2 = exam2    #initialize the second exam

    def getName(self):
        return self.__name  #getter for name

    def getExam1Grade(self):   #getter for first exam
        return self.__exam1

    def setExam1Grade(self, exam1):  #setter for first exam
        self.__exam1 = exam1

    def getExam2Grade(self):  #getter for second exam
        return self.__exam2

    def setExam2Grade(self, exam2):  #setter for second exam
        self.__exam2 = exam2

    def getAverage(self):   
        if((self.__exam1 == None) or (self.__exam2 == None)): #checks if the exam grades are equal to none, and will print an error message.
            return ("Some exam grades not available.")
        return(self.__exam1 + self.__exam2)/2  #finds the average for the exam
        
    def __str__(self):
        return ("Student: " + str(self.__name) + "\n" + "  Exam 1: " + str(self.__exam1) + " \n" + "  Exam 2: " + str(self.__exam2))


x = Student("Mike")

print(Student mik

