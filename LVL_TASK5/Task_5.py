def Celsius_to_fahrenheit(temperature):
    temp=temperature
    print("The temperature is {:.2f}".format(temp))
    Fahrenheit=(temp*9/5)+32
    print("The {:.2f}".format(temp),"Degree Celsius is equal to : {:.2f}".format(Fahrenheit),"Degree Fahrenheit")
def Fahrenheit_to_celsius(temperature):
     temp=temperature
     print("The temperature is {:.2f}".format(temp))
     Celsius=(temp-32)*5/9
     print("The {:.2f}".format(temp),"Degree Fahrenheit is equal to : {:.2f}".format(Celsius),"Degree Celsius")
def user():
    while(1):
        print("******************************")
        print("Select Operations")
        print("1. Convert Celsius to Fahrenheit")
        print("2.Convert Fahrenheit to Celsius")
        print("3.Exit")
        choice=int(input("Enter the Choice :"))
        if choice==3:
            print("****************Exit*************")
            break
        elif choice==1:
            temperature=float(input("Enter the Temperature :"))
            Celsius_to_fahrenheit(temperature)
        elif choice==2:
             temperature=float(input("Enter the Temperature :"))
             Fahrenheit_to_celsius(temperature)
        '''else:
             print("invalid choice")
             break'''
user()
            
     
    
