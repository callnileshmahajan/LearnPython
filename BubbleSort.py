def swapnumbers(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp
    return num1, num2


def bubblesort(mylist):
    for i in range(0, len(mylist) - 1):
        for j in range(0, len(mylist) - i - 1):
            if mylist[j] > mylist[j + 1]:
                mylist[j], mylist[j + 1] = swapnumbers(mylist[j], mylist[j + 1])
    return mylist


list = [7, 2, 1, 6, 8, 5, 3, 4]
newlist = bubblesort(list)
print(newlist)
