def Endscript(text,*keys):
	i = 0
	Etext = ""
	for Char in text:
		Etext += chr((ord(Char)+keys[i])%256)
		i += 1
		if i >= len(keys):
			i = 0
	return Etext
NamePlainText = input("Please enter the file name of the plain text: ")
Key = int(input("Please enter encryption key: "))
NameCipherText = input("Please enter the file name of the cipher text: ")
Pfile = open(NamePlainText,"r")
Cfile = open(NameCipherText,"w")
Cfile.write(Endscript(Pfile.read(),Key))
Pfile.close()
Cfile.close()
