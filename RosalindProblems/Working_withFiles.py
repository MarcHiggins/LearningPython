## Learning how to read files
## and iterate through lines


#Print the even numbered lines


f = open('rosalind_ini5.txt', 'r')
i = 1


for line in f.readlines():
    if i % 2 == 0:
        print(line)
    i = i+1
    
