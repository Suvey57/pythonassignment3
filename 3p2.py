def insertionSort(arr):
   for i in range(1, len(arr)):
      key = arr[i]
      j = i-1
      while j >=0 and key < arr[j] :
         arr[j+1] = arr[j]
         j -= 1
      arr[j+1] = key

arr= []
b=int(input("enter a length of list::"))
for i in range(b):
    c=int(input("enter the elements of list::"))
    arr.append(c)
print(arr)
insertionSort(arr)
print(arr)
