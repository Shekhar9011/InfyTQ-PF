#PF-Exer-40
#This verification is based on string match.

num1=10
num2=10

div = lambda x,y: x+y

if(div(num1,num2)%10)==0:
    print("Divisible by 10")
else:
    print("Not Divisible by 10")
