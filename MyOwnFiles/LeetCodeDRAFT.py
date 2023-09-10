from collections import Counter
"""
t = 'abcd'
s = 'abcde'

T = Counter(t)
S = Counter(s)

less = list(Counter(t)-Counter(s))[0]
"""
#print(T, S)



#----------------
"""
int
str
double
lst
dict
"a" == 'a'
chr('a') == chr("a")
"""

def nextGreatestLetter(letters, target) -> str:
        ans = chr(0)
        #print(f"Este es el chr NULL ---{ans}---")
        for i in letters:
            if (i > target) and (target > ans):
                ans = i
            else:
                continue
        if ans == chr(0):
            ans = letters[0]
        return ans

letters = ["x","x","y","y"]
target = "z"
#print(nextGreatestLetter(letters,target))

#----------------
"""
0
1
1

2++++

1
1
2

4++++

1
2
3

6++++
"""

#----------------

import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #AJUSTE DE NUMEROS A MOVIMIENTOS POSIBLES
        #X = m -1    #DIMENSION REAL
        #Y = n -1    #DIMENSION REAL
        A = (m+n)-2     #NUMERO NUMERADOR DE COMB

        if m <= n:
            B = m -1 
        else:
            B = n -1 
        
        C = A - B
        fA = math.factorial(A)
        fB = math.factorial(B)
        fC = math.factorial(C)
    
        ans = ((fA)//(fB*fC))
        return ans




def moveZeroes(nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        leng = len(nums)
        if leng >= 2:
                   
            while i < leng:
                if nums[i] == 0:
                    nums.pop(i)
                    nums.append(0)
                    leng -=1
                else:
                    i +=1
        else:
             pass
        #print(nums)
        
nums = [0,1,0,3,12]
lst1 = [1,2,3]
lst2 = ([0]*3)
#print(lst1 += lst2)
#print(moveZeroes(nums))





def findRightInterval(intervals):
        if len(intervals) > 1 and #########CONTINUE HERE....
        elif len(intervals) >1:
             #
        else:
             ans = [-1]