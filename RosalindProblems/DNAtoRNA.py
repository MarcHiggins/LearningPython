# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 14:17:12 2020

@author: marcg
"""
#Upload test DNA sequence
DNA = "GATGGAACTTGACTACGTAAATT"

#Convert to RNA with .replace() function
#Test it works
RNA = DNA.replace("T","U")
print(RNA)

#write a function
def DNAtoRNA(x):
    y = x.replace("T","U")
    print (y)
    
DNAtoRNA(DNA)

#Use Rosalind DNA sequence
RosaDNA = "CGAATACACGACAGGAATAGACCCGTTGGGACGCTCTGGTCTATCAGTCATAAATTCCACCCGTGCTAATCCCAAATGCGACCACCAACCCCATTATAGTTATTAAGGCAGTTTCGGAAGGAGATTATCATGGAGGCCCCTCACAGGCAGGTCAATGATGATCGGGTTCCCGTTACAATTTGCTTTGAAATCTCGCTGCCTGAAGTCGAAAGGAGTGGACGCCCCTACGGTCTCATTGTTTGTCTGGCAATAGATCCTCCAGGAGCAAGAGTAGTTTGCATGAGGACTGGTCCTCAAACGTTCTACACGGACGACAAGCACCTACAAGGTCTAGGGCGGTGAATGACTTTAGCCAATTTAATTCAGGGTCGCTTCAATGCAGATCAACTTCCGCCAGAGACGAGCCACACCACCCGTTCAAGTTAATATCCACTATTTTAAAAAAGGATTCACAAAGCGTGAAGCACGGACGGCACGGATAGGATGTTCACCCTATCTTGGTTCTAAAGAGCGGGTAGCGGTGGCATACCGCACCACCCCGTACGTCGCGAAACCGTGCTTGCTACCTCATTAAGGCACATCGCAGGTAAATGAGTAAGGATTTGGAGTTGATTGACAATTTTCGCTTTAGGTGCCTGAGGTATCAAACTTACCGTACGACTGGAGCCGCTGAGGTTTTATGGCAGCGAAATGGAAGCCTCCTGTCACCATTATCCTCTAGTTTTCGTACCTGGGTAAGCCGTACCATGCTTAAAGCACCGGAATGAACCAGCAAAGGCATTACTACATGGAGAAGGACATCGCCACCGCAGCGGTTAAGCGTCAATTGACGATAAGGGTAGGATATACCTAAGCAGTGTCGATTGATACACCTACTAAGAGGGCGACTGACTCATATGGTTCCTCAGAGCGCTTATTGCCATGTTTAGCCTGACAAACGATCCTATCCAGGGTGGTTCAGA"

DNAtoRNA(RosaDNA)