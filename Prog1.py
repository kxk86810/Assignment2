First_name = input("Enter the first name: ")
Last_name = input("Enter the last name: ")
fullName = First_name + " " + Last_name

def Full_name(fn,ln):
    print("Full name is: " + fn +" "+ ln)

Full_name(First_name, Last_name)

def string_alternative(str):
    output = ""
    for i in range(len(str)):
        if (i%2)==0:
            output+=str[i]

    print("String Alternative :",output)

string_alternative(fullName)