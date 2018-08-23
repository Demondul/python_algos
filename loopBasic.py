for i in range(1,151):
    print(i)

for i in range(5,1000001,5):
    print(i)

for i in range(1,101):
    if i%5==0:
        print("Coding")
    if i%10==0:
        print("Dojo")
    
sum=0
for i in range(1,500000,2):
    sum=sum+i
print(sum)

for i in range(2018,1,-4):
    print(i) 


lowNum=2
highNum=9
mult=3
for i in range(lowNum,highNum+1):
    if i%mult == 0:
        print(i)