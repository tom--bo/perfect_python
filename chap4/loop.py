for index, name in enumerate(["apple", "orange", "lemon"]):
    print(index, name)
    if index == 2:
        break
else: #途中でbreakした場合は実行されない
    print("done")



