#Identify person names in a given piece of text, using dictionaries.
import re
regex = "[a-zA-Z]+"													#Defining regex for tokenizer.

with open("female.txt") as f:										
    female_names = f.readlines()									#Read names line by line and store them in a list.
female_names = [w.strip() for w in female_names]					#Remove \n or newline character from the end of each name.

with open("male.txt") as f:
    male_names = f.readlines()
male_names = [w.strip() for w in male_names]

person_names = female_names + male_names							#Concatenate both the lists to form one big list. Python cool :)						
text = input("Enter some text: ")
tokenized_words = re.findall(regex,text)
ne = [word for word in tokenized_words if word in person_names]		#You have seen the use of this last week. Check if given word is NE.
print("NEs in the given text are: ")
print(ne)
