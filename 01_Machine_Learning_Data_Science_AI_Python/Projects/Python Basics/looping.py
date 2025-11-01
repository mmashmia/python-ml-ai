print("Loop 1:")
for x in range(10):
    print(x)

print("\nLoop 2:")
for x in range(10):
    if x is 1:
        continue
    if x > 5:
        break
    print(x)

print("\nLoop 3:")
x = 0
while x < 10:
    print(x)
    x += 1