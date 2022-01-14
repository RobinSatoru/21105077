#question - 1
#asking for input
print("          1st PROGRAM\n")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

avg = (num1 + num2 + num3)/3

print("The average of the three numbers is = ", avg)

#question - 2
print("\n          2nd PROGRAM\n")
gross_income = round(float(input("Enter your gross income: ")), 2) #income rounded to nearest penny
dependents = int(input("Enter number of dependents: "))

#initializing some constants and variables
tax_rate = 0.20
s_deduction = 10000
d_deduction = 3000

t_income = gross_income - s_deduction - dependents*d_deduction
tax = t_income*tax_rate
                     
print("Your taxable income is: $", round(t_income, 2))
print("Your net income tax: $", round(tax, 2))

#question - 3
print("\n          3rd PROGRAM\n")

student = [21105077, 'Robin Singh', 'M', 'ECE', 9.99]
print("student = [SID, Name, Gender, Branch, CGPA]")
print("output = ", student)

#question - 4
print("\n          4th PROGRAM\n")

mark_list = []
index = 0
while index < 5:
    print("Enter marks of Student ", index+1,": ", end = '')
    mark_list.append(float(input()))
    index += 1
mark_list.sort()
print("Sorted marks: ", mark_list)

#question - 5
print("\n          5th PROGRAM\n")

color = ['red','green', 'white', 'black', 'pink','yellow']
print('Original list: ', color)
del color[3]
print("After removing 4th element: ", color)

color = ['red','green', 'white', 'black', 'pink','yellow']

color[3:5] = ['purple']
print("After replacing black and pink with purple: ", color)






