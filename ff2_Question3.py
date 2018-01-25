import random,string
x=7
i=0
print "Enter lenght of string"
num =input()
correct_char=0
correct_char_pos=0
rand_str=""
rand_str=''.join(random.choice(string.ascii_uppercase) for i in range(num))
print(rand_str)
text=raw_input()
char_string={}
for s in rand_str:
	if s not in char_string:
		char_string[s]=1
	else:
		char_string[s]=char_string[s]+1
for i in text:
	if i in char_string.keys():
		if char_string[i] > 0:
			correct_char+=1
			char_string[i]-=1		
for i in range(num):
	if text[i]==rand_str[i]:
		correct_char_pos+=1
print "Number of characters that are correct but in the wrong place " ,correct_char-correct_char_pos
print "Number of characters that are correct and in the correct place ",correct_char_pos
