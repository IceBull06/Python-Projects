x=int(input()) #get inputs
xs=[] #make list
ys=[] #make another list
for i in range(x):
  x,y=map(int,input().split()) #get more inputs
  xs.append(x) #append x
  ys.append(y) #append y
xs.sort() #sort list
ys.sort() #sort other list
l=xs[-1]-xs[0] #get length
w=ys[-1]-ys[0] #get width
print((l+w)*2) #print
