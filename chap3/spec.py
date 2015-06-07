ba1 = bytearray()
ba1.append(115)
ba1.append(112)
ba1.append(97)
ba1.append(109)
print(ba1)

ba4 = bytearray(b'egg')
print(ba4)
print(ba4[1])

x = [1,2,3.0,"a", "b", 'c']
for i in x:
    print(type(i))
print(x[-1])
print(x[-6])


l = [i for i in range(10) if i % 2 == 0]
print(l)
