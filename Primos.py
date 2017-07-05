primo = input('valor: ')
def funcao(primo):
    for i in range(2,primo+1):
        if i != primo:
            i = primo % i
            if i == 0:
                print 'Nao e primo'
                break
        else:
            print 'E primo'
            break


funcao(primo)

