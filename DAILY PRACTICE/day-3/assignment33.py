str1=input("enter your string = ")
def vowelcount():
    str2=str1.lower()
    str3=str2.replace(" ","")
    length=len(str3)
    vowelcount=0
    for i in range(length):
        if(str3[i]=='o'or str3[i]=='i'or str3[i]=='e'or str3[i]=='u'or str3[i]=='a'):
            vowelcount+=1
    print("vowel=",vowelcount)
    return vowelcount

def consonantcount():
    str2=str1.lower()
    str3=str2.replace(" ","")
    length=len(str3)
    consonantcount=0
    for i in range(length):
        if(str3[i]!='o'and str3[i]!='i'and str3[i]!='e'and str3[i]!='u'and str3[i]!='a'):
            consonantcount+=1
    print("consonant=",consonantcount)
    return consonantcount

def ratio():

    ratio=vowelcount()/consonantcount()
    print("ratio=",ratio)

ratio() 