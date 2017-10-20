'''
MIT License

Copyright (c) 2017 Kasemsanm

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''


# Show Output Text On Terminal.
print ("Hello World")

# Get Input On Terminal And Show input.
A = input("Enter the text : ")
print (A)

# Basic Condition
# Condition must be a comparison and the results are only true or false.
# Comparison uses the symbol.
# == 	->  equal to
# !=	-> 	not equal
# >		-> 	greater than
# <		-> 	less than
# >=	-> 	greater than or equal to
# <=	-> 	less than or equal to
# Logic is used. 
# and 
# or 
# not 
A = 5
B = 10
if A > B and B > 0 : #  
	print(A)

# If you are writing more than one line, use this.
if A > B and \
   B > 0 :  
	print(A)

# Basic Loop 
# Show Hello World 10 times
# for loop
for x in range(0,10):
 	print("Hello World")

# while loop
x = 0
while x < 10:
	print("Hello World")
	x += 1 # you can't x++ 