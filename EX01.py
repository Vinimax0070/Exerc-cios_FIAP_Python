
print("PRODUÇÃO MULTIMÍDIA FIAP ON!! ")
print("-" * 60)
#ENTRADA DOS VALORES
tipo_assinatura =(input("Informe o tipo da sua assinatura: Basic, Silver, Gold, Platinum:  "))
faturamento = float(input("Informe o faturamento anual obtido:R$  "))

faturaNova = 0
#FILTRAGEM DO TIPO DE ASSINATURA + PORCENTAGEM QUE IRÁ PAGAR DE ACORDO COM O LUCRO ANUAL
if tipo_assinatura.upper() == "BASIC":
    faturaNova = faturamento * 0.3
elif tipo_assinatura.upper() == "SILVER":
    faturaNova = faturamento * 0.2
elif tipo_assinatura.upper() == "GOLD":
    faturaNova = faturamento * 0.1
elif tipo_assinatura.upper() == "PLATINUM":
    faturaNova = faturamento * 0.05
else:
    print("DESCULPE, ESSE TIPO DE ASSINATURA NÂO SE ENCONTRA DISPONÍVEL")

#RESULTADO DA PORCENTAGEM QUE DEVARÁ PAGAR DE ACORDO COM O PLANO    
if faturaNova != 0:
    print(f"O faturamento anual foi de R${faturamento}. Com o tipo de assinatura {tipo_assinatura.upper()}, o cliente deve pagar:R$ {faturaNova} ")
