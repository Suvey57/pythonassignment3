a = []
b=int(input("enter a length of list::"))
for i in range(b):
    c=int(input("enter the elements of list::"))
    a.append(c)
print(a)

for j in range(len(a)):
    swapped = False
    i = 0
    while i<len(a)-1:
        if a[i]>a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
            swapped = True
        i = i+1
    if swapped == False:
        break
print (a)