# https://dmoj.ca/problem/mockccc15j1
# a is the phone number of the user. 
a=input().split()
if int(a[0])<1000:
  if a[0]=='416':
    print("valuable")
  elif a[0]=='647' or a[0]=='437':
    print("valueless")
  else:
    print("invalid")
else:
  print("invalid")
