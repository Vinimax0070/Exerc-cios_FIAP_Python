
print("RESOLVENDO UM ATAQUE HACKER")
print("-" * 60)
#DIGITAR OS MINUTOS ATUAIS
min = float(input("Usuário digite os minutos atuais:  "))
print("-"*60)
#CALCULANDO O FATORIAL ATRAVÉS DE LOOP
fatorial = 1
if float(min) >=1:
    for i in range (1,int(min)+1):
        fatorial = fatorial * i
print("Fatorial de ",min , " é: ",fatorial)
print("-" * 60)
#REVELANDO A SENHA CORRETA PARA O DESBLOQUEIO
print(f"Com base nos minutos digitados a sua senha é: LIBERDADE{fatorial}")
#HABILITANDO ACESSO DO USUARIO COM A SENHA CORRETA'''
while True:
    senha_acesso = input("Digite sua senha: ")

    if senha_acesso == f"LIBERDADE{fatorial}":
        print("ACESSO LIBERADO!")
        break
    else:
        print("ACESSO NEGADO!")

