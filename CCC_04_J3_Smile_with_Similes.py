adj_times = int(input())
noun_times = int(input())
adjs = [input() for i in range(adj_times)]
nouns = [input() for i in range(noun_times)]
output = []
for i in range(adj_times):
  for j in range(noun_times):
    output.append(adjs[i] + " as " + nouns[j])
for i in output:
  print(i)
