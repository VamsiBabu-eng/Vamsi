#  Example 
def add():
   a=10
   b=10
   print(a+b)
add()
 
def mul():
     a=10
     b=2
     print(a*b)
mul()
#  Example 
def registration():
    Name_r =input("Enter Name Here:")
    Email_r =input("Enter Email :")
    Paswd_r =input("Enter Password :")
    CPaswd_r =input("Enter Renter Password :")
    if Paswd_r == CPaswd_r:
        print("Registration Successful")
    else:
        print("Password Not Mached")

registration()

def login():
    Email="Vamsi@gmail.com"
    Paswad="123456"
    
    Email_r =input("Enter Email :")
    Paswd_r =input("Enter Password :")
    if Email == Email_r and Paswad ==  Paswd_r:
        print(" login Successful")
    else:
        print(" login credentials invalid")

login()


# Example 2
def dashboard():
    print("Wellcome")


def registration():
    Name_r =input("Enter Name Here:")
    Email_r =input("Enter Email :")
    Paswd_r =input("Enter Password :")
    CPaswd_r =input("Enter Renter Password :")
    if Paswd_r == CPaswd_r:
        print("Registration Successful")
    else:
        print("Password Not Mached")


def login():
    Email="Vamsi@gmail.com"
    Paswad="123456"
    
    Email_r =input("Enter Email :")
    Paswd_r =input("Enter Password :")
    if Email == Email_r and Paswad ==  Paswd_r:
        print(" login Successful")
        dashboard()
    else:
        print(" login credentials invalid")

registration()
login()

