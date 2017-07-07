import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()

user = input('Entre com seu email: ')       
senha = input('Digite sua senha: ')
to = input('Digite o email que deseja enviar a mensagem: ')
numero = int(input('Digite a quantidade de email que você deseja enviar: '))
msg = input('Digite a mensagem que deseja enviar: ')

try:
    server.login(user, senha)
    print ('Logado com sucesso')
except:
    print('Email ou senha invalidos , lembre-se de verificar a permissão em seu email')
    
x = 0  

while(x<numero):
    
    server.sendmail(user, to, msg)
    x=x+1
    print ('Enviado ', x, 'Email')

