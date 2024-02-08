import sys
import math


def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def shred(filename):
    #Using a dictionary here. You may change this to any data structure of
    #your choice such as lists (X=[]) etc. for the assignment
    X=dict()
    for i in range(ord('A'), ord('Z') + 1):
        character = chr(i)
        X[character] = 0
    #Sorting, and Upper Case
    with open (filename,encoding='utf-8') as f:
        for line in f:
            AtoZ = line.upper()
            for character in AtoZ:
                if character >= 'A' and character <= 'Z':
                    X[character] += 1 
    #Output
    print("Q1")
    for letters in sorted(X.keys()):
        print(letters + " " + str(X[letters]))
    
    return X

def logProb (e,s):
    #list
    lettercounts = []
    for ascii_code in range(ord('A'), ord('Z') + 1):
        lettercounts.append(letterdict[chr(ascii_code)])
    #prob
    LogE1 = lettercounts[0] * math.log(e[0])
    LogE2 = lettercounts[0] * math.log(s[0])
    #print
    print('Q2')
    print("{:.4f}".format(LogE1))
    print("{:.4f}".format(LogE2))

def langProb (e,s):
    #list
    lettercounts = []
    for ascii_code in range(ord('A'), ord('Z') + 1):
        lettercounts.append(letterdict[chr(ascii_code)])
    
    #PriorProbs
    probEngl = math.log(0.6)
    probSpan = math.log(0.4)

    #F(English) & F(Spanish)
    Fenglish = probEngl + sum(lettercounts[i]*math.log(e[i]) for i in range(26))
    Fspanish = probSpan + sum(lettercounts[i]*math.log(s[i]) for i in range(26))

    #print
    print('Q3')
    print("{:.4f}".format(Fenglish))
    print("{:.4f}".format(Fspanish))

    #Normalizing
    if Fspanish - Fenglish >= 100:
        EnglishX = 0
    elif Fspanish - Fenglish <= -100:
        EnglishX = 1
    else:
        EnglishX = 1/(1+math.exp(Fspanish - Fenglish))

    #print
    print('Q4')
    print("{:.4f}".format(EnglishX))
        
#Main
if __name__ == '__main__':
    e,s = get_parameter_vectors()
    letterdict = shred('letter.txt') #bring to testing file and use testing filename here, letter.txt is for cloud testing.
    logProb(e,s)
    langProb(e,s)
