def calc():
    n=int(input("Enter the first number :"))
    oper=input("Enter the operation to do: ")
    if(oper=="+" or oper=="-" or oper=="/" or oper=="*"):
        p=int(input("Enter the second number: "))
        if oper=="+" :
            return n+p
        elif oper=="-":
            return n-p
        elif oper=="/":
            return n/p
        else:
            return n*p
    else:
        print("Enter valid operation from + - / *")



a=calc()
print(a)
