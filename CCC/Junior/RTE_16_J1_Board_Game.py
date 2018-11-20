x = ''.join(input().split())

maximum = 0
tmp = 0

for i in range(len(x)):
  if x[i] != 'L':
    tmp = 0
  else :
    if i > 0 and i < len(x)-1:
      tmp += 1
    elif i == 0:
      tmp += 1
    elif i == len(x)-1:
      tmp += 1
  
  if tmp > maximum:
    maximum = tmp

print(x.count('L'), maximum)
