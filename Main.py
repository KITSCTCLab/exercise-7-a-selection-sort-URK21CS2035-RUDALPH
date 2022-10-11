from typing import List

def selectionSort(array, size) -> List[int]:
  for j in range(size):
    min = j
    for i in range(j + 1,size):
      if array[i]<array[min]:
        min = i
    (array[j],array[min])=array[min],array[j]
   return array

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))

