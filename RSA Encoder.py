import itertools
#coding: utf-8


def print_factors(num):
    pass


def valorpq():
    print ('-----------RSA Coder---------------')
    q = int(input('Digite um valor primo para q: '))
    if q < 0:
        print ('invalido')
        return valorpq()
    for i in range(2, q + 1):
        if i != q:
            i = q % i
        if i == 0:
            print ('nao e primo')
            return valorpq()

    p = int(input('Digite um valor primo para p: '))
    if p < 0:
        print ('invalido')
        return valorpq()

    for i in range(2, p + 1):
        if i != p:
            i = p % i
        if i == 0:
            print ('nao e primo')
            return valorpq()

    n = q*p

    print ('Valor de N = ', n)

    Tgn = (p - 1) * (q - 1)
    print ('Tgn: = ', Tgn)

    print('Os divisores comuns de', Tgn, 'sao: ')
    for i in range(1, Tgn + 1):
        if Tgn % i == 0:
            print (i),
            print ('\n-')

        num = Tgn

        print_factors(num)

    Y = int(input('Digite um valor que seja maior que 1 e menor que Tgn, mas que NAO possua divisor comum com Tgn: '))
    if Tgn % Y ==0:
        print ('Invalido')
        return valorpq()

    i = 0
    for i in itertools.count():
        if (i * Y) % Tgn == 1:
            print (i),
            print ('\n-')

        elif i > 1000:
            break

    print ('Suas chaves publicas: ', n , Y)
    print ('Suas chaves privadas: ', p , q , i)

    def MsgMc():
        elements = int(input('Digite o codigo ASCII ou 0 para sair: '))
        if elements == 0:
            exit()
        for element in [elements]:
            x = element ** Y % n
            print(x)
            MsgMc()


    message = input("Digite a mensagem: ")

    print ("Texto(em ASCII):")
    for ch in message:
        print (ord(ch)),
    print ("\n")

    MsgMc()





valorpq()
