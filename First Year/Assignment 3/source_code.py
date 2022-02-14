print("\n       QUESTION - 1\n")

inputString = input("Enter the string: ").lower().split()
if len(inputString) == 1:
    inputString = inputString[0]
countDict = {}
for i in inputString:
    if i in countDict:
        countDict[i] += 1
    else:
        countDict[i] = 1
print("The occurence(s) of:")
for i in countDict.keys():
    print(i,":",countDict[i])
        
print("\n       QUESTION - 2\n")    

print("Please enter numerical values only.\n")

day=0
month=0
year=0
month30 = [4,6,9,11]

while True: #this loop runs until all the conditions are satisfied and result is calculated
    day = int(input('Day -'))
    month = int(input('Month -'))
    year = int(input('Year -'))

    if not(1<=month<=12):
        print('Month has been entered incorrectly.\nPlease enter Month as 1<=month<=12')
    if not(1<=day<=31):
        print('Day has been entered incorrectly.\nPlease enter Day as 1<=day<=31')
    if not(1800<=year<=2025):
        print('Year has been entered incorrectly.\nPlease enter Year as 1800<=year<=2025')
    if (month in month30):
        if day > 30:
            print("The month you entered contains only 30 days.\nPlease enter valid date.")
            continue
        
    if (1<=month<=12 and 1<=day<=31 and 1800<=year<=2025):
        #if the 3 given conditions satisfied we check for leap year month boundaries
        
        if (year%4==0 and year != 1800 and year != 1900): #because 1800 and 1900 are not leap years
            if (month == 2):
                if (day <= 29):
                    if day == 29:
                        print("The next Date is 01/03/",year,sep='')
                    else:
                        print("The next Date is ",day+1,"/02/",year,sep='')
                    break
                else:
                    print("Year entered is leap year.\nThere are only 29 days in the 2nd month of a leap year.\nPlease enter data correctly.")
            else: #month entered is not February so no need to check
                break
        elif (month == 2 and day <= 28):
            if day == 28:
                print("The next Date is 01/03/",year,sep='')
            else:
                print("The next Date is ",day+1,"/02/",year,sep='')
            break
        else:
            break

if day != 30 and day != 31:
    print("The next Date is ",day+1,"/",month,"/",year, sep = '')
elif day == 30:
    if month in month30:
        print("The next Date is 01/",month+1,"/",year, sep = '')
    else:
        print("The next Date is ",day+1,"/",month,"/",year, sep = '')
else:
    if month == 12:
        print("The next Date is 01/01/",year+1, sep = '')
    else:
        print("The next Date is 01/",month+1,"/",year, sep = '')
            

print("\n       QUESTION - 3\n")

while True:
    print('How many numbers do you want to add? ')
    
    listLengthC = input()
    #checks input type
    if not(listLengthC.isnumeric() and int(listLengthC)>0):
        print('Enter positive integer')
        continue
    listLength= int(listLengthC)
    
    numList = []
    for i in range(listLength):
        print('Enter number ',i+1,': ', end = '',sep='')
        
        numList.append(int(input()))

    numSquareList = []
    for num in numList:
        numSquareList.append((num,num**2))
    break

print('Result:',numSquareList)

print("\n       QUESTION - 4\n")

while True: #invalid input checker
    print('Enter grade of student')
    gradePoint = input()
    if gradePoint.isnumeric():
        if not (4<=int(gradePoint)<=10):
            print("Input invalid. Grade should be an integer between 4 and 10.")
            continue
        else:
            break
    else:
        print("Input invalid. Grade should be an integer between 4 and 10.")    

gradeDict = {"10":("A+", "Outstanding"), "9":("A", "Excellent"), "8":("B+", "Very Good"),\
             "7":("B", "Good"), "6":("C+", "Average"), "5":("C", "Below Average"), "4":("D", "Poor")}

print('Your Grade is ', gradeDict[gradePoint][0], ' and ', gradeDict[gradePoint][1],".",sep='')

print("\n       QUESTION - 5\n")
#program is made in such a way that we can have any kind of baseString

baseString = "ABCDEFGHIJK"

for lineCount in range(1, int((len(baseString)+1)/2)+1): #range is adjusted acccording to the number of lines
    print(' '*(lineCount-1), end = '')

    for letterCount in range(1, len(baseString)-2*lineCount+3): #we chop off two letters from the end of baseString
        print(baseString[letterCount-1],end = '')               #after each line
    print()

print("\n       QUESTION - 6\n")

print("Please enter unique SID and correct Name everytime.")

register = {}
ans = 'y'
while ans == 'y':
    print("Enter SID of Student - ", end = '')
    SID_test = input()
    SID = 0 #variable declaration so as to not get scope issues

    if SID_test.isnumeric():
        if len(SID_test) == 8:
            SID = int(SID_test)
        else:
            print("SID must contain only 8 digits.\nPlease enter valid SID.")
            continue
    else:
        print("Please enter valid numeric SID.")
        continue

    print("Enter Name of Student - ", end = '')
    name = input()
    
    register[SID] = name

    while True:
        ans = input("Do you want add more students? Enter Y or N - ").lower()
        if ans == 'y' or ans == 'n':
            print()
            break
        else:
            print("Please enter Y or N")

print("a) The Students' details are as follows - ")

for SID1 in list(register.keys()):
    print("SID -", SID1, "Name -", register[SID1])

print()

#Sort by names
nameSorted = sorted(register.values())
registerSort1 = {}

for i in range(len(nameSorted)):
    name = nameSorted[i]

    #the following method is to find out which name is related to which SID(key)
    SID = list(register.keys())[list(register.values()).index(name)]
    registerSort1[SID] = name

print("b) Dictionary sorted by student names =", registerSort1)
print()

SIDSorted = sorted(register)
registerSort2 = {}
for i in range(len(SIDSorted)):
    SID = SIDSorted[i]
    name = register[SID]
    registerSort2[SID] = name

print("c) Dictionary sorted by SID's =", registerSort2)
print()

print("d) Student details' search")

while True:
    print("Enter Student's SID - ", end = '')
    SID = int(input())

    if SID in register:
        print("Student's name is", register[SID])
        break
    else:
        print("SID not found in register.\nPlease recheck and enter again.")
            
print("\n       QUESTION - 7\n")

totalTerms = int(input("How many terms do you want to print? "))

num1 = 0
num2 = 1
total = 1 #because of first 2 terms
count = 2 #because 2 terms are already there

print(num1,num2,end=' ')
while count < totalTerms:    
    num3 = num1 + num2
    print(num3,'',end='')

    num1 = num2
    num2 = num3
    count += 1
    total += num3

avg = total/totalTerms
print('\nAverage of first',totalTerms,'terms =',avg)

print("\n       QUESTION - 8\n")

set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}
set3 = {1, 5, 9, 13, 17}

setSymDiff = set1 ^ set2
setSymDiffAll = set1 ^ set2 ^ set3
set4 = ((set1&set2) | (set2&set3) | (set3&set1)) - (set1&set2&set3)

set5 = {1,2,3,4,5,6,7,8,9,10} - set1
set6 = {1,2,3,4,5,6,7,8,9,10} - set1 - set2 - set3

print("a)", setSymDiff)
print("b)", setSymDiffAll)
print("c)", set4)
print("d)", set5)
print("e)", set6)




