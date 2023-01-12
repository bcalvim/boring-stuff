senha_arquivo = open('senhaDoArquivo.txt')
palavra_secreta = senha_arquivo.read()
print('Digite sua senha.')
senha_digitada = input()
if senha_digitada == palavra_secreta:
    print('Acesso permitido')
elif senha_digitada == '12345':
    print('Essa senha é a que um idiota usaria no cadeado de sua bagagem')
else:
    print('Acesso negado')
