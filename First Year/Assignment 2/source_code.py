print("         QUESTION - 1\n")

iString = 'Python is a case sensitive language'
print('Input string = ',iString)

length = len(iString)
print('a. Length of the input string is', length, 'characters')

reverse = iString[::-1] #extended slicing
print('b. Reversed string(using extended slice) =', reverse)

sliced = iString[iString.find('a case'): iString.find('ive')+3]
#found 'ive' in 'sensitive' then added 3 to adjust the index

print('c. Sliced String =', sliced)

repString = iString.replace('a case sensitive', 'object oriented')
print('d. New string obtained after replacement =', repString)

pString = iString
print('e. The substring \'a\' was found at index = ', end = '')
i = 0
for travel in pString:
    if travel == 'a':
        #this 2nd if statement is to prevent printing of a ',' at the last index
        #we find the index of the last occurence of 'a'
        if i != (len(pString) - pString[::-1].find('a') - 1): 
            print(i, ', ', sep = '', end = '')
        else:
            print(i)
    i += 1

noSpaceString = iString.replace(' ', '')
print('f. New string with spaces removed =', noSpaceString)

print("\n         QUESTION - 2\n")

name = 'Robin Singh'
sid = 21105077
department = 'ECE'
cgpa = 10

print('Hey! %s here!\n\
My SID is %d\n\
I am from %s department and my CGPA is %f'%(name, sid, department, cgpa))

print("\n         QUESTION - 3\n")

a = 56
b = 10
print('a. a&b =', a&b)
print('b. a|b =', a|b)
print('c. a^b =', a^b)
print('d. a << 2 =', a << 2, 'b << 2 =', b << 2)
print('e. a >> 2 =', a >> 2, 'b >> 4 =', b >> 4)

print("\n         QUESTION - 4\n")

#Numbers are stored into a list and then the list is sorted
numberList = [0, 0, 0]
for i in range(len(numberList)):
    numberList[i] = float(input('Enter number %d: '%(i+1)))
numberList.sort()
print('The greatest number =', numberList[2])

print("\n         QUESTION - 5\n")

input_string = input('Enter your string: ')

index = input_string.find('name')
# Because find() function returns -1 when the substring is not found in the given string
if index == -1:
    print('No')
else:
    print('Yes')

print("\n         QUESTION - 6\n")

sideList = [0, 0, 0]
for i in range(len(sideList)):
    sideList[i] = int(input('Enter side %d: '%(i+1)))
sideList.sort()

# Checking if the sum of the smallest 2 side lengths
# is greater than the largest side is sufficient
result =  sideList[0] + sideList[1] > sideList[2]

if result:
    print('Yes')
else:
    print('No')
