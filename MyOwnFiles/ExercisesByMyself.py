import random
from random import choice

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
"""
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
"""

#E2

"""
age=int(input("Enter your current age:\n"))
ans=input("Do you have driver license?(Y/N):\n")
if ans == "Y":
    license = True
elif ans == "N":
    license = False
print("")

print(f"Age:{age}\nDriver license:{license}\n")
print("")

ageRestrict=(age >= 18)

if (ageRestrict == True) and (license == True):
    print(f"You can drive!!!")
elif ageRestrict == False:
    print(f"You can't drive yet. You must be 18 years old and have a license")
elif (ageRestrict == True) and (license == False):
    print(f"You can't drive. You need to have a license")
else:
    print(f"Any case detected\nAge:{age}\nState of driver license:{license}")
"""

#E3
"""
python=(input("Do you know Python(Y/N):\n"))
eng=input("Do you know english?(Y/N):\n")

if python == "Y":
    python = True
elif python == "N":
    python = False
else:
    python = None

if eng == "Y":
    eng = True
elif eng == "N":
    eng = False
else:
    eng = None
print("")

print(f"Python:{python}\nEnglish:{eng}\n")
print("")



if (python == True) and (eng == True):
    print(f"You meet the requirements to apply")
elif (python == False) and (eng == False):
    print(f"To apply, you need to know how to program in Python and have knowledge of English")
elif (python == True) and (eng == False):
    print(f"To apply, you need to have knowledge of English")
elif (python == False) and (eng == True):
    print(f"To apply, you need to know how to program in Python")
else:
    print(f"Any case detected\nPython knowledge:{python}\nEnglish knowledge:{eng}")
"""
###22LOOPFOR
#E1
"""
students_class = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás",
"Daniela"]

for i in students_class:
    print("Hello " + i)
"""
#E2
"""
list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
sum = 0
for i in list_numbers:
    sum += i
print(sum)
"""
#E3
"""
numbers_list = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

sumOdd = 0
sumEven = 0

for i in numbers_list:
    if i%2==0:
        sumEven += i
    else:
        sumOdd += i
print(f"The sum of odd numbers is:{sumOdd}\nThe sum of even numbers is:{sumEven}")
"""

###23LOOPWHILE
#E1
"""
num = 10

while num >= 0:
    print(num)
    num -=1
"""
#E2
"""
num = 50

while num >= 0:
    if num%5 == 0:
        print(num)
    num-=1
"""
#E3
"""
numbers_list = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for i in numbers_list:
    if i <0:
        print(f"For the number {i} the program will be interrupt")
        break
    else:
        continue
"""

###24RANGE
#E1

"""
myList = list(range(2500,2586))
print(myList)
"""

#E2
"""
myList= list(range(3,301,3))
print(myList)
"""
#E3
"""
sumCuadrados=0
for i in range(1,16):
    sumCuadrados+=i**2
print(sumCuadrados)
"""
###25ENUMERATE
#E1
"""
list_names = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta",
"Darío", "Emiliano", "Melisa"]

for i in range(0,len(list_names)):
    name = list_names[i]
    index = i
    print(f"{name} is found at index {index}")
"""
#E2
"""
indexList=[]
str="Python"
for i in range(0,len(str)):
    indexList.append((i,str[i]))
print(indexList)
"""
#E3
"""
names_list = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta",
"Darío", "Emiliano", "Melisa"]

for i in names_list:
    if i[0] == "M":
        print(i)
    else:
        continue
"""
###26ZIP
#E1
"""
capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]

zipTuple = tuple(zip(capitals,countries))

for i in zipTuple:
    capital=i[0]
    country=i[1]
    print(f"The capital of {country} is {capital}")
"""
#E2
"""
brands=['Samsung','Nothing','Acer','McDonalds']
products=['Tv','Phone','Laptop','Fast food']

zipTst = (zip(brands,products))

print(zipTst)
"""
#E3
"""
Spanish=["uno","dos","tres","cuatro","cinco"]
Portuguese=["um","dois","três","quatro","cinco"]
English=["one","two","three","four","five"]

numbLst=list(zip(Spanish,Portuguese,English))

print(numbLst)
"""
###27MIN&MAX
#E1
"""
list_numbers = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067,
353254, 123134, 55**12, 611**5]
maxValue = max(list_numbers)
print(maxValue)
"""
#E2
"""
list_numbers = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254,
123134, 552512, 611665]

maxVal=max(list_numbers)
minVal=min(list_numbers)

diff=maxVal-minVal
print(diff)
"""

#E3
"""
ages_dictionary = {"Carlos":55, "María":42, "Mabel":78, "José":44,
"Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2 ,"Dario":49}

agesLst=ages_dictionary.values()
namesLst=ages_dictionary.keys()

minAge=min(agesLst)
maxName=max(namesLst)
print(f"The minAge is: {minAge}\nThe last name is: {maxName}")
"""

###28RANDOM
#E1

"""
random=random.randint(1,10)     #2 LIMITS TO WORK
print(random)
"""
#E2
"""
random=random.random()      #NO LIMITS TO WORK
print(random)
"""
#E3
"""
names = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
random = random.choice(names)
print(random)
"""
###29LISTSCOPREHENSION
#E1
"""
values = [1, 2, 3, 4, 5, 6, 9.5]
valuesPow=[]
for i in values:
    valuesPow.append(i**2)
print(valuesPow)
"""
#E2
"""
values = [1, 2, 3, 4, 5, 6, 9.5]
valuesEven=[]
for i in values:
    if i%2==0:
        valuesEven.append(i)
    else:
        continue
print(valuesEven)
"""
#E3
"""
temperature_fahrenheit = [32, 212, 275]
degrees_celcius=[]
for F in temperature_fahrenheit:
    C = (F - 32) * (5/9)
    degrees_celcius.append(C)
print(degrees_celcius)
"""
###30METHODS&HELP
#E1
"""
txt=",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
tst= txt.lstrip(",:%_#")
print(tst)
"""
#E2
"""
fruits = ["mango", "banana", "cherry", "plum", "grapefruit"]
fruits.insert(3, "orange")      #index to be insert, stuff to insert
print(fruits)
"""
#E3
"""
smartphone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
tv_brands = {"Sony", "Philips", "Samsung", "LG"}

isolatedSets=smartphone_brands.isdisjoint(tv_brands)
print(isolatedSets)
#NOTE: TWO SETS ARE DISJOINT WHEN HAVE NULL ELEMENTS IN COMMON
"""

###31FUNCTIONS
#E1
"""
def greet():
    print("Hello World!")
"""
#E2
"""
def welcome(name:str):
    print(f"Welcome {name}")
"""
#E3
"""
def square(numb:int):
    print(f"The square of {numb} is {numb**2}")
"""
###32RETURN
#E1
"""
def power(base:int,exp:int):
    ans=base**exp
    return ans
"""
#E2
"""
def usdToEur(usd:int):
    eur= usd*0.90
    return eur
"""
#E3
"""
def reverseWord(word:str):
    reverse=word[::-1]
    up=reverse.upper()
    return up

#print(reverseWord("Python"))
"""
###33DYNAMICFUNCT
#E1
"""
def allPositives(values:list):
    ans=True
    for i in values:
        if i < 0:
            ans=False
            break
    return ans

#tst=[1,5,89,4,2,87,3,4,-1]
#tst1=[1,5,89,4,2,87,3,4,1]
#print(allPositives(tst1))
"""
#E2
"""
def sumMinors(numbList:list):
    sum=0
    for i in numbList:
        if i > 0 and i < 1000:
            sum+=i
    return sum

#numbers_list = [1, 50, 500, 5000, 750]

#print(sumMinors(numbers_list))
"""
#E3
"""
def evenCount(numbList:list):
    counter=0
    for i in numbList:
        if i % 2 == 0:
            counter+=1
        else:
            continue
    return counter
#numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,19, 20]
#print(evenCount(numbers_list))
"""
###34FUNCTIONSINTERACTIONS
#E1
"""
numbers = [1, 2, 3, 4, 5, 6 ]

def rollDice():
    fInt=choice(numbers)
    sInt=choice(numbers)
    return fInt,sInt
def evalMove(fInt:int,sInt:int):
    sum = fInt+sInt
    if sum <=6:
        print(f"The sum of your dice is {sum}.Sorry.")
    elif sum > 6 and sum < 10:
        print(f"The sum of your dice is {sum}. You have a good chance.")
    elif sum >=10:
        print(f"The sum of your dice is {sum}. It looks like a winning move.")
"""
#E2
"""
def reduceList(numbList:list):
    sortedList=numbList.sort()
    sortedList.pop()
    filterList=list(tuple(sortedList))
    return filterList
def average(filterList:list):
    sum=0
    numElements=len(filterList)
    for i in filterList:
        sum+=i
    ans=sum/numElements
    return ans
"""
#E3
"""
def tossCoin():
    res=random.choice(["Face","Cross"])
    return res
numbList = [1,2,3,4]
def testLuck(res:str,numbList:list):
    if res == "Face":
        numbList=[]
        print("The list will self-destruct")
        print(f"The numbList:{numbList}")
    elif res == "Cross":
        print("The list was saved")
        print(f"The numbList:{numbList}")
#print(testLuck(tossCoin(),numbList))
"""
###UNDEFINEDARGS
#E1
"""
def sumSquares(str):
    sum = 0
    print(f"The chain that was written is: {str}")
    for i in str:
        try:

            num = int(i)
            if int(i) / 1 == int(i):
                x = True
            else:
                x = None
            if x == True:
                sum += (num*num)

        except:
            continue
    if sum==0:
        ans=print(f"No se han encontrado numeros")
    else:
        ans=print(f"La suma de los cuadrados encontrados es de:{sum}")
    return ans
#print(sumSquares("1,2,3"))
"""

#E2
"""
def sumAbs(*args):
    sum=0

    for arg in args:
        if arg < 0:
            arg *= -1
            sum += arg
        else:
            sum+=arg
    return sum
"""
#E3
"""
def personNumb(name,*numbers):
    sum=0
    for numb in numbers:
        try:
            sum+=int(numb)
        except:
            continue
    print(f"{name}, the sum of your numbers is {sum}")
"""    
###36UNDEFINEDARG(KWARGS)
#E1

"""
#(*args)

def countParameters1(*args):
    sum = print(f"The numbers of parameters are: {len(args)}")
    return sum

#print(countParameters1(2,2,4,"asd",[4,5,8]))

#(**kwargs)

def countParameters2(**kwargs):
    sum=0
    for key,value in kwargs.items():
        sum+=1
    ans = print(f"The number of items insert in the parameters function is: {sum}")
    return ans

#print(countParameters2(key1=14,key2=15))
"""

#E2
#NOTE: The dictionaries methods can be use with **kwargs
"""
def listAttributes(**kwargs):
    lst=kwargs.values()
    ans = print(f"The list with all the values is: {lst}")
    return ans
#print(listAttributes(key1=14,key2=15))
"""

#E3
"""
def describePerson(name,**kwargs):
    print(f"Characteristics of: {name}\n")
    lst = kwargs.items()
    for each in lst:

        print(f"{each[0]} : {each[1]}")
    print("")

#describePerson("Mary", eye_color="blue", hair_color="blonde")
"""

###37OPEN&MANIPULATEFILES
#E1
"""
file = open("tstfile.txt", "w")
#w -> write in the file but overwritting
#a -> write in the end of the existing file
file.write("Test text in the file")
file.close()

f=open("tstfile.txt", "r")
print(f.read())
"""
#E2 & E3
"""
file = open("file2.txt","w")
for i in range(1,11):
    file.writelines(f"This is the {i} line\n")
file.close

file = open("file2.txt","r")
lines= file.readlines()

counter=0
for line in lines:
    counter+=1
    #print(f"This is the line{counter} and the content is: {line.strip()}")
    if counter == 1:
        print(f"The first line is: {line.strip()}")
    elif counter == 2:
        print(f"The second line is: {line.strip()}")
"""

###38CREATE&WRITEFILES
#E1
"""
file = open("myFile.txt","w")
file.write("New text")
file.close()

file = open("myFile.txt","r")
print(file.read())
"""
#E2
"""
file = open("myFile.txt","a")
file.write("New login")
file.close()

file=open("myFile.txt","r")
print(file.read())
"""
#E3
"""
record_last_session = ["Federico", "20/12/2021", "08:17:32 hs",
"No loading errors"]
file=open("log.txt","w")
for each in record_last_session:
    file.writelines(each+"\t")
file.close()

file=open("log.txt","r")
print(file.read())
"""

###39PATH
#E1

from pathlib import Path
"""
basePath=Path.home()

print(basePath)
"""
#E2
"""
path = Path("PythonCourse","Day 6","path_practices.py")
print(path)
"""
#E3
"""
home = Path.home()
fPath = Path(home,"PythonCourse","Day 6","path_practices.py")

print(fPath)
"""
###40FILES&FUNCTIONS
#E1
#NOTE: Not is necessary  to print before the return
"""
def openRead(file):
    fl=open(file,"r")
    ans=fl.read()
    return ans
"""
#E2
"""
def overWrite(file):
    fl=open(file,"w")
    return fl.write("Content deleted")
"""    

#E3
"""
def errorLog(file):
    fl=open(file,"a")
    ans=fl.write("an execution error has been logged")
    return ans
    fl.close()
"""    

###41CLASSES
#E1
"""
class Character:
    pass

ironman = Character()
"""

#E2
"""
class Dinosaur:
    pass

velociraptor=Dinosaur()
tyrannosaurus_rex=Dinosaur()
brachiosaurus=Dinosaur()
"""
#E3
"""
class StreamingPlatform:
    pass 

netflix = StreamingPlatform()
hbo_max = StreamingPlatform()
amazon_prime_video = StreamingPlatform()
"""

###42ATRIBUTES
#E1
"""
class House:
    def __init__(self,color,numberFloors):
        self.color = color
        self.numberFloors = numberFloors
    def printFunct(self):
        print(f"The color is: {self.color}\nThe number of floors: {self.numberFloors}")
tstHouse = House("White",4)
tstHouse.printFunct()
"""
#E2
"""
class Cube:
    def __init__(self,color):
        self.faces = 6
        self.color = color
    def __str__(self):
        return f"Faces: {self.faces}\nColor: {self.color}"
redCube = Cube('red')
print(redCube)      #USE the __str__ function to print
"""
#E3
"""
class Character:
    real=False
    def __init__(self,species,inventor,age) -> None:
        self.species = species
        self.inventor = inventor
        self.age = age
    def __str__(self) -> str:
        return f"species:{self.species}\ninventor:{self.inventor}\nage:{self.age}"
ironman = Character("Human",True,53)
print(ironman)
"""

###43METHODS
#E1
"""
class Dog:
    def bark(self):
        print("Wow!")
"""    
#E2
"""
class Inventor:
    def createInvent():
        return f"Eureka"

DaVinci = Inventor.createInvent()

#print(DaVinci)
"""
#E3
"""
class Alarm:
    def postoned(minutes):
        return f"The alarm has been postponed {minutes} minutes"

AlarmTst1 = Alarm.postoned(10)
print(AlarmTst1)
"""

###44METHODTYPES
#E1
"""
class Pet:

    @staticmethod
    def breathe():
        return f"Inhale..Exhale"
    
#print("Every pet needs to: ", Pet.breathe())
"""

#E2
"""
class Player:
    live = False
    @classmethod
    def revive(self):
        self.live = True
        return f"The actual state of the attribute live is: {Player.live}"

    def __str__(self):
        return f"State of live: {Player.live}"
playerTest = Player()
#print(playerTest)
#print(playerTest.revive())
"""
#E3
"""
class Character:
    def __init__(self, numbArrows):
        self.numbArrows = numbArrows

    def throwArrow(self):
        self.numbArrows -= 1
"""

###45INHERITANCE
#E1
"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    pass        #IF YOU DON´T NEED ADD ANYTHING
"""
#E2
"""
class Pet:
    def __init__(self,age, name, numbPaws) -> None:
        self.age = age
        self.name=name
        self.numbPaws=numbPaws

class Dog(Pet):
    def __init__(self,age,name,numbPaws):       #OTHER WAY TO INHERIT THE ATTRIBUTES BUT NO USING PASS
        super.__init__(age,name,numbPaws)
"""
#E3
"""
class Vehicle:
    def accelerate():
        pass
    def brake():
        pass

class Car(Vehicle):
    pass        #THE EASIEST WAY, WHEN NOTHING ELSE IS ADDED
"""

###46EXTENDEDINHERITANCE
#E1
"""
class Father:
    def __init__ (self):
        self.work = "Hospital"
        self.laught = "Father´s Laught like -Hahaha!-"
    
class Mother:
    def __init__(self):
        self.work = "Investigator"

class Daughter(Father,Mother):
    pass
"""
#E2
"""
class Vertebrate:
    vertebrate = True
class Fish:
    def layEggs(self):
        return f"layEggs"
    def swim(self):
        return f"swim"

class Reptile:
    poisonous = True
class Bird:
    beak = True
    def layEggs(self):
        return f"layEggs"
class Mammal:
    def walk(self):
        return f"CanWalk"
    def nurse(self):
        return f"CanNurse"

class Platypus(Vertebrate,Fish,Reptile,Bird,Mammal):
    pass
"""

#E3
"""
class Father():
    eyeColor = "brown"
    height = "high"
    voice = "average"
    sport = "soccer"
    def laught(self):
        return "Ha Ha Ha!"
    def hobby(self):
        return "Read books"
    def carrer(self):
        return "Engeneering"
    
class Son(Father):
    def hobby(self):
        return "I play videogames in my spare time"
"""

###47POLYMORPHISM
#E1
"""
word = "jellyfish"
list = ["constitution","medical","livingroom"]
tuple = (1,2,3,67)

for i in word:
    wordLen = len(word)

print(wordLen)

for i in list:
    listLen = len(list)

print(listLen)

for i in tuple:
    tupleLen = len(tuple)

print(tupleLen)
"""

#E2
"""
class Inventor():
    def innovate(self):
        print("Invent")

class Researcher():
    def innovate(self):
        print("Research")

class Scientist():
    def innovate(self):
        print("Science")

Tesla = Inventor()
MarieCurie= Researcher()
Einstein = Scientist()

characters = [Tesla,MarieCurie,Einstein]

for character in characters:
    character.innovate()

print(character)
"""

#E3
"""
class Defender():
    def defend(self):
        print("Mark and sweep")

class Goalkeeper():
    def defend(self):
        print("Watch out the goal")

class Midfielder():
    def defend(self):
        print("Back off and block attacks")

Ramos = Defender()
Ospina = Goalkeeper()
Kroos = Midfielder()

players = [Ramos,Ospina,Kroos]

def characterDef(player):
    player.defend()
"""

###48SPECIAL METHODS
#E1
"""
class Book:

    def __init__(self,title,author,numbPages):
        self.title = title
        self.author = author
        self.numbPages = numbPages
        
    def __str__(self):
        return f'"{self.title}", by {self.author}'
"""
#E2
"""
class Book:
    def __init__ (self,title,author,numbPages):
        self.title=title
        self.author=author
        self.numbPages = numbPages

    def __len__(self):
        return int(self.numbPages)
"""

#E3
"""
class Book:

    def __init__(self,title,author,numbPages):
        self.title=title
        self.author=author
        self.numbPages=numbPages

    def __del__(self):
        return f"Book deleted"
"""    


###49ERRORHANDING
#E1
"""
def sum(numb1,numb2):
    try:
        ans = numb1 + numb2
        return f"The result is: {ans}"
    except:
        return f"Unexpected error"
"""    

#E2
"""
def div(numb1,numb2):
    try:
        ans = numb1 / numb2
        ans = round(ans,2)
        return f"The result is: {ans}"
    
    except TypeError:
        return f"The arguments to be entered must be numbers"
    
    except ZeroDivisionError:
        return f"The second argument must not be zero"
"""    
#E3
"""
def openFile(file):
    try:
        f = open(file,"r")
        print(f"File open in lecture mode and the CONTENT is:\n{f.read()}")
        print("OPENING SUCCESSFULLY")
    except FileNotFoundError:
        return f"The file was not found"
    else:
        return f"Unknown error"
    finally:
        print("Finishing execution")
"""
#print(openFile("file2.txt"))
#print("")
#print(openFile("noExist.txt"))
#print("")
#print(openFile(2))
#print("")

###50GENERATORS
#E1
"""
def generator():
    ans = 0
    while True:
        ans+=1
        print(f"El numero reservado es: {ans}")
        yield ans
    
infgenerator = generator()
#print(infgenerator)
"""

#E2
"""
def multipliesOfSev():
    ans = 1
    while True:
        ans += 7
        yield ans

generator = multipliesOfSev()
"""

#E3
"""
#USUAL PROCEDURE
def loseLife():
    lifes = 3
    print(f"The last lifes was: {lifes}")
    while lifes != 0:
        lifes-=1
        yield f"You have {lifes} life left"
    else:
        return f"Game Over"
    

#YIELD PROCEDURE
def loseLifes():
    lifes= "You have 3 lifes"
    yield lifes

    lifes= "You have 2 lifes"
    yield lifes

    lifes= "You have 1 lifes"
    yield lifes

    lifes= "Game over"
    yield lifes
"""

###51COLLECTIONS
from collections import *

#E1
"""
list = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

cnt = Counter(list)     #Counter is a method from collections

print(cnt)
"""
#E2
"""
myDict = defaultdict(lambda:"Value not found")
myDict['age']=44

print(myDict)
"""
#E3
"""
citiesList = deque(["London", "Berlin", "Paris", "Madrid", "Rome", "Moscow"])
print(citiesList)
"""

###52 DATETIME
from datetime import *
#E1

###














