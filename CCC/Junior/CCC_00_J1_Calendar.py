# https://dmoj.ca/problem/ccc00j1
start, length = input().split()

calendar = [
  ['Sun','Mon','Tue','Wed','Thr','Fri','Sat']
]

week = []
for _ in range(int(start)-1):
  week.append('')

for i in range(1,int(length)+1):
  if len(week) < 7:
    week.append(str(i))
  else:
    calendar.append(week)
    week = []
    week.append(str(i))
calendar.append(week)

for row in calendar:
  string = ""
  for element in row:
    
    if row.index(element) == len(row)-1:
      string += "{:>3}".format(element)
    else:
      string += "{:>3} ".format(element)
  print(string)
