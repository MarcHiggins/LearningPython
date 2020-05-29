## Rosalind problem - conditions and loops
## Aim: When given two positive intergers (a,b) return the 
## sum of all odd integers between and including a and b 


#write a function for this
def sumodds(x,y):
    odds = [i for i in range (x, (y+1)) if i % 2 == 1] ##create a list of all odd numbers between the two inputs
    return sum(odds) #sum what is stored in this list

sumodds(100,200) #test with the example inputs

sumodds(4860,9368) #actual probelms as provided by Rosalind