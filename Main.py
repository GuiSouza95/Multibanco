from Functions import autenticar_cliente
from Menus import MenuCliente

#Lista clientes

clientes = [
    {
        "nome": "Cliente 1",
        "numero_conta": "123",
        "pin": "1234",
        "saldo": 100,
        "movimentos": []
    }
]

while True:

    numero = input("Digite o número da conta: ")
    pin = input("Digite o PIN: ")

    cliente = autenticar_cliente(clientes, numero, pin)

    if cliente:

        print("\nAutenticação bem-sucedida!")
        print(f"\nBem-vindo, {cliente['nome']}!\n")

        print(f"Numero da conta: {cliente['numero_conta']}\n")

        MenuCliente(cliente)

    else:

        print("Número de conta ou PIN incorretos.")
