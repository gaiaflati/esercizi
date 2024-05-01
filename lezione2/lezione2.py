#Gaia Flati
#18/04/2024

print ("Hello World")

#2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. 
#Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

name: str= "Mario"
message: str= f"ciao {name}, ti va di imparare un po' di python insieme?"
print(message)

#2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.

name: str= "Mario"
lower_name: str= name.lower()
upper_name: str= name.upper()
print(name, lower_name, upper_name)

#oppure
print(f"{name}, {name.upper()}, {name.lower()}")

#2-5. Famous Quote: Find a quote from a famous person you admire. 
#Print the quote and the name of its author. 
#Your output should look something like the following, including the quotation marks: Albert Einstein once said,
# “A person who never made a mistake never tried anything new.”

name: str= "Albert Einstein"
quote: str= "A person who never made a mistake never tried anything new."
print(f"{name} once said, \"{quote}\" ")

#2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. 
#Then compose your message and represent it with a new variable called message. Print your message. 

famous_person: str="Albert Einstein"
message: str= f"{famous_person} once said, \"{quote}\""
print(message)

#2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). 
#Assign the value 'python_notes.txt' to a variable called filename. 
#Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.

filename: str= "python_notes.txt"
print(filename.removesuffix(".txt"))

#3-1. Names: Store the names of a few of your friends in a list called names. 
#Print each person’s name by accessing each element in the list, one at a time.

names: list=["mario","matteo","davide","giulia"]

for i in names:
    print(i)

#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them.
#The text of each message should be the same, but each message should be personalized with the person’s name.

#uso la lista dell'es 3-1
for i in names:
    print("ciao,",i, "sei bello")

#3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
#Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

transports: list=["audi","ford","bmw","fiat"]
for i in transports:
    print("vorrei comprare un'auto",i)
    print("la mia marca preferita di auto è: ",i)

#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
#Make a list that includes at least three people you’d like to invite to dinner. 
#Then use your list to print a message to each person, inviting them to dinner.

guest_list: list=["Alessandro Borghi","Leonardo Di Caprio","Beyonce"]
for i in guest_list:
    print(f"ciao, {i} vuoi venire a cena con me?")

#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
# You’ll have to think of someone else to invite.
#• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
#• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#• Print a second set of invitation messages, one for each person who is still in your list.

guest_list: list=["Alessandro Borghi","Leonardo Di Caprio","Beyonce"]
for i in guest_list:
    print(f"ciao, {i} vuoi venire a cena con me?")
print(f"{guest_list[1]} non può venire alla cena")
guest_list[1]= "Van Gogh"
for i in guest_list:
    print (f"{i}, ti andrebbe di cenare con me?")

#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
#• Use insert() to add one new guest to the beginning of your list.
#• Use insert() to add one new guest to the middle of your list.
#• Use append() to add one new guest to the end of your list.
#• Print a new set of invitation messages, one for each person in your list.    

guest_list: list=["Alessandro Borghi","Leonardo Di Caprio","Beyonce"]
for i in guest_list:
    print(f"ciao, {i} vuoi venire a cena con me?")
print("ho trovato un ristorante con un tavolo più grande")
guest_list.insert(0,"pippo")
guest_list.insert(2,"Pluto")
guest_list.append("topolino")
for i in guest_list:
    print(f"ciao, {i} abbiamo cambiato posto per la cena, ci vediamo alle 20")

#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner,
#and now you have space for only two guests.
#• Start with your program from Exercise 3-6.
# Add a new line that prints a message saying that you can invite only two people for dinner.
#• Use pop() to remove guests from your list one at a time until only two names remain in your list. 
#Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#• Print a message to each of the two people still on your list, letting them know they’re still invited.
#• Use del to remove the last two names from your list, so you have an empty list.
# Print your list to make sure you actually have an empty list at the end of your program.

print("posso invitare solo due persone")

print(f"sono davvero dispiaciuta,",{guest_list[0]}," ma non posso più invitarti alla cena")
guest_list.pop(0)

print(f"sono davvero dispiaciuta,",{guest_list[1]}," ma non posso più invitarti alla cena")
guest_list.pop(1)

print(f"sono davvero dispiaciuta,",{guest_list[2]}," ma non posso più invitarti alla cena")
guest_list.pop(2)

print(f"sono davvero dispiaciuta,",{guest_list[-1]}," ma non posso più invitarti alla cena")
guest_list.pop(-1)

for i in guest_list:
    print ("ciao,",i,"sei ancora invitato alla cena")
del guest_list[:]
print(guest_list)

#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
#• Store the locations in a list. Make sure the list is not in alphabetical order.
#• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
#• Use sorted() to print your list in alphabetical order without modifying the actual list.
#• Show that your list is still in its original order by printing it.
#• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
#• Show that your list is still in its original order by printing it again.
#• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
#• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#• Use sort() to change your list so it’s stored in reverse-alphabetical order.
#Print the list to show that its order has changed.
places=["svezia","cuba","giappone","rio","portogallo",]
print(places)
print(sorted(places))



#3-9. Dinner Guests: Working with one of the programs from Exercises 3,
#use len() to print a message indicating the number of people you’re inviting to dinner.
print(f"il numero di invitati alla cena è: {len(guest_list)}")


#3-10. Every Function: Think of things you could store in a list. 
#For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
#Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

languages=["italiano","inglese","francese","spagnolo"]
languages.pop(2)
languages.append("portoghese")
languages.insert(1,"giapponese")
languages[0].upper
print(languages)

#6-1. Person: Use a dictionary to store information about a person you know. 
#Store their first name, last name, age, and the city in which they live.
#You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

antonella_dict={"first_name": "antonella", "last_name": "riposati", "age": 64, "city": "ladispoi"}
print (antonella_dict.values())

#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. 
#Think of five names, and use them as keys in your dictionary. 
#Think of a favorite number for each person, and store each as a value in your dictionary.
#Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

favorite_number={"gaia": 3, "lorenzo": 7, "matteo": 16, "giulia": 23, "viola": 12}
for key in favorite_number:
    print(f"il numero preferito di {key} è: ", favorite_number.get(key))

#6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#• Think of five programming words you’ve learned about in the previous chapters.
#Use these words as the keys in your glossary, and store their meanings as values.
#• Print each word and its meaning as neatly formatted output. 
#You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. 
#Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

glossary={"insert": "inserisce un elemento alla lista specificando l'indice", "pop": "rimuove un elemento della lista specificando l'indice", "append": 
          "aggiunge un elemento alla fine della lista", "print": "stampa", "upper": "trasforma una stringa in maiuscolo"}
for key in glossary:
    print(key, glossary.get(key))

#6-7. People: Start with the program you wrote for Exercise 6-1.
#Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
#Loop through your list of people. As you loop through the list, print everything you know about each person.

leonardo_dict={"first_name": "leonardo", "last_name": "servetti", "age": 23, "city": "ladispoli"}
roberta_dict={"first_name": "roberta", "last_name": "giuntini", "age": 25, "city": "ladispoli"}
people=[antonella_dict,roberta_dict,leonardo_dict]
for i in people:
    print(i.values())

#6-8. Pets: Make several dictionaries, where each dictionary represents a different pet.
#In each dictionary, include the kind of animal and the owner’s name. 
#Store these dictionaries in a list called pets. Next, loop through your list and as
#you do, print everything you know about each pet. 

dog={"kind": "dog", "owner": "monica"}
cat={"kind": "cat", "owner": "davide"}
parrot={"kind": "parrot", "owner": "luca"}
pets=[dog,cat,parrot]
for i in pets:
    print(i.items())

#6-9. Favorite Places: Make a dictionary called favorite_places.
#Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 
#To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. 
#Loop through the dictionary, and print each person’s name and their favorite places.

favorite_places={"lorenzo": ["giappone","indonesia","kenya"],"oussama": ["marocco","spagna","brasile"], "francisco":["alaska","italia","brasile"]}
for key in favorite_places:
    print(key,favorite_places.get(key))

#6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
#Then print each person’s name along with their favorite numbers.

favorite_number={"gaia": [3,13] , "lorenzo": [7,31], "matteo": [16,99], "giulia": [23,5], "viola": [12,48]}
for key in favorite_number:
    print(f"i numeri preferit di {key} sono: ", favorite_number.get(key))

#6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
#Create a dictionary of information about each city and include the country that the city is in, its approximate population, 
#and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. 
#Print the name of each city and all of the information you have stored about it.
cities : dict = [{"city": "Rome",
                  "country": "Italy",
                  "population": "2.873 mln",
                  "fact": "Rome wasn't always the capital city"},
                  {"city": "Paris",
                   "country": "France",
                   "population": "2,145 mln",
                   "fact": "The Louvre is the largest museum in the world"},
                   {"city": "Barcelona",
                    "country": "Spain",
                    "population": "1,62 mln",
                    "fact": "Barcelona has two official languages"}]

for i in cities:
    print(f"these are the details of {i["city"]}: country={i["country"]}, population={i["population"]}, fact={i["fact"]}.")


