base = 2

i = 1

sum = 0

while i <= 100:
  j = 0
  while base ** j < i:
    j += 1
  if base ** j == i:
    sum += i
  i += 1

print(sum)
