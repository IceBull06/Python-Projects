def am_to_can(word):

  word[-1]="u" #adds a u
  word.append('r') #adds a r
  return "".join(word)
x = ""
words=[]
vowels=["a","e","i","o","u","y"]
def is_am(word):
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
