print("Escola de inglês JoWell Sant’ana")
print("-" * 60)
list_impares = 50
list_pares = 50
nota_impar = 0
nota_par = 0
quant_par = 0
quant_impar= 0
#NA PROBLEMÁTICA,NÃO FOI INFORMADO O VALOR MINÍMO E MÁXIMO DAS NOTAS, COLOQUEI ENTRA 0 A 10 QUE É O PADRÃO!!
#DIGITAR A NOTA DOS 25 ALUNOS QUE TEM NUMERO IMPAR
print("Você está digitando a nota dos alunos ímpares!")
print("-" * 60)
for impares in range (1,list_impares + 1,2):
    quant_impar += 1
    notas1 = float(input(F"DIGITE A NOTA DO ALUNO {impares}:\n"))
    while notas1 < 0 or notas1 > 10:
        print("NOTA INVÁLIDA... TENTE NOVAMENTE!")
        print("-" * 60)
        notas1 = float(input(F"DIGITE A NOTA DO ALUNO {impares}:\n"))
    nota_impar += notas1
#DIGITAR A NOTA DOS 25 ALUNOS QUE TEM O NUMERO PAR
print("-" *60 )
print("Você está digitando a nota dos alunos PARES!")
print("-" * 60)
for pares in range (2,list_pares,2):
    quant_par += 1
    notas2 = float(input(F"DIGITE A NOTA DO ALUNO  {pares}:\n"))
    while notas2 < 0 or notas2 > 10:
        print("NOTA INVÁLIDA... TENTE NOVAMENTE!")
        print("-" * 60)
        notas2 = float(input(F"DIGITE A NOTA DO ALUNO {pares}:\n"))
    nota_par += notas2
print("-" * 60)
#CALCULAR A MÉDIA DOS ALUNOS IMPARES
mediaImpar = nota_impar / 25
#CALCULAR A MÉDIA DOS ALUNOS PARES
mediaPar = nota_par / 25
#EXIBIÇÃO DAS MÉDIAS DAS SALAS
print(f"NOTA DOS NÚMEROS ÍMPARES:{mediaImpar:.2f}")
print(f"NOTA DOS NÚMEROS PARES: {mediaPar:.2f}")
#QUAL DELAS TEVE A MAIOR NOTA
print("-" * 60)
if mediaImpar > mediaPar:
    print(f"A MAIOR MÉDIA DE NOTAS FOI DOS ALUNOS ÍMPARES:\n{mediaImpar:.2f}")
elif mediaImpar < mediaPar:
    print(f"A MAIOR MÉDIA DE NOTAS FOI DOS ALUNOS PARES!:\n{mediaPar:.2f}")
elif mediaImpar == mediaPar:
    print(f"HOUVE UM EMPATE ENTRE AO ALUNOS ÍMPARES E PARES")

