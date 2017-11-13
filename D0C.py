# -*- coding: utf-8 -*-

import speech_recognition as sr
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from google import search
import pyttsx
import hashlib
import os
import sys

bot = ChatBot('Test')


def pesquisa():

    en = pyttsx.init()
    en.setProperty('voice', b'brazil')
    en.say('Pesquisa ativada')
    en.runAndWait()
    print('Bot:', response)


    ip = input('Digite o que deseja procurar : ')

    for resultado in search(ip, stop=10):
        print(resultado)


conv = ['oi', 'olá', 'olá, bom dia', 'bom dia', 'bom dia, como vai?', 'estou bem', ]

ConvAg = ['obrigado', 'de nada',]

ConvInt = ['qual seu nome?','meu nome é DOC']

ConvP = 'pesquisa'

convF = ['Que filmes que você gosta?', 'eu gosto de de volta para o futuro e matrix', ]

bot.set_trainer(ListTrainer)

bot.train(conv)
bot.train(convF)
bot.train(ConvAg)
bot.train(ConvInt)


en = pyttsx.init()
en.setProperty('voice', b'brazil')
en.say('Olá Lucas')
en.runAndWait()

def AberTar():

    diretório = input('Digite o diretório do arquivo ou endereço web: ')

    os.startfile(diretório)



# MD5 Crypt ------------------------------------------------

def computeMD5hash():
    string = input('Coloque o código que queira criptografar: ')
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    print(m.hexdigest())



# MD5 Crypt -----------------------------------------------

# sha_256 Crypt -------------------------------------------

def sha256hash():
    hash_256 = input('Coloque o código que queira criptografar: ')
    h256 = hashlib.sha256()
    h256.update(hash_256.encode('utf-8'))
    print(h256.hexdigest())


# sha_256 Crypt -------------------------------------------

# sha1 Crypt -------------------------------------------

def sha1hash():
    hash_1 = input('Coloque o código que queira criptografar: ')
    h256 = hashlib.sha1()
    h256.update(hash_1.encode('utf-8'))
    print(h256.hexdigest())


# sha1 Crypt -------------------------------------------

# sha224 Crypt -------------------------------------------

def sha224hash():
    hash_1 = input('Coloque o código que queira criptografar: ')
    h256 = hashlib.sha224()
    h256.update(hash_1.encode('utf-8'))
    print(h256.hexdigest())


# sha224 Crypt -------------------------------------------

# sha384 Crypt -------------------------------------------

def sha384hash():
    hash_1 = input('Coloque o código que queira criptografar: ')
    h256 = hashlib.sha384()
    h256.update(hash_1.encode('utf-8'))
    print(h256.hexdigest())


# sha384 Crypt -------------------------------------------

# sha512 Crypt -------------------------------------------

def sha512hash():
    hash_1 = input('Coloque o código que queira criptografar: ')
    h256 = hashlib.sha512()
    h256.update(hash_1.encode('utf-8'))
    print(h256.hexdigest())


# sha512 Crypt -------------------------------------------

# Identificador de Hash ----------------------------------

def IdHash():
    from sys import executable
    from subprocess import Popen, CREATE_NEW_CONSOLE
    Popen([executable, 'hashid.py'], creationflags=CREATE_NEW_CONSOLE)

# Identificador de Hash ----------------------------------

# Decrypt ------------------------------------------------

def decrypt():
    hash_to_crack = input('Digite a Hash: ')
    dict_file = input('Digite o nome da sua wordlist + .txt: ')
    hash_type = input('Digite o tipo de Hash: ')

    if (hash_type) == 'md5':
        x = hashlib.md5

    elif (hash_type) == 'sha256':
        x = hashlib.sha256
    elif (hash_type) == 'sha1':
        x = hashlib.sha1

    elif (hash_type) == 'sha384':
        x = hashlib.sha384

    elif (hash_type) == 'sha512':
        x = hashlib.sha512

    elif (hash_type) == 'sha224':
        x = hashlib.sha224

    with open(dict_file) as fileobj:
        for line in fileobj:
            line = line.strip()
            if x(line.encode('utf-8')).hexdigest() == hash_to_crack:
                print ("Sucesso na operação da hash %s: A hash é: %s" % (hash_to_crack, line))
                return ""
    print ("Falha na operação.")

# Decrypt ------------------------------------------------

def Calc():

    en = pyttsx.init()
    en.setProperty('voice', b'brazil')
    en.say('Calculadora ativada')
    en.runAndWait()
    print('Bot:', response)


    print('---Calculadora---')
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Divisão')
    print('4- Multiplacação')
    print('5 - Módulo')
    print('----------------')

    zs = input('Selecione a opção que deseja: ')

    if (zs) == '1':
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        print(num1+num2)

    elif (zs) == '2':
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        print(num1 - num2)

    elif (zs) == '3':
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        print(num1 / num2)

    elif (zs) == '4':
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        print(num1 * num2)

    elif (zs) == '5':
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        print(num1 % num2)


def ConversorTemp():
    print('----Conversor de Temperatura------')
    print('1-Celsius para Kelvin')
    print('2-Celsius para Fahrenheit')
    print('3-Fahrenheit para Kelvin')
    print('4-Fahrenheit para Celsius')
    print('5-Kelvin para Fahrenheit')
    print('6-Kelvin para Celsius')
    x = input('Digite a opção que deseja: ')
    if (x) == '1':
        Temp1 = int(input('Digite o valor: '))
        print(Temp1 + 273)
    elif (x) == '2':
        Temp1 = int(input('Digite o valor: '))
        print(9*Temp1/5+32)
    elif (x) == '3':
        Temp1 = int(input('Digite o valor: '))
        print((Temp1+ 459.67)*5/9)
    elif (x) == '4':
        Temp1 = int(input('Digite o valor: '))
        print((Temp1-32)/1.8)
    elif (x) == '5':
        Temp1 = int(input('Digite o valor: '))
        print((Temp1*9/5)-459.67)
    elif (x) == '6':
        Temp1 = int(input('Digite o valor: '))
        print(Temp1-273)

def Mnu():
    Menu = input('Qual tipo de Hash deseja utilizar ,se não , deseja identificar ou realizar um ataque?: ')

    if (Menu) == 'MD5':
        computeMD5hash()
    elif (Menu) == 'sha256':
        sha256hash()
    elif (Menu) == 'sha1':
        sha1hash()
    elif (Menu) == 'sha224':
        sha224hash()
    elif (Menu) == 'sha384':
        sha384hash()
    elif (Menu) == 'sha512':
        sha512hash()
    elif (Menu) == 'iden':
        IdHash()
    elif (Menu) == 'decrypt':
        decrypt()


while True:

    quest = input('Você: ')

    response = bot.get_response(quest)

    if (response.confidence) > 0.5:
        en = pyttsx.init()
        en.setProperty('voice', b'brazil')
        en.say(response)
        en.runAndWait()
        print('Bot:', response)

    elif (quest) == ConvP:
        pesquisa()


    elif (quest) == 'hash':
        Mnu()

    elif (quest) == 'calculadora':
        Calc()

    elif (quest) == 'abrir':
        AberTar()

    elif (quest) == 'temp':
        ConversorTemp()

    elif (quest) == 'fechar':
        sys.exit()

    else:
        en = pyttsx.init()
        en.setProperty('voice', b'brazil')
        en.say('Não entendi')
        en.runAndWait()
        print('Não entendi')













