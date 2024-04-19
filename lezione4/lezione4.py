#try to define a function named substract ouselves:
#it should take 2 parametres
#inside the function, it should substract the two
#then return the rsult
#After you defined it, call the function with some argument

def substract(x,y):
    return x-y
print(substract(4,7))

#è la stessa cosa di:
#out= substract(x,y)


#Write a function check_value(), which takes a number as an argument.
#Using if / else, the function should print whether the number is bigger, smaller, or equal to 5.

def check_value(x:int):
    if x>5:
        print("il numero è Maggiore a 5")
    elif x<5:   
        print("il numero è minore a 5")
    
    else:
        print("il numero è uguale a 5")

check_value(int(input("inserisci un numero")))

#Exercise 2
#Write a function check_length(), which takes a string as an argument.
#Using if / else, check if the length of the string is bigger, smaller, or equal to 10 characters

def check_length(x: str): 
    if len(x)>10:
        return ("la stringa è > di 10 caratteri")
    elif len(x)<10:
        return ("la stringa è < di 10 caratteri")
    else:
        return ("la stringa è = a 10 caratteri")
print(check_length(input("inserisci una stringa")))

#Exercise 3
#Write a function print_numbers(), which takes a list of numbers as argument.
#Using a for loop, print each number one by on

def print_numbers(list:list):
    for i in list:
        print(i)
print_numbers([2,5,7,3,8,10,4])
