howManySentances = input('Paste your text: ')
sentanceCount = 0
wordCount = 1
for x in howManySentances:
  if x == '.':
    sentanceCount += 1
  else:
    pass
for x in howManySentances:
  if x == ' ':
    wordCount += 1
  else:
    pass
strLength = str(len(howManySentances))
print ("Sentances: " + str(sentanceCount))
print ("Words: " + str(wordCount))
print ("Charecters: " + strLength)
