def mergeTwoLists(list1, list2):
    result = []
    while len(list1) != 0 and  len(list2) != 0:
        if list1[0] <= list2[0]:
            result.append(list1[0])
            list1 = list1[1:]
        else:
            result.append(list2[0])
            list2 = list2[1:]

    return result + list1 + list2


