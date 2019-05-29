arg = 152
    
      
def chek_of_type(spis):
    if type(arg) == list:
        integer = int()
        string = int()
        boolean = int()
        float1 = int()
        total = int()
        long = len(arg)
        for i in range(0, long):
            if type(spis[i]) == int:
                integer = integer + 1
            elif type(spis[i]) == str:
                string = string + 1
            elif type(spis[i]) == bool:
                boolean = boolean + 1
            elif type(spis[i]) == float:
                float1 = float1 + 1
       
        if integer > 0:
            total = total + 1
        if string > 0:
            total = total + 1
        if boolean > 0:
            total = total + 1
        if float1 > 0:
            total = total + 1                        
        print('Всего типов в списке: {}'.format(total))
    else:
        print('Тип пргумента:{}'.format(type(arg)))

chek_of_type(arg)


