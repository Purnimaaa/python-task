import random
print("PASSWORD GENERATOR")
print("===================")
list_1 = ["Panda","Cat","Lion","Tiger","Dog","Giraffe","Snake","Fox"]
list_2 = ["Apple","Orange","Pineapple","Mango","Peach","Fruits","Avocado","litchi"]
list_3 = ["Ink","Pen","Paper","Bench","Desk","Fan","Door","Window"]

# This is a try and except block. It is used to catch errors.
try:
    user = int(input("How many passwords are needed: "))
    if(user == 0):
        print("please enter a number between 1 and 24")
    elif (user>24):
        print("please enter a number between 1 and 24")
        exit()
    elif(user<=0):
        print("please enter a number between 1 and 24")
        exit()
        
except ValueError:
    print("TypeInteger")
    exit()


def generate_password(password):
    for x in range(user):
        x = x+1
        print(f"{x}-->",random.choice(list_1)+random.choice(list_2)+random.choice(list_3))    
generate_password(user)
