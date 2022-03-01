print("           QUESTION - 1\n")

def Hanoi(n, fromS, targetS, spareS):
    if n == 1:
        print("move 1 disk from "+fromS+" to "+targetS)
    else:
        Hanoi(n-1,fromS,spareS,targetS)
        Hanoi(1,fromS,targetS,spareS)
        Hanoi(n-1,spareS,targetS,fromS)

Hanoi(3,"stack 1","stack 2","stack 3")

print("\n           QUESTION - 2\n")

n = int(input("Enter number of lines - "))

print("Using Iteration -")
for line in range(1, n + 1):
    C = 1
    for i in range(1, line + 1):
        print(C, end = " ")
        C = int(C*(line - i) / i)
    print("")

print("\nUsing Recursion -")

def pascal(row, column):
    if row < 0 or column < 0:
        return 0
    elif row == 0 and column == 0:
        return 1
    else:
        return pascal(row - 1, column) + pascal(row - 1, column - 1)

for i in range(n):
    for j in range(i+1):
        print(pascal(i,j),"", end='')
    print("")

print("\n           QUESTION - 3\n")

num1 = int(input("Enter first number - "))
while True:
    num2 = int(input("Enter second number - "))
    if num2 == 0:
        print("Second number should not be 0")
    else:
        break

result = divmod(num1,num2)
print("Quotient:",result[0],"   Remainder:",result[1])

ans = callable(divmod)
print("\na)callable() function was used to check if the function(divmod()) was callable.\nAnswer is", ans)

if result != (0,0):
    print("\nb)All values are not zero")
else:
    print("\nb)All values are zero")

result += (4,5,6)
print("\nc)After adding values -",result)
result_copy = result
result = ()
for i in range(len(result_copy)):
    if result_copy[i] <= 4:
        result += (result_copy[i],)

print("After filtration -",result)

result = set(result)
print("\nd)After converting into set datatype -",result)

result = frozenset(result)
print("\ne)Conversion into immutable set -",result)

print("\nf)Maximum value of set =",max(result),"\nIt's hash value =",hash(result))

print("\n           QUESTION - 4\n")

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

print("\n           QUESTION - 5\n")

class EmployeeData:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def printDet(self):
        print("Name - "+self.name+"     Salary -",self.salary)

emp1 = EmployeeData("Mehak", 40000)
emp2 = EmployeeData("Ashok", 50000)
emp3 = EmployeeData("Viren", 60000)

print("Employee Details:")
emp1.printDet()
emp2.printDet()
emp3.printDet()

emp1.salary = 70000
print("\nUpdated Details:")
emp1.printDet()
emp2.printDet()
emp3.printDet()

del emp3
print("\nUpdated Details:")
emp1.printDet()
emp2.printDet()

print("\n           QUESTION - 6\n")

while True:
    gWord = input("Enter word uttered by George - ").lower()
    bWord = input("Enter word made by Barbie - ").lower()

    if(gWord.isalpha() and bWord.isalpha()):
        if(gWord == bWord):
            print("Both words are same. Enter different words.")
        else:
            break
    else:
        print("Please enter a valid word")

gWordSorted = ''.join(sorted(gWord))
bWordSorted = ''.join(sorted(bWord))

if(gWordSorted == bWordSorted):
    print("Their friendship is real.")
else:
    print("They are fake friends.")

