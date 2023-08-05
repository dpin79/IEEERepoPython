"""Write a program that stores the subjects 
of a course (e.g. Mathematics, Physics, 
Chemistry, History and Language) in a list
 and displays it on the screen."""

def subjects():
    ans= []
    loop = None
    qs = input("Do you want add any subject?(Y/N):\n")
    if qs == "Y":
        loop = True
        while loop == True:
            sub = str((input("Write subject-NONE to stop write subjects-:\n")))
            if sub == "NONE":
                loop = False
            else:
                grade = str(input("Write the grade in the signed subject:\n"))
                tuple = f"The subject is: {sub} and the grade is: {grade}\n"
                ans.append(tuple)
    print("")
    return f"The subjects list is: {ans}"

print(subjects())

"""
Write a program that stores the subjects of a course (e.g. Mathematics, 
Physics, Chemistry, History and Language) in a list, asks the user the 
grade he/she got in each subject, and then displays them on the screen 
with the message In <subject> you got <grade> where <subject> is each 
of the subjects in the list and <grade> is each of the corresponding 
grades entered by the user.
"""
def subs():
    ans = []
    loop = input("Write down any subject?(Y/N): ")      #INCOMPLETE
    print("")
    sub = str(input("Write a subject"))
    grade = str(input("Write a grade"))
    tuple = (sub,grade)

    ans.append(tuple)

    
    
    
