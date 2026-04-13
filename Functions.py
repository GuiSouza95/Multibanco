def autenticar_cliente(clientes, numero_conta, pin):
    for cliente in clientes:

        if cliente["numero_conta"] == numero_conta and cliente["pin"] == pin:
            return cliente
    return None


def Levantar(cliente):

    while True:
        try:
            valor = float(input("Digite o valor a levantar: "))

        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
            continue
        
        if valor <= 0:
            print("Valor deve ser maior que zero.")
            continue
        
        if valor > cliente["saldo"]:
            print("Saldo insuficiente para realizar o levantamento.")
            continue

        cliente["saldo"] -= valor
        cliente["movimentos"].append(f"Levantamento: -€{valor}")
        print(f"Levantamento de €{valor} realizado com sucesso.")

        break