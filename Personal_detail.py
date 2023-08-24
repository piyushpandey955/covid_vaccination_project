def name():
    n=input("enter name")
    if n.isalpha()==True:
        return n
    else:
        print("invalid name")

def age():
    age=input("enter age")
    if age.isnumeric():
        return age
        if (age<18):
             print("you are not eligible for vaccination")
    else:
        print("invalid age")

def gender():
    gender=input("enter  your gender")

def pincode():
    pincode=input("enter pincode")
    if (len(pincode)==6 and pincode.isnumeric()==True):
        return pincode
    else:
        print("invalid pincode")

def address():
    address=input("enter address")

def city():
    city=input("enter city")
def phone_num():
    phone_num=input("enter phone no.")
    if (len(phone_num)==10 and phone_num.isnumeric()):
        return phone_num
    else:
        print("invalid no.")

    
#name()
#age()
#gender()
#pincode()
#address()
#city()
phone_num()
