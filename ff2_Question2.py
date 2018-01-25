import random
import string

#returns random string of len num
def getRandString(num):
	rand_str=''.join(random.choice(string.ascii_uppercase) for i in range(num))
	return rand_str

#count frequency of each character
def getFreq(rand_str):
	char_string={}
	for s in rand_str:
		if s not in char_string:
			char_string[s]=1
		else:
			char_string[s]=char_string[s]+1
	return char_string

#main logic
def game(text,rand_str,player,char_string):
	correct_char=0
	correct_char_pos=0
	num = len(text)	
	for i in text:
		if i in char_string.keys():
			if char_string[i] > 0:
				correct_char+=1
				char_string[i]-=1		
	for i in range(num):
		if text[i]==rand_str[i]:
			correct_char_pos+=1

	print "Stats of :",player
	print "-------------------"
	print "Number of characters that are correct and in the correct place ",correct_char_pos
	print "Number of characters that are correct but in the wrong place " ,correct_char-correct_char_pos

#For user 
num = random.randint(3,10)
rand_str = getRandString(num)
char_string= getFreq(rand_str)
print "Enter a string of length:",str(len(rand_str))
text = str(raw_input())
print("\n")
#print "Random String ",rand_str
#print "User Guess String ",text
game(text,rand_str,"User",char_string)


print"\n"


#For computer
num = random.randint(3,10)
rand_str = getRandString(num)
comp_text = getRandString(num)
char_string = getFreq(rand_str)
#print "Random String ",rand_str
#print "Computer Guess String ",comp_text
game(comp_text,rand_str,"Computer",char_string)
