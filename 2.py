list1=[16, -17, 2, 78.7, False, False, 555, 12, 23, 42, 'DD']
long1 = len(list1)

def sortirovka(spis):
    list2 = [list1[i] for i in range(0, long1) if type(list1[i]) == int or type(list1[i]) == float]
    long2 = len(list2)
    for i in range(long2-1):
        for j in range(long2-i-1):
            if list2[j] > list2[j+1]:
                list2[j], list2[j+1] = list2[j+1], list2[j]
    print('Сортированный список: {}'.format(list2))


sortirovka(list1)