#1
def biggieSize(arr):
    for i in range(0,len(arr)):
        if arr[i]>0:
            arr[i]="big"
    return arr

#2
def countPositives(arr):
    ctr=0
    for i in range(0,len(arr)):
        if arr[i]>0:
            ctr=ctr+1
    arr[len(arr)-1]=ctr
    return arr

#3
def sumTotal(arr):
    sum=0
    for i in range(0,len(arr)):
        sum=sum+arr[i]
    return sum

#4
def average(arr):
    ave=0
    for i in range(0,len(arr)):
        ave=ave+arr[i]
    ave=ave/len(arr)
    return ave

#5
def length(arr):
    return len(arr)

#6
def minimum(arr):
    if len(arr)==0:
        return False
    min=arr[0]
    for i in range(0,len(arr)):
        if arr[i]<min:
            min=arr[i]
    return min

#7
def maximum(arr):
    if len(arr)==0:
        return False
    max=arr[0]
    for i in range(0,len(arr)):
        if arr[i]>max:
            max=arr[i]
    return max

#8
def ultimateAnalyze(arr):
    dictionary={"sum":0,"ave":0,"min":arr[0],"max":arr[0],"len":0}
    for i in range(0,len(arr)):
        if dictionary["min"]>arr[i]:
            dictionary["min"]=arr[i]
        if dictionary["max"]<arr[i]:
            dictionary["max"]=arr[i]
        dictionary["sum"]=dictionary["sum"]+arr[i]
    dictionary["len"]=len(arr)
    dictionary["ave"]=dictionary["sum"]/dictionary["len"]
    return dictionary

#9
def reverseList(arr):
    if(len(arr)>0):
        limit=int(len(arr)/2)
        for i in range(0,limit):
            temp=arr[i]
            arr[i]=arr[len(arr)-1-i]
            arr[len(arr)-1-i]=temp
    return arr



""" 
arr = biggieSize([-1,-2,4,5,-1,6,-7,8])
for i in range(0,len(arr)):
        print(arr[i])
 """

""" 
arr = countPositives([-1,-2,4,5,-1,6,-7,8])
for i in range(0,len(arr)):
        print(arr[i])
 """

#print(sumTotal([1,2,3,4]))

#print(average([1,2,3,4]))

#print(length([1,2,3,4]))

#print(minimum([1,2,3,4]))

#print(maximum([1,2,3,4]))

""" 
webster=ultimateAnalyze([1,2,3,4])
print("Sum Total: " + str(webster["sum"]))
print("Average: " + str(webster["ave"]))
print("Minimum: " + str(webster["min"]))
print("Maximum: " + str(webster["max"]))
print("Length: " + str(webster["len"]))
 """

""" 
reverseList
arr = reverseList([-1,-2,4,5,-1,6,-7,8])
for i in range(0,len(arr)):
        print(arr[i])
 """
