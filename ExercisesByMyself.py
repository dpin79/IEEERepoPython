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
###16TUPLES
#E1
"""
my_tuple = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
counter = my_tuple.count(2)
print(counter)
"""
#E2
"""
my_tuple = (1, 2, 3, 2, 3, 1, 3, 2)
myList = list(my_tuple)
print(myList)
"""
#E3
"""
my_tuple=(1,2,3,4)
a=my_tuple[0]
b=my_tuple[1]
c=my_tuple[2]
d=my_tuple[3]

list = [a,b,c,d]
print(list)
"""
###17SETS
#E1
"""
set1={1,2,'three','four'}
set2={'three',4,5}
set3= set1.union(set2)
print(set3)
"""
#E2
"""
raffle = {"Camila", "Margarita", "Axel", "George", "Michael", "Monica"}
randElement = raffle.pop()
print(randElement)
"""
#E3
"""
raffle = {"Camila", "Margarita", "Axel", "George", "Michael", "Monica"}
raffle.add("Damian")
print(raffle)
"""
###18BOOLEANS
#E1
"""
test=3>1
print(test)
"""
#E2
"""
res=17834/34 > 87*56
print(res)
"""
#E3
"""
sqrt = False
if (25**0.5==5):
    sqrt = True
print(sqrt)
"""
###19COMPARISONOPERATORS
#E1
"""
num1=36
num2=17
bool=(num1 >= num2)
print(bool)
"""
#E2
"""
num1=(25**0.5)
num2=(5)
bool=(num1==num2)
print(bool)
"""
#E3
"""
num1=64*3
num2=24*8
bool=(num1!=num2)
print(bool)
"""
###20BOOLEAN LOGICAL OPERATORS
#E1
"""
num1=36
num2=72/2
num3=48
bool=(num1>num2) and (num1<num3)
print(bool)
"""
#E2
"""
num1=36
num2=72/2
num3=48
bool=(num1>num2) or (num1<num3)
print(bool)
"""
#E3
"""
word1="success"
word2="technology"
sentence="When something is important enough, you do it even if the odds are not with you"

a = sentence.__contains__(word1)
b = sentence.__contains__(word2)

res = bool(~(a or b))

print(res)
"""
###21FLOWCONTROL
#E1

num1=input("Enter the number 1:\n")
num2=input("Enter the number 2:\n")

print(f"The written numbers was {num1} as the \nfirst one and {num2} as the second one.\n")
print("")
statement1=(num1>num2)
statement2=(num2>num1)
statement3=(num1==num2)

if statement1 == True:
    print(f"The number 1: {num1} is greater than the number 2: {num2}")
elif statement2 == True:
    print(f"The number 2: {num2} is greater than the number 1: {num1}")
elif statement3 == True:
    print(f"The number 1: {num1} is EQUAL than the number 2: {num2}")
else:
    print(f"Any case detected\nNumber 1:{num1}\nNumber 2:{num2}")
    