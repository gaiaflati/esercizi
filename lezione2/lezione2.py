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

names=["mario","matteo","davide","giulia"]

for i in names:
    print(i)