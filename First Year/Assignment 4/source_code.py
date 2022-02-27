##print("           QUESTION - 1\n")
##
##
##
##print("\n           QUESTION - 2\n")
##
##
##
print("\n           QUESTION - 3\n")

class Student:                                                                                          
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        
    def __del__(self):
        print("\nObject destroyed")
        
name = input("Enter name of student: ")                                                       
roll_no = int(input("Enter SID of student: "))
              
stuObject = Student(name,roll_no)

print("\nThe name of the student is "+name+" and his/her roll number is",roll_no)

del stuObject       

##print("\n           QUESTION - 4\n")
##
##
##
##print("\n           QUESTION - 5\n")
##
##

##print("\n           QUESTION - 6\n")
##
##while True:
##    gWord = input("Enter word uttered by George - ").lower()
##    bWord = input("Enter word made by Barbie - ").lower()
##
##    if(gWord.isalpha() and bWord.isalpha()):
##        if(gWord == bWord):
##            print("Both words are same. Enter different words.")
##        else:
##            break
##    else:
##        print("Please enter a valid word")
##
##gWordSorted = ''.join(sorted(gWord))
##bWordSorted = ''.join(sorted(bWord))
##
##if(gWordSorted == bWordSorted):
##    print("Their friendship is real.")
##else:
##    print("They are fake friends.")
