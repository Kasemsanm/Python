def Decryption(text):
	f = open("word list.txt","r")
	words = f.read().split()
	correct = False
	keys = [0]
	while True:
		n = 0
		found = 0
		Dtext = ""
		k = 0
		for c in text:
			Dtext += chr((ord(c)-keys[k])%256)
			k += 1
			if k >= len(keys):
				k = 0
		for word in Dtext.split(" "):
			n+=1
			word = word.strip("!\"#$%&'()*+,-./0123456789:;<=>?@[\]^_`{|}~ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ")
			if len(word) < 30 and len(word) != 0:
				if words.count(word.lower()) >= 1:
					found += 1
		if found > n/2:
			return Dtext,"Key is "+str(keys).strip('[]')
		keys[0] += 1
		for i in range(0,len(keys)):
			if keys[i] >= 256:
				if i == len(keys)-1:
					keys.append(0)
					keys[i] = 0
				else:
					keys[i+1] += 1
					keys[i] = 0
NameCipherText = input("Please enter the file name of the cipher text: ")
Cfile = open(NameCipherText,"r")
Kfile = open("Key.txt","w")
Pfile = open("original_text.txt","w")
Ptext = Decryption(Cfile.read())
text = ""
for x in Ptext[0]:
	try:
		if x == "\x92" or x == "\x93" or x == "\x94" or x == "\x85":
			text += "'"
		else:
			text += x
	except:
		pass
Pfile.write(text)
Kfile.write(Ptext[1])
Kfile.close()
Pfile.close()
Cfile.close()