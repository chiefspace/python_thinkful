swapCounter = 1
listItemCounter = 0
nextListItemCounter = 1
list1 = [2, 7, 3, 9, 2]
numberOfListItems=len(list1) - 1
print numberOfListItems
print list1
print "#################"

while swapCounter != 0: 
    swapCounter = 0
    listItemCounter = 0
    nextListItemCounter = 1
    while listItemCounter < numberOfListItems: 
                if list1[listItemCounter] <= list1[nextListItemCounter]: 
                        listItemCounter += 1
                        nextListItemCounter += 1
                        print list1
                        print swapCounter
                else:
                        tempSwap = list1[listItemCounter]
                        list1[listItemCounter] = list1[nextListItemCounter]
                        list1[nextListItemCounter] = tempSwap
                        swapCounter += 1
                        listItemCounter += 1
                        nextListItemCounter += 1
                        print list1
                        print swapCounter

print "#################"
print list1
print swapCounter