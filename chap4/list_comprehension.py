print([x**2 for x in range(1,11)])

print([x**2 for x in range(1,11) if x%2 == 0])

vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

res = (x**2 for x in range(1,11))

print(next(res))
print("a")
print(next(res))
print("b")
print(next(res))
print("c")

