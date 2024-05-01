import random
#1. School Grading System:
#Create a function that takes a student's name and their scores in different subjects as input.
#The function calculates the average score and prints the student's name, average,
#and a message indicating whether the student passed the exam (average >= 60) or failed.
#Create a for loop to iterate over a list of students and scores, calling the function for each student.
students=["gaia","lorenzo","oussama", "marco"]
voti_gaia=[30,60,100,80,75]
voti_lorenzo=[20,55,86,98]
voti_oussama=[73,62,54,81]
voti_marco=[10,15,84,53]
def students_score(name: str,marks: list): #-> str 
    average= sum(marks)/len(marks)
    if average >= 60:
        print(f"the student passed the exam with an average of {average}, congratulations {name}!! ")
    else:
        print(f"you failed the exam. your average is of {average}, try again next year, {name}.")       
    
for i in students:
    if i=="gaia":
        students_score(i,voti_gaia)
    elif i=="lorenzo":
        students_score(i,voti_lorenzo)
    elif i=="oussama":
        students_score(i,voti_oussama)
    elif i=="marco":
        students_score(i,voti_marco)

#2. Guess the Number Game:
#Create a function that generates a random number within a range specified by the user.
#Prompt the user to guess the number within a specified maximum number of attempts.
#Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
#Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.
range__number=int(input("inserisci un range per il numero da indovinare: "))
def random_number(range_number):
    number=random.randint(0,range_number)
    guess_number=int(input("indovina il numero, hai al massimo 3 tentativi. "))
    i=1
    while i<=3:
        if guess_number==number:
            print("hai vinto")
            break
        elif guess_number < number:
            guess_number= int(input("hai sbagliato, prova un numero più grande"))
        elif guess_number > number:
            guess_number= int(input("hai sbagliato, prova con un numero più piccolo"))   
        i+=1
        
out=random_number(range__number)

#3. E-commerce Shopping Cart:
#Create a function that defines a product with a name, price, and quantity.
#Create a function that manages the shopping cart, allowing the user to add, remove, and view products in the cart.
#The function should calculate the cart total and apply any discounts or taxes.
#Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.
"""
def shopping_cart(x):
    shirt_item= {"name": "shirt", "price": 19.99, "quantity": 1 }
    skirt_item={"name": "skirt", "price": 9.99, "quantity": 1}
    trousers_item={"name": "trousers", "price": 25, "quantity": 1}
    item= input("scegli un articolo tra 'shirt', 'skirt' e 'trousers'. ")
    add=input("inserisci la quantità")
    
    product=[]   #fatto una lista con i prodotti
    if item=="shirt":
        product.append(item)
        shirt_item["quantity"]= add
    elif item=="skirt":
        product.append(item)
        skirt_item["quantity"]= add
    elif item=="trousers":
        product.append(item)
        trousers_item["quantity"]= add
    
    prices=[]    #fatto una lista con i prezzi moltiplicati per le quantità
    if item=="shirt":
        prices.append(shirt_item["price"])
        if add!= 1:
            prices.append(shirt_item["price"*add])
    elif item=="skirt":
        prices.append(skirt_item["price"])
        if add!= 1:
            prices.append(skirt_item["price"*add])
    elif item=="trousers":
        prices.append(trousers_item["price"])
        if add!= 1:
            prices.append(trousers_item["price"*add])
"""

#4. Text Analysis:
#Create a function that reads a text file and counts the number of occurrences of each word.
#The function should print a report showing the most frequent words and their number of occurrences.
#You can use a for loop to iterate over the words in the text and a dictionary to store the occurrences.
#Implement error handling to handle missing files or other input issues.





