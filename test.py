#! /usr/bin/python

def calcMax(num, min_index, max_index, max_num, array):
  half_index = int((min_index + max_index) / 2)
  total = num + array[half_index]
  if total == max_num:
    return total
  elif min_index == half_index:
    if max_num < total:
      return 0
    else:
      return total
  elif total < max_num:
    return calcMax(num, half_index, max_index, max_num, array)
  else:
    return calcMax(num, min_index, half_index, max_num, array)

init = raw_input()
init = init.split(' ')

p = []
for i in range(int(init[0])):
  p.append(int(raw_input()))
p.sort()

m = []
for i in range(int(init[1])):
  m.append(int(raw_input()))

for max_num in m:
  temp = 0
  for i in range(len(p) - 1):
    if max_num < p[i] + p[i + 1] :
      break
    result = calcMax(p[i], i + 1, len(p) - 1, max_num, p)
    if temp < result:
      temp = result
      if temp == max_num:
        break
  print temp

