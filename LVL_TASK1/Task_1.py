def Addition(x,y):
    a=x
    b=y
    return a+b
def Subtraction(x,y):
    a=x
    b=y
    return a-b
def Multiplication(x,y):
    a=x
    b=y
    return a*b
def Division(x,y):
    a=x
    b=y
    if b==0:
        print("Error Division by Zero")
    else:
        return a/b
def Calculator():
    while(1):
        print("------------------Calculator------------------")
        print("Select Operations")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Divison")
        print("5.Exit")
        choice=int(input("Enter the Choice(1-5) :"))
        if choice==5:
            print("\n invalid choice!!! ")
            break
        elif choice==1:
            x=float(input("Enter the 1st Number :"))
            y=float(input("Enter the 2nd Number :"))
            Result=Addition(x,y)
            print("Result of  Addition is: {:.4f}".format(Result))
        elif choice==2:
            x=float(input("Enter the 1st Number :"))
            y=float(input("Enter the 2nd Number :"))
            Result=Subtraction(x,y)
            print("Result of  Subtraction is : {:.4f}".format(Result))
        elif choice==3:
            x=float(input("Enter the 1st Number :"))
            y=float(input("Enter the 2nd Number :"))
            Result=Multiplication(x,y)
            print("Result of Multiplication is: {:.4f}".format(Result))
        elif choice==4:
            x=float(input("Enter the 1st Number :"))
            y=float(input("Enter the 2nd Number :"))
            Result=Division(x,y)
            print("Result of Division is: {:.4f}".format(Result))
        '''else:
            print("\n invalid choice!!! ")
            break'''
Calculator()
print("------------------End------------------")

            
        
            
            
            
    
