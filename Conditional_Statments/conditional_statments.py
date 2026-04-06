#synatx:--

# if condition:
#     #code
# elif condition:
#     #code
# elif condition:
#     #code
# else:
#     #code        

# finding grade of students 

# marks=77

# if marks >=92:
#     print("A+") 
# elif marks >=81 and marks <=91: #elif 77 >=81 and 77 <=91
#     print("A")  
# elif marks >=71 and marks <81: #71 >> <<81
#     print("B+")         
# else:
#     print("fail")  
#type casting implicit 
# explicit :-- q="1"   q=int("1") q=1

# elif exmple
print("1. 1440p")
print("2. 1080p")
print("3. 720p")
print("4. 480p")
print("5. 360p")
print("6. 2k")

q=int(input("choose quality from above to your video")) # "1"

if q==1:
    print("your streaming 1440p quality video content and ads")
elif q==2:
    print("your streaming 1080p quality video content and ads")
elif q==3:
    print("your streaming 720p quality video content and ads")
elif q==4:
    print("your streaming 480p quality video content and ads")
    
elif q==5:
    print("your streaming 360p quality video content and ads")
elif q==6:
    print("your streaming 2k quality video content and ads")
else:
    print("choose valid option")       



a=10
b=10

# # commented
#  #syntax
# # if condition:
#     #code to execute

if a == b: #if 10 == 10 # if True
    print("vamsi")

if True:
    print("vamsi 222")
 

time=10
supportTime=18
phonpe=True
if phonpe and time >= supportTime : # if True and 10>=18
    print("light on")
else:
    print("no light on")    




if False:
    print("vamsi333")
else:
    print("not true")        

time=10
supportTime=18
phonpe=True
if phonpe and time >= supportTime : # if True and 10>=18
    print("light on")
else:
    print("no light on")    


email ="vamsi@gmail.com"
pswd="12345678"

e=input("enter email here :-- ")
p=input("enter paswd here :-- ")

if email == e and  pswd == p: #if False
    print("login successful")
else:
    print("login failed")    



# nest if example
if True:
    if None == 0: #research topic
        print("line 3")
    else:
        print("line 5") 
else:
    if 100:
        print("line 8") 
    else:
        print("line 10") 