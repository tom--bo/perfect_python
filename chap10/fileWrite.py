f = open('test.txt', encoding='utf-8')
# print(f.read(), end="")
cnt = 1
for line in f:
    print(cnt)
    print(line, end="")
    cnt += 1
f.close()

