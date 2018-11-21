# https://dmoj.ca/problem/mockccc15j1
a=input().split()
if int(a[0])<1000:
  if a[0]=='416' or a[0]=='437':
    print("Valuable")
  else:
    print("Invalid")
else:
  print("Invalid")
