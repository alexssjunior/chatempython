#chat em python , para sair digitar fim.
import os

mensagens = []

nome = input("nome :")
while True :
    #limpando o terminal
    os.system("cls")
    if len (mensagens)>0:
        for M in mensagens:
            print( M ["nome"] , "-", M ['texto'])
    print("=============================================")
    #obtendo texto
    texto = input("mensagem:")
    if texto == "fim":
        break
    #adicionando mensagem a lista
    mensagens.append({
        "nome": nome ,
        "texto": texto
    })