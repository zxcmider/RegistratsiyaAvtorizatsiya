import random
def avtoparol()->str:
	str0=".,:;!_*-+()/#¤%&"
	str1 = '0123456789'
	str2 = 'qwertyuiopasdfghjklzxcvbnm'
	str3 = str2.upper() 
	str4 = str0+str1+str2+str3
	ls = list(str4) 
	random.shuffle(ls) 
	psword = ''.join([random.choice(ls) for x in range(12)])
	print(psword)