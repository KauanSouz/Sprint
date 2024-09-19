# Função para adicionar um novo item ao estoque
def adicionar_item(estoque):
    nome = input("Digite o nome do item: ")
    quantidade = int(input("Digite a quantidade do item: "))

    if nome in estoque:
        print("Item já existente no estoque. A quantidade será atualizada.")
        estoque[nome] += quantidade
    else:
        estoque[nome] = quantidade

    print("Item adicionado ao estoque com sucesso!\n")

# Função para verificar o estoque atual
def verificar_estoque(estoque):
    print("Estoque atual:")
    for item, quantidade in estoque.items():
        print(f"{item}: {quantidade}")
    print()

# Função principal
def main():
    estoque = {}  # Dicionário para armazenar o estoque

    while True:
        print("Menu:")
        print("1. Adicionar item ao estoque")
        print("2. Verificar estoque atual")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_item(estoque)
        elif escolha == "2":
            verificar_estoque(estoque)
        elif escolha == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.\n")

if __name__ == "__main__":
    main()
