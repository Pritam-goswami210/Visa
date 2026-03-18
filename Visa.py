
Bankbalance = float(input("Entre your bank balance-----> "))
age = int(input("Entre your age-----> "))
pasport = (input("If you have a passport type yes and if you don't have type no---> "))
def new_func(question):
    print(question)

if(pasport == "no"):
    print( "Access Denied: You need a passport to travel!")
    exit()
elif(pasport == "yes"):
    print("You can travel")
    if(Bankbalance==500000):
     print("Visa Approved: Welcome to your international trip! 🌟")
    elif(Bankbalance>=500000):
     print("Visa Approved: Welcome to your international trip! 🌟")
elif(Bankbalance<=500000):
        print("Visa Denied: You need more savings for an adult visa. 🛑")
        if(age>=18):
            print("You can travel🙂")
        elif(age<18):
            question = ("Do you have a Parent's Permission Letter? yes/no") 
            new_func(question)
            if(question =="yes"):
             question1 = ("Entre your bank balance:- ")
            print(question1)                
if(question1 == 200000):
                print("Visa Approved: Have a safe school trip! 🎒")
elif(question1>=200000):
                     print("You can travel enjoy youe trip 😍")
elif(question1<=200000):
                    print( "Visa Denied: You need both a letter and ₹2 Lakhs. 🛑")


                
