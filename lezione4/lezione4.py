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

#Write a function check_each(), which takes a list of numbers as argument.
#Using a for loop, iterate through the list.
#For each number, print “bigger” if it’s bigger than 5, “smaller” if it’s smaller than 5,
#and “equal” if it’s equal to 5.

def check_each(numb: list):
    for i in numb:
        if i>5:
            print("bigger")
        elif i<5:
            print("smaller")
        else:
            print("equal")
out=check_each([3,8,6,5,9,1])

#Write a function add_one(). It takes an integer as argument. The function adds 1 to
#the integer and returns it.
#Write another function add_one_to_list(). It takes a list of integers as argument.
#Define a variable new_list in this function.
#Using a for loop, iterate through the argument list.
#Using add_one(), fill new_list with integers from the argument list incremented by 1.
#Print new_list.
#Example:
#add_one_to_list([1, 2, 3])
#>>> [2, 3, 4]

#prima funzione
def add_one(a: int):
    a +=1
    return a
print(add_one(3))

#seconda funzione con argomento lista di interi
def add_one_to_list (integers_list):
    new_list=[]
    for n in integers_list:
        new_list.append(add_one(n))
    print (new_list)
add_one_to_list([4,6,1,9])

