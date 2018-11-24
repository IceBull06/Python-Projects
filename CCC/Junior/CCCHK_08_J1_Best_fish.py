c = int(input())
set_c = [input().split() for _ in range(c)]

n = int(input())
set_n = [input().split() for _ in range(n)]

max_c = 0
max_n = 0

for fish in set_c:
  tmp = int(fish[0]) * int(fish[1])
  if tmp > max_c:
    max_c = tmp

for fish in set_n:
  tmp = int(fish[0]) * int(fish[1])
  if tmp > max_n:
    max_n = tmp

if max_c > max_n:
  print('Casper')
elif max_n > max_c:
  print('Natalie')
else:
  print('Tie')
