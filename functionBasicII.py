#1
def countdown(num):
    newArr=[]
    for i in range(0,num):
        newArr.append(num-i)
    return newArr

#2
def printAndReturn(arr):
    print(arr[0])
    return arr[1]

#3
def firstPlusLength(arr):
    if len(arr)>0:
        return arr[0]+len(arr)
    else:
        return 0

#4
def valuesGreaterThanSecond(arr):
    if len(arr)<=1:
        return False
    else:
        newArr=[]
        for i in range(0,len(arr)):
            if arr[i]>arr[1]:
                newArr.append(arr[i])
        print("There are " + str(len(newArr)) + " values is greater than the 2nd value of array.")
        return newArr

#5
def thisLengthThatValue(num1,num2):
    newArr=[]
    if num1 == num2:
        print("Jinx!")
    
    for i in range(0,num1):
        newArr.append(num2)
    
    return newArr



""" 
arr = countdown(5)
for i in range(0,len(arr)):
    print(arr[i])
 """
#print(printAndReturn([3,6]))    

#print(firstPlusLength([3,4,5,6]))

""" 
arr = valuesGreaterThanSecond([1,1,4,6,7,3,2,1,1,1])
if arr:
    for i in range(0,len(arr)):
        print(arr[i])
else:
    print(str(arr))
     """


""" arr = thisLengthThatValue(4,4)
for i in range(0,len(arr)):
        print(arr[i])
 """