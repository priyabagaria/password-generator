#!/usr/bin/python

import random

def random_pass():
	usrpwd = raw_input("Enter insecure password...\n")
	
	temp = []
	adjectives = []
	animals = []
	skills = []
	names = []

	with open("./adjectives.txt","r") as words:
		 for line in words:
			  adjectives.append(line.rstrip())
		 words.close()

	with open("./animals.txt","r") as words:
		for line in words:
			animals.append(line.rstrip())
		words.close()

	with open("./skills.txt","r") as words:
		 for line in words:
			  skills.append(line.rstrip())
		 words.close()

	with open("./names.txt","r") as words:
		 for line in words:
			  names.append(line.rstrip())
		 words.close()
	
	random.seed()
	
	## Random selection of words from our dictionaries
	adjective = adjectives[random.randint(0,len(adjectives)-1)].title()
	name = names[random.randint(0,len(names)-1)].title()
	animal = animals[random.randint(0,len(animals)-1)].title()
	skill = skills[random.randint(0,len(skills)-1)].title().replace(" ","")
	
	## Generating list of special characters
	special = [x for x in range(32, 48)]
	special.extend([x for x in range(58, 65)])
	special.extend([x for x in range(123, 127)])
	
	## Randomly picking a special character and digit to pad before and after the words
	padsymbol = chr(special[random.randint(0,len(special)-1)]) 
	paddigit = str(random.randint(10,99))
	
	## Picking a random number between 1 and 3 which is the number of times the spl chr is padded
	padcount = random.randint(1,2)
	special.remove(ord(padsymbol))
	
	## Random selection of special character used to join the words
	sepsymbol = chr(special[random.randint(0,len(special)-1)]) 
	switcher = { 0: adjective,
			1 : name,
			2 : animal,
			3 : skill,
			}	
	option1 = random.randint(0,3)
	word1 = switcher[option1]
	r = range(0,option1) + range(option1+1, 3)
	option2 = random.choice(r)
	word2 = switcher[option2]
	temp.extend([usrpwd, word1, word2])
	random.shuffle(temp)
	
	## Randomize the words case
	option = random.randint(1,5)
	switcher = { 0: alternatingWordCase,
			1 : toggleCase,
			2 : allLowerCase,
			3 : allUpperCase,
			4 : capitaliseFirstLetter,
			5 : capitaliseAllExceptFirst,
			}	
	temp = switcher[option](temp)		
	
	temp = sepsymbol.join(temp)
	padding = paddigit + padcount * padsymbol
	newpwd = padding + temp + padding[::-1]
	#print(len(newpwd))
	print("Recommended password: "+ newpwd)
	
	
def alternatingWordCase(words): 
	newlist = []
	for i in range(len(words)):
		if i%2 == 0:
			newlist.append(words[i].upper())	
		else:	
			newlist.append(words[i].lower())
	return newlist
	
	
def toggleCase(words):
	newlist = []
	for word in words:
		new = ''
		for i in range(len(word)):
			if i%2 == 0:
				new += word[i].upper()	
			else:	
				new += word[i].lower()	
		newlist.append(new)
	return newlist
	
	
def allLowerCase(words):
	newlist =  [word.lower() for word in words]
	return newlist
	
	
def allUpperCase(words):
	newlist =  [word.upper() for word in words]
	return newlist
	
			
def capitaliseFirstLetter(words):
	newlist = [word[0].upper() + word[1:].lower() for word in words]
	return newlist
	
					
def capitaliseAllExceptFirst(words):
	newlist = [word[0].lower() + word[1:].upper() for word in words]
	return newlist



if __name__ == "__main__":
	random_pass()
	
	
## To calculate password strength, goto:  http://www.passwordmeter.com/	
