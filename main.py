howManySentances = input('Paste your text: ')
count = 0
for x in howManySentances:
  if x == '.':
    count += 1
  else:
    pass
print (count)