

def a():
    return 5
print(a())     
# prediction: 5

def a():
    return 5
print(a()+a())     
# prediction: 10

def a():
    return 5
    return 10
print(a())     
# prediction: 5

def a():
    return 5
    print(10)
print(a())     
# prediction: 5

def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a)  # prediction: Error. it did not call function a() on the print function 

def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))               # prediction: 7
print(a(5,3))               # prediction: 14
print(a(2,3) + a(5,3))      # prediction: 21  

def a(b,c):
    return b+c
    return 10
print(a(3,5))               # prediction: 8   


b = 500                     
print(b)                    # prediction at this line: 500 
def a():
    b = 300
    print(b)                
print(b)                    # prediction at this line: 500
a()                         # prediction at this line: 300
print(b)                    # prediction at this line: 500


b = 500
print(b)                    # prediction at this line: 500
def a():
    b = 300
    print(b)
    return b
print(b)                    # prediction at this line: 500
a()                         # prediction at this line: 300
print(b)                    # prediction at this line: 500


b = 500
print(b)                    # prediction at this line: 500
def a():
    b = 300
    print(b)
    return b
print(b)                    # prediction at this line: 500
b=a()                       # prediction at this line: 300
print(b)                    # prediction at this line: 300

