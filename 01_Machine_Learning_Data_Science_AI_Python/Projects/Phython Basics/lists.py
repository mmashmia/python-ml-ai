x = [1, 2, 3, 4, 5, 6]
print(len(x))

print(x[:3])

print(x[3:])

print(x[-2:])

x.extend([7,8])
print(x)

x.append(9)
print(x)

y = [10, 11, 12]
listOfLists = [x, y]
print(listOfLists)

print(y[1])

z = [3, 2, 1]
z.sort()
print(z)

z.sort(reverse=True)
print(z)
