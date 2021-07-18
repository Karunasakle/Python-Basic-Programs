def isVowel(ch):
    switcher={
        'a': "Vowel",
        'e': "Vowel",
        'i': "Vowel",
        'o': "Vowel",
        'u': "Vowel",
        'A': "Vowel",
        'E': "Vowel",
        'I': "Vowel",
        'O': "Vowel",
        'U': "Vowel"
    }
    return switcher.get(ch,"Consonant")
ch=input("Enter any character to cheak vowel or consonant: ")
print(ch,'is a '+isVowel(ch))   
