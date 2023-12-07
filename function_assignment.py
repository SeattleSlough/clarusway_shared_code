# ########## FIZZ BUZZ  ################

def fizz_buzz():
    for num in range(1,101):
        if (num % 3 == 0) and (num % 5 == 0):
            print('FizzBuzz', sep='\n')
        elif num % 3 == 0:
            print("Fizz", sep='\n')
        elif num % 5 == 0:
            print("Buzz", sep='\n')
        else:
            print(num, sep='\n')

fizz_buzz()

##########  LEAP YEAR  #############

def leap_year(year):
    if (year % 400 == 0):
        print(f"{year} is a leap year")
    elif (year % 4 == 0) and (year % 100 != 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

leap_year(2000)
leap_year(1900)


###########   ARMSTRONG NUMBER   #############


def validate_positive_int():
    num = ""

    while True:
        num = input("Please enter a positive integer: ")
        
        if num.isalpha():
            print("Do not use any entries other than numeric values.")
        elif ('.' in num):
            print("Please enter a positive integer.")
        elif (int(num) <= 0):
            print("Please enter a positive integer.")
        else:
            break
    
    return num

def is_armstrong_number():
    num_as_str = validate_positive_int()
    length = len(num_as_str)
    num = int(num_as_str)
    armstrong_total = 0

    for digit in num_as_str:
        armstrong_total += pow(int(digit),length)
    
    if num == armstrong_total:
        print(f"{num} is an Armstrong Number")
    else:
        print(f"{num} is not an Armstrong Number")


is_armstrong_number()