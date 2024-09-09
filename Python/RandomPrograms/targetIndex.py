def search_element(lst, target):
    for index in range(len(lst)):
        if target == lst[index]:
            return index
    return -1


target = 4
lists = [1, 3, 4, 5, 6, 7]
result = search_element(lists, target)
print(result)
