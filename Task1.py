while(True):
    register=input("Do you want to register: ")
    if(register.lower()=="no"):
        break
    elif(register.lower()=="yes"):
        username=input("Enter Username: ")
        password=input("Enter Password: ")
        if len(password) < 8:
            print('Invalid Password: length should be greater than 8')
            continue
        elif not any(word.isdigit() for word in password):
            print('Invalid Password: Password should have at least one numeral')
            continue
        elif not any(word.isupper() for word in password):
            print('Invalid Password: Password should have at least one uppercase letter')
            continue
        elif not any(word.islower() for word in password):
            print('Invalid Password: Password should have at least one lowercase letter')
            continue
        else:
            print("Valid Password ")
            break        
    
while(True):
    login=input("Do you want to login: ")
    if(login.lower()=="no"):
        break
    elif(login.lower()=="yes"):
        name=input("Enter Username: ")
        passwrd=input("Enter Password: ")
        if(name!=username or password!=passwrd):
            print("Details not matched")
            continue
        elif(name==username and password==passwrd):
            print("login completed")
            choose=input("Choose anyone from three options: Calculator, Table, Pattern: ")
            if(choose.lower()=="calculator"):
                a = float(input("Give first number: "))
                b = float(input("Give second number: "))
                c = input("Choose one Operator- Add, Subtract, Multiply, Divide: ")
                if(c.lower()=="add"):
                    print(a+b)
                elif(c.lower()=="subtract"):
                    print(a-b)
                elif(c.lower()=="multiply"):
                    print(a*b)
                elif(c.lower()=="divide"):
                    print(a/b)
                break           
            elif(choose.lower()=="table"):
                n=int(input("Table of: "))
                for i in range(1,11):
                    print(n*i)
                break                 
            elif(choose.lower()=="pattern"):
                n=int(input("Pattern till: "))
                num=1
                for i in range(n):
                    num=1
                    for j in range(i+1):
                        print(num, end=" ")
                        num+=1
                    print("\r")
                break
   
    
