class Employee:
    def __init__(self,n,a,g,p,s,b,c,u):
        self.name=n
        self.age=a
        self.sex=g
        self.position=p
        self.__salary=s
        self.__password=b
        self.phone_number=c
        self.user=u
    def get_salary(self):
        return self.__salary
    def get_password(self):
        print("wanna see... pasword!")
        opinion=input()
        if opinion=="yes":return self.__password
        else:return "password is hided"
#---------------------- Function which shows user's profile-------------------------------------------------------
def showDetails(obj):
    print("Here you go...\n")
    print("-"*40)
    print("Name of the employee:",obj.name)
    print("Age:",obj.age)
    print("Gender:",obj.sex)
    print("Designation:",obj.position)
    print("Salary:",obj.get_salary())
    print("Phone Number:",obj.phone_number)
    print("Username:",obj.user)
    print("Password:",obj.get_password())
    print("-"*40)
#----------------------- Functions which checks for a certain user-------------------------------------------------
def userExists(d,id_):
    for i in d.keys():
        if d[i].user==id_:
            return i
    return False
#-----------------------Function which modifies User details-------------------------------------------------------
def Set(d):
    print("Hello,",d.name)
    n=int(input("Type 1. to modify name, 0. to be unchanged "))
    if n==1:d.name=input("Enter name: ")
    n=int(input("Type 1. to modify phone no. , 0. to be unchanged "))
    if n==1:d.phone_number=input("Enter new phone no.: ")
    
    print("*****details updated successfully******")
    print()
    return d
#-----------------------Function which Creates a new User profile--------------------------------------------------
def newUser():
    name=input("Enter employee's name: ")
    age=int(input("Enter employee's age: "))
    gender=input("Enter employee's gender: ")
    position=input("Enter employee's position: ")
    salary=input("Enter employee's salary: ")
    password=(input("Enter employee's password: "))
    phone=int(input("Enter employee's phone.no: "))
    userId=int(input("Enter employee's userID: "))
    new=Employee(name,age,gender,position,salary,password,phone,userId)
    return new
#---------------------Initialisation of employee detail's----------------------------------------------------------
d={}
d["e1"]=Employee("Swaraj",34,"male","CEO","2Crores","pqrs$123",8374813172,190011) #1st person
d["e2"]=Employee("Mourya",40,"male","Manager","2lakhs","uvwe%12",8688043071,190019) #2nd person
d["e3"]=Employee("Lochan",28,"male","Team Lead","85k","melam$28",9848152269,190016) #3rd person
d["e4"]=Employee("Indra",35,"male","senior software engineer","65k","rgthj@34",9490641403,190012) #4th person
d["e5"]=Employee("Jayashankar",27,"male","Junior Software Developer","31k","zxcv$#785",8688977065,190044) #5th person
d["e6"]=Employee("Sonu",28,"Female","Project Manager","45K","tzjo%856",9446745277,190030) #6th person
d["e7"]=Employee("Shravika",29,"Female","Consultant","47K","ehr%565",7799274784,190029) #7th person
num=7
#-------------------------------------------------------------------------------------------------------------------
flag=1
while flag:
    print("Enter 1. To display Details of an existing User")
    print("Enter 2. To delete Profile of an existing User")
    print("Enter 3. To Modify detail's of an existing User")
    print("Enter 4. To add a new User")
    choice=int(input())
    
    if choice==1: #show details
        id_=int(input("Please enter the username given by the company:"))
        exists=userExists(d,id_)
        if exists==False:
            print("User doesn't exists")
            print()
        else:
            showDetails(d[exists])

    elif choice==2: #delete User
        id_=int(input("Please enter the username given by the company:"))
        exists=userExists(d,id_)
        if exists==False:
            print("User doesn't exists")
        else:
            del d[exists]
            print("*********User has been deleted*********")
            print()

    elif choice==3: #modify details
        id_=int(input("Please enter the username given by the company:"))
        exists=userExists(d,id_)
        if exists==False:
            print("User doesn't exists")
            print()
        else:
            d[exists]=Set(d[exists])

    elif choice==4: #add User
        d["e"+str(num+1)]=newUser()
        print("*********User has been added succesfully*********")
        num+=1
    else:
        print("Invalid choice")
        print()
        
    print("Type 1 to try again or 0 to quit")
    flag=int(input())


    




