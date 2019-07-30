v=['a','e','i','o','u','A','E','I','O','U']
vowel=input()
if vowel.isalpha():
    if vowel in v:
      print("Vowel")
    else:
      print("Consonant")
else:
    print("invalid")
