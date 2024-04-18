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

