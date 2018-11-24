# https://dmoj.ca/problem/ccc01j1
h = int(input())

data = []

top_left = [
  ['*' if x < h - i * 2 else ' ' for x in range(h)]
  for i in range(h//2, 0, -1)
]
top_right = [reversed(row) for row in top_left]

# join together left and right
for i in range(len(top_left)):
  tmp = []
  for symbol in top_left[i]:
    tmp.append(symbol)
    
  # append bottom
  for symbol in top_right[i]:
    tmp.append(symbol)

  data.append(tmp)
  
# flip top to bottom
bottom = reversed(data)

# add middle
data.append(['*' for _ in range(2*h)])

# append bottom
for row in bottom:
  data.append(row)

for row in data:
  print(''.join(row))
