import os
import re
from collections import Counter

commonwords = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "I", "it", "for", "not", "on", "with", "he", "as", "you", "do", "at"]

print("I'd love to help you find the most common words on any website!")
website = input("Please enter website here \n:")

result = os.popen("wget -O test.html {} && curl -H 'Accept: text/plain' -T test.html http://localhost:9998/tika".format(website)).read()
rawwords = result

wordList = re.sub("[^\w]", " ", rawwords).split()

yn = input("would you like to exclude some of the most common words? Y or N\n:")
if yn == "Y":
    exclusions = int(input("how many, up to 20, words would you like to exclude? \n:"))
    selectedCommonwords = [commonwords[0:(1-exclusions)]]
    editedWordList = [x for x in wordList if not in selectedCommonwords]
    howmany = int(input("How many top words would you like? \:"))
    print(Counter(editedWordList).most_common(howmany))

else:
    howmany = int(input("How many top words would you like? \:"))
    print(Counter(wordList).most_common(howmany))
