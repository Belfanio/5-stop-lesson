arg = [152, 'asd']
def what (arg):
      print('Тип пргумента:{}'.format(type(arg)))
      
def what2(spis):
    cel = int()
    stok = int()
    bul = int()
    necel = int()
    net = int()
    itogo = int()
    dlinna = len(arg)
    for i in range(0, dlinna):
        if type(spis[i]) == int:
            cel = cel + 1
        elif type(spis[i]) == str:
            stok = stok + 1
        elif type(spis[i]) == bool:
            bul = bul + 1
        elif type(spis[i]) == float:
            necel = necel + 1
       
    if cel > 0:
        itogo = itogo + 1
    if stok > 0:
        itogo = itogo + 1
    if bul > 0:
        itogo = itogo + 1
    if net > 0:
        itogo = itogo + 1
    if necel > 0:
        itogo = itogo + 1                    
    print('Всего типов в списке: {}'.format(itogo))
if type(arg) == list:
    what2(arg)
else:
    what(arg)


