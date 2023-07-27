###1PRINT STATEMENTS
#EXERCISE 1

#print("I love code down python\n")

#EXERCISE 2

#print("Studyng with 'Python Masters' it´s super fun")

#EXERCISE 3

#operation = 333 + 222
#print(operation)

###2STRINGS
#EXERCISE 1

"""
print('Line 1\nLine 2\nLine 3')
"""

#EXERCISE 2
"""
A = '1'
B = '2'
C = '3'
D = '4'
E = '5'
F = '6'
G = '7'
H = '8'
I = '9'

print(A+'\t'+B+'\t'+C+'\n'+D+'\t'+E+'\t'+F+'\n'+G+'\t'+H+'\t'+I+'\n')
"""

#EXERCISE 3
"""
print("Regular Bar: /\nBackslash: \\")
"""

###3INPUTS
#EXE1
"""
carrer = input("What are u studying?\n")
print("You are learning " + carrer)
"""

#EXE2
"""
country = input("Where are you come from?\n")
print("You are from " + country)
"""

#EXE3
"""
name = input("What´s your name?\n")
print("")
last = input("What´s your last name?\n")
print("")

print("Your full name is: " + name + " " + last)
"""

###4VARIABLES
#EXE1
"""
name = "Ada Lovelace"
age = 37
"""
#EXE2
"""
name = "Bill"
lastName = "Gates"

fullName = name + " " + lastName
"""

#EXE3
"""
course = "Python"
sentence = "You are taking the course of " + course
"""

###5INTS&FLOATS&NUMS
#EXE 1
"""
integerNum = 5
print(type(integerNum))
"""

#EXE 2
"""
decimalNum = 1.1

print(type(decimalNum))
"""

#EXE 3
"""
num1 = 7.5
num2 = 2.5

sum = num1 + num2

print(type(sum), sum)
"""
###6DATATYPECONV
#EXE1
"""
num1 = 7.5
Inum1 = int(num1)

print(Inum1)
"""

#EXE2
"""
num2 = 10

Fnum2 = float(num2)

print(Fnum2)
"""

#EXE3
"""
num1 = "7.5"
num2 = "10"

sum = float(num1) + int(num2)
print(sum, type(sum))
"""

###7STRINGFORMAT
#EXE1
"""
associateName = input("Write down your Name\n")

associateNumber = input("Write down your number of associate\n")

print(f"Dear {associateName}, your associate number is: {associateNumber}")
"""

#EXE2
"""
newPoints = int(input("The new points are: \n"))

totalPoints = 50 + newPoints

print(f"You have earn {newPoints} points! In total, you accumulate {totalPoints} points")
"""

#EXE3
"""
newPoints = int(input("The new points are: \n"))

oldPoints = int(input("How much are the old points: \n"))

totalPoints = newPoints + oldPoints

print(f"You have earn {newPoints} points! In total, you accumulate {totalPoints} points")
"""

###8MATHOPERATORS
#EXE1
"""
operation = 874 // 7

print(operation)
"""
#EXE2
"""
print(456%33)
"""

#EXE3
"""
print(783**0.5)
"""

###9ROUNDING
#E1
"""
print(round(10/3,2))
"""
#E2
"""
print(round(10.676767))
"""
#E3
"""
print(round(5**0.5,4))
"""
###10INDEXMETHOD
#E1
"""
word="computer"
print(word[4])
"""
#E2
"""
sentence = "In theory, theory and practice are the same. In practice, they are not."
word = "practice"

index = sentence.index(word)
print(index)
"""
#E3
"""
sentence = "In theory, theory and practice are the same. In practice, they are not."
word = "practice"

index = sentence.rindex(word)
print(index)
"""
###11SUBSTRING
#E1
"""
sentence = "Controlling complexity is the essence of programming"
fWord = sentence[:11]
print(fWord)
"""
#E2
"""
sentence = "Never trust a computer you can't throw out a window"
SWord = sentence[8::3]
print(SWord)
"""
#E3
"""
sentence = "It's great working with computers. They don't argue, they remember everything and they don't eat your food"
reverseSent = sentence[::-1]

print(reverseSent)
"""
###12STRINGMETHODS
#E1
"""
sentence="Especially in electronic communications, writing in all caps is equivalent to yelling."
upperSentence=sentence.upper()

print(upperSentence)
"""
#E2
"""
list = ["The","readability","account."]
string = " ".join(list)
print(string)
"""
#E3
"""
fSentence="If the implementation is hard to explain, "
sSentence="it might be a bad idea."
ans1 = fSentence.replace("hard","easy")
ans2 = sSentence.replace("bad","good")
print(ans1+ans2)
"""
###13STRINGPROPS
#E1
"""
string = "Repetition "
ans = string*15
print(ans)
"""
#E2
"""
word = "water"
poem = "Wet earth,

my travel memories

between the rains
"
ans = word not in poem
print(ans)
"""
#E3
"""
word="electroencephalographer"
length=len(word)
print(length)
"""
###14LISTS
#E1
"""
myList=["Aa",True,5,7.5,"2"]
"""
#E2
"""
transportMeans=["plane","car","boat","bicycle"]
transportMeans.append("motorcycle")
print(transportMeans)
"""
#E3
"""
fruits = ["apple", "banana", "mango", "cherry", "watermelon"]
removed=fruits.pop(2)
"""
###15DICTS
#E1
"""
myDict={"name":"Hedy",
        "surname":"Lamarr",
        "age":84,
        "occupation":"Inventor and much more..."}
"""
#E2
"""
my_dict = {"values_1":{"v1":3,"v2":6},"points":{"points1":9,"points2":[10,300,15]}}
ans = my_dict["points"]['points2'][1]
print(ans)
"""
#E3
"""
myDict={"name":"Hedy",
        "surname":"Lamarr",
        "age":84,
        "occupation":"Inventor and much more..."}

myDict["occupation"]="Screenwriter, producer..."
myDict["country"]="Austria and United States"

print(myDict)
"""
