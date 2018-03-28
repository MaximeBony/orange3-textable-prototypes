import re
import os
import LTTL
from LTTL.Segmenter import intersect, tokenize, Segment

myList = ["Bonjour", "Aurevoir", "Merci", "Non", "Oui"]
myRamblings = ("Non Bonjour petit bonhomme frustré, je suis la Fée Qui Dit Non"
    ", et j'aime la tartiflette aux fleurs et je te dis aurevoir!")

myReString = "|".join(myList)
myReString = "(%s)" % myReString
print(myReString)

myRegex = re.compile(myReString)

result = myRegex.match(myRamblings)
results

print(results)
