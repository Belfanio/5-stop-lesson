spis=[16, -17, 2, 78.7, False, False, 555, 12, 23, 42, 'DD']
dlinna = len(spis)

def sortirovka(spis):
    spis1 = [spis[i] for i in range(0, dlinna) if type(spis[i]) == int or type(spis[i]) == float]
    list.sort(spis1)
    print('Сортированный список: {}'.format(spis1))

sortirovka(spis)