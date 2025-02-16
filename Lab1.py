
from itertools import product

S1 = "abc"
S2 = "xyz"

s2 = "a b c d e f g h i j k"
s1 ="1 2 3 4 5 6 7 8 9"
#1
def concatenate(S1, S2):
    return S1 + S2

res = concatenate(S1, S2)
print(res)  


def invers(S1):
    return S1[::-1] 

inv = invers(S1)
print(inv)  

def substitute(S1):
    return S1.replace("a", "b")

subs = substitute(S1) 
print(subs)  

def length(S1):
    return len(S1)

lungime = length(S1)

print(lungime)

#2

def concat(s2, s1):
    return s2+s1

conc = concat(s1,s2)
print(conc)

for _ in range(5):  
    s2 += "  "   

print(s2)  

def inverse(s2):
    return s2[::-1] 

inve = invers(s2)
print(inve)

def extract(s, i, j):
    return s[i:j+1]  


substring = extract(s2, 4, 9) 
print(substring)

s = "ana are mere"

def replace(s, sub):
    return s.replace(sub, "Filip")

newSub = replace(s, "ana")
print(newSub) 

#3



E = "1 2 3"  
digits = E.split()  

def is_palindrome(s):
    return s == s[::-1]

palindromes = set()


for length in range(1, 6):  
    for comb in product(digits, repeat=length):  
        num = "".join(comb)  
        if is_palindrome(num):
            palindromes.add(num)


print( sorted(palindromes, key=int))


#4
def genereaza(max_length=5):

    results = []
    
    for i in range(max_length + 1): 

        for j in range(max_length + 1):
            results.append('a'*i+'b'*j)
    
    return results


strings = genereaza(4)
print(strings)
