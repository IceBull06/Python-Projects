def am_to_can(word):
  word=list(word)
  word[-1]="u"
  word.append('r')
  return "".join(word)
x = ""
words=[]
vowels=["a","e","i","o","u","y"]
def is_am(word):
  word=list(word)
  if word[-1]=="r" and word[-2]=="o" and word[-3] not in vowels:
    return True
  else:
    return False
while x != "quit!":
  x = input()
  words.append(x)
words.pop()
for i in range(len(words)):
  if len(words[i])>4 and is_am(words[i]):
    print(am_to_can(words[i]))
  else:
    print(words[i])
