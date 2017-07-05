def print_menu():
    print ('--------ASCII Coder&Decoder------')
    print ('1. Texto para ASCII')
    print ('2. ASCII para texto')
    print ('3. Sair')
    print ('----------------------------------')

loop=True

while loop:
    print_menu()
    choice = input('Selecione de [1-3]:  ')

    if choice==1:
        message = raw_input("Digite a mensagem: ")

        print "Decoded string (in ASCII):"
        for ch in message:
            print ord(ch),
        print "\n\n"

    elif choice==2:
        message = raw_input("Digite o codigo ASCII: ")

        decodedMessage = ""

        for item in message.split():
            decodedMessage += chr(int(item))

        print "Decoded message:", decodedMessage

    elif choice==3:
        exit()



