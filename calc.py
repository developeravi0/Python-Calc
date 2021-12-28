print("Calculator Activated")
opr=input("Enter the operator of the operation you want to do - ")
if opr=="+":
    no1=int(input("Enter no1 - "))
    no2=int(input("Enter no 2 - "))
    ans=no1+no2
    print(f"Your sum is {ans}")
elif opr=="-":
    no1=int(input("Enter no1 - "))
    no2=int(input("Enter no 2 - "))
    ans=no1-no2
    print(f"Your diference is {ans}")
elif opr=="*":
    no1=int(input("Enter no1 - "))
    no2=int(input("Enter no 2 - "))
    ans=no1*no2
    print(f"Your product is {ans}")
elif opr=="/":
    no1=int(input("Enter no1 - "))
    no2=int(input("Enter no 2 - "))
    ans=no1/no2
    print(f"Your quotient is {ans}")
elif opr=="**":
    no1=int(input("Enter no1 - "))
    no2=int(input("Enter no 2 - "))
    ans=no1**no2
    print(f"Your answer is {ans}")
elif opr=="mod":
    no1=int(input("Enter no1 - "))
    no2=int(input("Enter no 2 - "))
    ans=no1%no2
    print(f"Your remainder is {ans}")
elif opr=="%":
    no1=int(input("Enter no1 - "))
    no2=int(input("Enter no 2 - "))
    ans=(no1/no2)*100
    print(f"Your answer is {ans}%")
else:
    print("Operation not defined")