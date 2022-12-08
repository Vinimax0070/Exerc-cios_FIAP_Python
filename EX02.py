
print("VOTAÇÃO DOS ALUNOS FIAP!")
print("-" * 75)
#ENTRADA DO NUMERO DE ALUNOS PARTICIPANTES
total_alunos = int(input("Informe o numero total de alunos participantes: "))
seg = 0 
ter = 0
qua = 0 
qui = 0
sex = 0
#LOOP DE VOTOS DE ACORDO COM O TOTAL DE ALUNOS PARTICIPANTES
for votos in range (1,total_alunos+1):
    print("-" * 75)
    votacao = int (input(f"Aluno {votos} Escolha o seu voto:\n1-SEGUNDA:\n2-TERÇA:\n3-QUARTA:\n4-QUINTA:\n5-SEXTA:\n\nSEU VOTO:"))
    if  votacao == 1:
        seg += 1
    elif votacao == 2:
        ter += 1
    elif votacao == 3:
        qua +=1
    elif votacao == 4:
        qui+= 1
    elif votacao == 5:
        sex += 1
    else:
        print("VOCÊ DIGITOU UM VOTO INVÁLIDO, O MESMO NÂO IRÁ SER COMPUTADO")
print("-" * 30)        
print(f"Segunda total de votos: {seg}\nTerca total votos:{ter}\nQuarta total votos:{qua}\nQuinta total votos:{qui}\nSexta total votos:{sex}")    
#COMPARAÇÃO PARA VER O DIA MAIS VOTADO, QUE NO CASO SERÁ O VENCEDOR              
if seg>ter and seg>qua and seg>qui and seg>sex:
        print("-" * 30 )
        print("DIA ESCOLHIDO FOI SEGUNDA!")  
elif ter>seg and ter>qua and ter>qui and ter>sex:
        print("-" * 30)
        print("DIA ESCOLHIDO FOI TERÇA!")
elif qua>seg and qua>ter and qua>qui and qua>sex:
        print("-" * 30)
        print("DIA ESCOLHIDO FOI QUARTA!")
elif qui>seg and qui>qua and qui>ter and qui>sex:
        print("-" * 30)
        print("DIA ESCOLHIDO FOI QUINTA!")
elif sex>seg and sex>ter and sex>qua and sex>qui:
        print("-" * 30)
        print("DIA ESCOLHIDO FOI SEXTA!")
else:
    print("HOUVE UM EMPATE!!")