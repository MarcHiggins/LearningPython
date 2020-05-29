##Dictonaries

#When given a string, count the occurances of each word

#import the ability to Count occurance

from collections import Counter


#test with given string
data = str("We tried list and we tried dicts also we tried Zen")

def wordCounter(data):
    l = data.split(' ')
    c = Counter(l)
    for key, value in c.items():
        print (key, value)    


wordCounter(data)



RosaInput = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

wordCounter(RosaInput)