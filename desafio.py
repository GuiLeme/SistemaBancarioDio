import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        # TODO: V1 - Só terá apenas um usuário
        quantia_desejada = float(input("Quanto deseja depositar? R$ "))
        if quantia_desejada <= 0:
            print("Por favor, digite um valor coerente")
            continue
        extrato.append({"transacao": "d", "quantia": quantia_desejada, "date": datetime.datetime.now()})
        saldo += quantia_desejada
        print("Depósito efetuado com sucesso.")

    elif opcao == "s":
        quantia_desejada = float(input("Quanto deseja sacar? R$ "))
        if quantia_desejada <= saldo:
            if quantia_desejada <= limite and numero_saques < LIMITE_SAQUES:
                numero_saques += 1
                saldo -= quantia_desejada
                extrato.append({"transacao": "s", "quantia": quantia_desejada, "date": datetime.datetime.now()})
                print("Saque efetuado com sucesso, saldo de R$ {:.2f}".format(saldo))
            elif quantia_desejada > limite:
                print("Desculpe, a quantia desejada é maior do que o limite por saque.")
            elif numero_saques >= LIMITE_SAQUES:
                print("Desculpe, você ultrapassou o máximo de saques possíveis por dia.")
        elif quantia_desejada > saldo:
            print("Desculpe, saldo insuficiente para o saque.")
    
    elif opcao == "e":
        # TODO: Deve listar todos os depositos e saques realizados na conta
        # TODO: No fim exibir o saldo atual no formato: R$ xxx.xx,
        for item in extrato:
            if item["transacao"] == "s":
                print('Data: {}; Quantia: R${:.2f}; Tipo de transação: {} '.format(item["date"], item["quantia"], "saque"))
            elif item["transacao"] == "d":
                print('Data: {}; Quantia: R${:.2f}; Tipo de transação: {} '.format(item["date"], item["quantia"], "depósito"))
        print("Saldo atual R${:.2f}".format(saldo))
    
    elif opcao == "q":
        print("Obrigado pela visita, até mais!")
        break

    else:
        print("Opção inválida, por favor selecione novamene a opção desejada.")

