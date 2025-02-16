
A = {'a', 'b', 'c'}
B = {'x', 'y', 'z'}
C = {'1', '2', '3'}


def concatenate(s1, s2):
    return s1 + s2


def invers(s):
    return s[::-1]


def substituie(s, a, b):
    return s.replace(a, b)

def lungime(s):
    return len(s)

s1 = "abc"
s2 = "xyz"

print("Concatenare:", concatenate(s1, s2))  # abcxyz
print("Inversare:", invers(s1))  # cba
print("Substituire:", substituie(s1, 'a', 'x'))  # xbc
print("Lungime:", lungime(s1))  # 3

#2
def concat(s1, s2):
    return s1 + s2

def repeat(s, n):
    return s * n

def reverse(s):
    return s[::-1]

def extract(s, i, j):
    return s[i:j+1]

def replace(s, sub, new_sub):
    return s.replace(sub, new_sub, 1)

# Example usage
word = "A123"
print("Original word:", word)

# Concatenation example
print("Concatenation with 'B456':", concat(word, "B456"))

# Repetition example
print("Repetition (2 times):", repeat(word, 2))

# Reverse example
print("Reversed:", reverse(word))

# Extraction example (characters from position 1 to 3)
print("Extracted (1-3):", extract(word, 1, 3))

# Replacement example (replace '123' with '789')
print("Replacement ('123' -> '789'):", replace(word, "123", "789"))

#3
from itertools import product

# Definirea alfabetului
E = ['0', '1', '2']

# Funcție pentru a verifica dacă un șir este palindrom
def este_palindrom(sir):
    return sir == sir[::-1]

# Generarea și afișarea palindroamelor pentru lungimi de 1 până la 5
for lungime in range(1, 6):
    print(f"Palindroame de lungime {lungime}:")
    for combinatie in product(E, repeat=lungime):
        sir = ''.join(combinatie)
        if este_palindrom(sir):
            print(sir)
