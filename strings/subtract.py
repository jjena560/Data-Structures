def getAvailableLetters(lettersGuessed):
    s="abcdefghijklmnopqrstuvwxyz"
    k=list(s)
    str1=lettersGuessed
    str2=list(str1.lower().replace(" ", ""))
    for i in range(len(str2)):
        if str2[i] in k:
            k.remove(str2[i])
    return k

print(getAvailableLetters('Jyotiprakash Jena')) ##this will remove all the characters tghat are in my name and return the rest of all the elements