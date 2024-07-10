# Função para ler os dados de um contato
def ler_contato():
    nome = input("Digite o nome do contato: ")
    endereco = input("Digite o endereço do contato: ")
    telefone = input("Digite o telefone do contato: ")
    return {"Nome": nome, "Endereço": endereco, "Telefone": telefone}

# Lista para armazenar os contatos
lista_contatos = []

while True:
    print("\nMenu:")
    print("1. Incluir contato")
    print("2. Listar contatos")
    print("3. Fim")

    opcao = input("Escolha uma opção (1/2/3): ")

    if opcao == "1":
        novo_contato = ler_contato()
        lista_contatos.append(novo_contato)
        print("Contato adicionado com sucesso!")

    elif opcao == "2":
        print("\nLista de Contatos:")
        for contato in lista_contatos:
            print(f"Nome: {contato['Nome']}, Endereço: {contato['Endereço']}, Telefone: {contato['Telefone']}")

    elif opcao == "3":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida! Escolha novamente.")

print("Programa encerrado.")
