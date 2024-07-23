def secondSlotCalk():

    firstSlot = int(input("Введите число из первого слота\n"))
    secondSlot = {}
    strSecSlot = ""

    for i in range(1, firstSlot):
        for j in range(1, firstSlot):
            if firstSlot == (i + j) and j not in secondSlot or firstSlot % (i + j) == 0 and j not in secondSlot:
                secondSlot[i] = j
                strSecSlot += str(i) + str(j)

    return strSecSlot

result = secondSlotCalk()
print("Вот шифр!")
print(result)