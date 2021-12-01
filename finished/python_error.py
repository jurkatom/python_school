#1) Oprava kódu (6)
print("1) Oprava kódu (6)\n")

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is', seasons[3], "\n")

#2) Oprava kódu (7)
print("2) Oprava kódu (7)\n")

message =""

for number in range(10):
    # use a if the number is a multiple of 3, otherwise use b
    if (number % 3) == 0 and number!=0:
        message = message + "a"
    else:
        message = message + "b"
print(message, "\n")

#3) Dotaz na uživatelské jméno (12)
print("3) Dotaz na uživatelské jméno (12)\n")

name = input("What is your name?\n")
number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

if(name[0:1].islower() == True):
    raise Exception("Your name should start with capital letter, try again!\n")

for letter in name:
    if letter in number_list:
        raise Exception("Your name contains number(s), try again!\n")
    if letter == " ":
        raise Exception("Your name contains space(s), try again!\n")

#4) Dělení čísel (13)
print("\n4) Dělení čísel (13)\n")

def int_division():
    num1=input("Give me the first integer: ")
    while True:
        num2=input("Give me the second integer: ")
        if num2!="0":
            break
        print("You cannot divide by zero! Try again!")
    
    try:
        num1=int(num1)
        num2=int(num2)
    except:
        raise Exception("Those were not integers!")
        
    result=num1/num2
    return str(result)
        
print(int_division(),"\n")

#5) Debugování (16)
print("5) Debugování (16)\n")

year = int(input("Greetings! What is your year of origin? "))
if year <= 1900:
    print("Woah, that\'s the past!")
elif year > 1900 and year < 2020:
    print("That's totally the present!")
else:
    print("Far out, that's the future!!")

