def zhenghe(a, b):
    c = []
    i=0
    j=0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    if i == len(a):
        for j in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c


def mergesort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)/2
    left = mergesort(lists[:middle])
    right = mergesort(lists[middle:])
    return zhenghe(left, right)

t=[1,2,3,6,3,7,2,5,2]
print mergesort(t)