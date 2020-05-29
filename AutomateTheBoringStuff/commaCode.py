##Aim is to print a list with all items separated with a comma
## and a space, with and inserted before the last item

##Test one with a simple, user defined list

spam = ['apples', 'bananas', 'tofu', 'cats']

print(spam)

def andlist(x):
    x.insert(-1, 'and')
    print(*x, sep = ", ")
    
andlist(spam)
    
print(*spam)
    
## Test two: generate a long list and call the function on this

import random
randomDNA = []
dna = ["A", "T", "G", "C"]
for i in range (0,100):
    randomDNA +=random.choice(dna)
print(randomDNA)

andlist(randomDNA)