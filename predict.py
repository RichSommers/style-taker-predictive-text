import operator
from os import system
def  clear():
	system('clear')


import sys
fn = sys.argv[1]

with open( fn ,'r') as f:
	fil=f.read()
fil=fil.lower().replace('\n', ' ').split()  #use \n ' ' for short stories


words={}
for i,word in enumerate(fil):
	#if key not in all add it and add next dict word at 1
	#if it is increment the dict in dict
	try:
		if word in words:
			if fil[i+1] in words[word]:
				words[word][fil[i+1]]+=1
			else:
				words[word][fil[i+1]]=1
		else:
			words[word]={fil[i+1]:1}
	except:
		print('')




from random import randint

seed=sys.argv[2]
ogseed=seed
#dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True)[:3]).keys()


final=seed+' '
print(final)
for i in range(30):

	nexts=sorted(words[seed].items(), key=operator.itemgetter(1))[-4:-1]
	#print(nexts)

	try:
		#n=int(input('Next: '))-1 #bc 1 2 are clos 0 1 are not
		n=randint(1,3)
		next=nexts[n]
	except:
		try:
			next=nexts[0]
			seed=next[0]
			final+=next[0]+' '
		except:
			seed=ogseed
			next=seed
			final+=next+' '
	#next=max(words[seed], key=words[seed].get)




clear()
print(final.replace('. ','.\n'))
